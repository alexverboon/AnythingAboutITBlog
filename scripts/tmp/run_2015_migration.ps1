$repoRoot = (Get-Location).Path
$jsonPath = Join-Path $repoRoot 'scripts/extracted_2015_posts.json'
$posts = Get-Content -LiteralPath $jsonPath -Raw | ConvertFrom-Json

$authorMap = @{
    'alex' = 'Alex Verboon'
    'alex verboon' = 'Alex Verboon'
}

$attempted = 0
$succeeded = 0
$failedSlugs = New-Object System.Collections.Generic.List[string]

foreach ($post in $posts) {
    $attempted++
    $slug = [string]$post.slug
    $year = [string]$post.year
    $month = ('{0:D2}' -f [int]$post.month)

    $authorKey = ([string]$post.author).ToLowerInvariant()
    if ($authorMap.ContainsKey($authorKey)) {
        $author = $authorMap[$authorKey]
    } elseif ([string]::IsNullOrWhiteSpace([string]$post.author)) {
        $author = 'Alex Verboon'
    } else {
        $author = [string]$post.author
    }

    $sourceSlug = $slug -replace '-\d+$',''
    $sourceImageDir = Join-Path $repoRoot ("content/post/{0}/{1}/{2}/images" -f $year, $month, $sourceSlug)
    if (-not (Test-Path -LiteralPath $sourceImageDir)) {
        $sourceImageDir = Join-Path $repoRoot ("content/post/{0}/{1}/{2}/images" -f $year, $month, $slug)
    }

    $imageNames = @()
    if ($null -ne $post.image_list) { $imageNames = @($post.image_list | ForEach-Object { [string]$_ }) }

    $description = [string]$post.description
    if ($null -eq $description) { $description = '' }

    $params = @{
        RepoRoot = $repoRoot
        Title = [string]$post.title
        DateIso = [string]$post.date
        Slug = $slug
        Description = $description
        Year = $year
        Month = $month
        SourceImageDir = $sourceImageDir
        ImageNames = $imageNames
        BodyMarkdownPath = [string]$post.body_file_path
        Author = $author
        Tags = @($post.tags | ForEach-Object { [string]$_ })
        Categories = @($post.categories | ForEach-Object { [string]$_ })
        Force = $true
    }

    $heroName = [string]$post.hero_image
    if (-not [string]::IsNullOrWhiteSpace($heroName)) {
        $heroCandidate = Join-Path $sourceImageDir $heroName
        if (Test-Path -LiteralPath $heroCandidate) {
            $params['HeroSourceImage'] = $heroCandidate
        }
    }

    try {
        & .\scripts\migrate-post.ps1 @params | Out-Null
        $succeeded++
    } catch {
        $failedSlugs.Add($slug) | Out-Null
        Write-Output ("[FAIL] {0}: {1}" -f $slug, $_.Exception.Message)
        continue
    }
}

$failedCount = $failedSlugs.Count
Write-Output ("Attempted={0}; Succeeded={1}; Failed={2}" -f $attempted, $succeeded, $failedCount)
if ($failedCount -gt 0) {
    Write-Output ("Failed slugs: {0}" -f (($failedSlugs | Sort-Object) -join ', '))
} else {
    Write-Output 'Failed slugs: (none)'
}

$expectedSlugs = @($posts | ForEach-Object { [string]$_.slug } | Sort-Object -Unique)
$actualSlugs = @(Get-ChildItem -LiteralPath (Join-Path $repoRoot 'content/post/2015') -Recurse -File -Filter 'index.md' | ForEach-Object { Split-Path -Leaf $_.DirectoryName } | Sort-Object -Unique)
$missingSlugs = @($expectedSlugs | Where-Object { $_ -notin $actualSlugs })

if ($missingSlugs.Count -gt 0) {
    Write-Output ("Missing slugs: {0}" -f ($missingSlugs -join ', '))
} else {
    Write-Output 'Missing slugs: (none)'
}

$indexCount = (Get-ChildItem -LiteralPath (Join-Path $repoRoot 'content/post/2015') -Recurse -File -Filter 'index.md').Count
Write-Output ("Final 2015 index.md count: {0}" -f $indexCount)
