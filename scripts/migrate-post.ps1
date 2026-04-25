param(
    [Parameter(Mandatory = $true)]
    [string]$RepoRoot,

    [Parameter(Mandatory = $true)]
    [string]$Title,

    [Parameter(Mandatory = $true)]
    [string]$DateIso,

    [Parameter(Mandatory = $true)]
    [string]$Slug,

    [Parameter(Mandatory = $true)]
    [string]$Description,

    [Parameter(Mandatory = $true)]
    [string]$Year,

    [Parameter(Mandatory = $true)]
    [string]$Month,

    [Parameter(Mandatory = $true)]
    [string]$SourceImageDir,

    [string[]]$ImageNames = @(),

    [string]$HeroSourceImage = "",

    [Parameter(Mandatory = $true)]
    [string]$BodyMarkdownPath,

    [string]$Author = "Alex Verboon",
    [string[]]$Tags = @(),
    [string[]]$Categories = @(),
    [string]$Alias,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

function Ensure-Path {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -Path $Path -ItemType Directory | Out-Null
    }
}

function To-YamlList {
    param([string[]]$Values)
    if (-not $Values -or $Values.Count -eq 0) {
        return @("  - Uncategorized")
    }

    $lines = @()
    foreach ($v in $Values) {
        $safe = $v.Replace('"', '\"')
        $lines += "  - $safe"
    }

    return $lines
}

if (-not (Test-Path -LiteralPath $RepoRoot)) {
    throw "RepoRoot does not exist: $RepoRoot"
}

if ($ImageNames.Count -gt 0 -and -not (Test-Path -LiteralPath $SourceImageDir)) {
    throw "SourceImageDir does not exist: $SourceImageDir"
}

if (-not (Test-Path -LiteralPath $BodyMarkdownPath)) {
    throw "BodyMarkdownPath does not exist: $BodyMarkdownPath"
}

if ($HeroSourceImage -and -not (Test-Path -LiteralPath $HeroSourceImage)) {
    throw "HeroSourceImage does not exist: $HeroSourceImage"
}

$postDir = Join-Path $RepoRoot "content/post/$Year/$Month/$Slug"
$postImagesDir = Join-Path $postDir "images"
$heroDir = Join-Path $RepoRoot "static/img/post-heroes"
$heroName = "$Slug.png"
$heroDest = Join-Path $heroDir $heroName
$indexPath = Join-Path $postDir "index.md"

Ensure-Path -Path $postDir
Ensure-Path -Path $postImagesDir
Ensure-Path -Path $heroDir

foreach ($imageName in $ImageNames) {
    $src = Join-Path $SourceImageDir $imageName
    $dst = Join-Path $postImagesDir $imageName

    if (-not (Test-Path -LiteralPath $src)) {
        throw "Missing source image: $src"
    }

    if ((Test-Path -LiteralPath $dst) -and -not $Force) {
        throw "Target image exists (use -Force to overwrite): $dst"
    }

    Copy-Item -LiteralPath $src -Destination $dst -Force:$Force
}

if ($HeroSourceImage) {
    if ((Test-Path -LiteralPath $heroDest) -and -not $Force) {
        throw "Hero target exists (use -Force to overwrite): $heroDest"
    }
    Copy-Item -LiteralPath $HeroSourceImage -Destination $heroDest -Force:$Force
}

if ((Test-Path -LiteralPath $indexPath) -and -not $Force) {
    throw "Post index exists (use -Force to overwrite): $indexPath"
}

$aliasValue = $Alias
if ([string]::IsNullOrWhiteSpace($aliasValue)) {
    $aliasValue = "/$Year/$Month/$Slug/"
}

$body = Get-Content -LiteralPath $BodyMarkdownPath -Raw
if ($null -eq $body) {
    $body = ""
}

# Rewrite local markdown links to copied post images under images/.
foreach ($imageName in $ImageNames) {
    $body = $body.Replace("]($imageName)", "](images/$imageName)")
    $body = $body.Replace("](./$imageName)", "](images/$imageName)")
}

$tagLines = To-YamlList -Values $Tags
$categoryLines = To-YamlList -Values $Categories

$escapedTitle = $Title.Replace('"', '\"')
$escapedDescription = $Description.Replace('"', '\"')
$escapedAuthor = $Author.Replace('"', '\"')

$yaml = @()
$yaml += "---"
$yaml += ('title: "{0}"' -f $escapedTitle)
$yaml += 'layout: "post"'
$yaml += "date: $DateIso"
$yaml += ('slug: "{0}"' -f $Slug)
$yaml += 'aliases:'
$yaml += ('  - "{0}"' -f $aliasValue)
$yaml += ('description: "{0}"' -f $escapedDescription)
$yaml += ('author: "{0}"' -f $escapedAuthor)
if ($HeroSourceImage) {
    $yaml += ('image: "img/post-heroes/{0}"' -f $heroName)
}
$yaml += 'tags:'
$yaml += $tagLines
$yaml += 'categories:'
$yaml += $categoryLines
$yaml += "---"
$yaml += ""

$out = ($yaml -join [Environment]::NewLine) + $body.TrimStart() + [Environment]::NewLine
Set-Content -LiteralPath $indexPath -Value $out -NoNewline:$false

Write-Output "Created post: $indexPath"
Write-Output "Copied images: $($ImageNames.Count)"
Write-Output "Hero image: $heroDest"
