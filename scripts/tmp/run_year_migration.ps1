$ErrorActionPreference='Continue'
$repoRoot = (Get-Location).Path
$uploadsRoot = 'C:\Dev\Alex\NewBlog\wp-source\uploads'
$yearSummaries = @()
$allFailed = @()
foreach ($year in 2008..2018) {
  Write-Output "=== YEAR $year ==="
  $extractOutput = & python .\scripts\extract_posts_by_year.py $year 2>&1
  $extractExit = $LASTEXITCODE
  $extractOutput | ForEach-Object { Write-Output $_ }

  $jsonPath = Join-Path $repoRoot "scripts\extracted_${year}_posts.json"
  $posts = @()
  if (Test-Path -LiteralPath $jsonPath) {
    try {
      $parsed = Get-Content -LiteralPath $jsonPath -Raw | ConvertFrom-Json
      if ($null -ne $parsed) { $posts = @($parsed) }
    } catch {
      Write-Output "[ERROR] Failed to parse $jsonPath : $($_.Exception.Message)"
    }
  } else {
    Write-Output "[WARN] Missing extraction file: $jsonPath"
  }

  $extractCount = $posts.Count
  $attempted = 0
  $succeeded = 0
  $failed = 0
  $failedSlugs = @()

  foreach ($post in $posts) {
    $attempted++
    $sourceImageDir = Join-Path (Join-Path $uploadsRoot ([string]$post.year)) ([string]$post.month)
    $heroPath = $null
    if (-not [string]::IsNullOrWhiteSpace([string]$post.hero_image)) {
      $candidateHero = Join-Path $sourceImageDir ([string]$post.hero_image)
      if (Test-Path -LiteralPath $candidateHero) { $heroPath = $candidateHero }
    }

    $author = [string]$post.author
    if ($author -eq 'alex') { $author = 'Alex Verboon' }
    if ([string]::IsNullOrWhiteSpace($author)) { $author = 'Alex Verboon' }

    $params = @{
      RepoRoot = $repoRoot
      Title = [string]$post.title
      DateIso = [string]$post.date
      Slug = [string]$post.slug
      Description = [string]$post.description
      Year = [string]$post.year
      Month = [string]$post.month
      SourceImageDir = $sourceImageDir
      ImageNames = @([string[]]$post.image_list)
      BodyMarkdownPath = [string]$post.body_file_path
      Author = $author
      Tags = @([string[]]$post.tags)
      Categories = @([string[]]$post.categories)
      Force = $true
    }
    if ($heroPath) { $params.HeroSourceImage = $heroPath }

    try {
      & .\scripts\migrate-post.ps1 @params
      $succeeded++
    } catch {
      $failed++
      $failedSlugs += [string]$post.slug
      Write-Output "[MIGRATE-ERROR] $($post.slug): $($_.Exception.Message)"
    }
  }

  $yearSummaries += [pscustomobject]@{
    Year = $year
    ExtractionCount = $extractCount
    Attempted = $attempted
    Succeeded = $succeeded
    Failed = $failed
    FailedSlugs = $failedSlugs
    ExtractExitCode = $extractExit
  }

  if ($failedSlugs.Count -gt 0) {
    $allFailed += $failedSlugs | ForEach-Object { "${year}/$_" }
  }
}

$slashPattern = '^date:\s*\d{1,2}/\d{1,2}/\d{4}'
$slashMatches = @()
Get-ChildItem -LiteralPath .\content\post -Recurse -Filter index.md -File | ForEach-Object {
  $m = Select-String -LiteralPath $_.FullName -Pattern $slashPattern
  if ($m) {
    $rel = $_.FullName.Substring($repoRoot.Length).TrimStart('\\')
    $yearPart = if ($rel -match '^content\\post\\(\d{4})\\') { $Matches[1] } else { 'unknown' }
    $slashMatches += [pscustomobject]@{ Year = $yearPart; Path = $rel }
  }
}
$slashByYear = $slashMatches | Group-Object Year | Sort-Object Name | ForEach-Object {
  [pscustomobject]@{ Year = $_.Name; Count = $_.Count }
}

Write-Output '=== SUMMARY ==='
$yearSummaries | ForEach-Object {
  Write-Output ("Year {0}: extracted={1}, attempted={2}, succeeded={3}, failed={4}" -f $_.Year,$_.ExtractionCount,$_.Attempted,$_.Succeeded,$_.Failed)
}
Write-Output '=== FAILED SLUGS ==='
if ($allFailed.Count -eq 0) { Write-Output 'None' } else { $allFailed | ForEach-Object { Write-Output $_ } }
Write-Output '=== DATE SLASH VALIDATION ==='
if ($slashByYear.Count -eq 0) {
  Write-Output 'No slash-format date lines found.'
} else {
  $slashByYear | ForEach-Object { Write-Output ("Year {0}: {1}" -f $_.Year,$_.Count) }
}
Write-Output ("Total slash-format date lines: {0}" -f $slashMatches.Count)
