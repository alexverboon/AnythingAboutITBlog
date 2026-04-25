$xmlPath = 'C:\Dev\Alex\NewBlog\anythingaboutit.WordPress.2026-04-11.xml'
$targetUrl = 'https://www.verboon.info/2022/08/microsoft-defender-for-identity-npcap-driver-update/'

[xml]$doc = Get-Content -Raw -LiteralPath $xmlPath
$ns = New-Object System.Xml.XmlNamespaceManager($doc.NameTable)
$ns.AddNamespace('content','http://purl.org/rss/1.0/modules/content/')
$ns.AddNamespace('dc','http://purl.org/dc/elements/1.1/')
$ns.AddNamespace('wp','http://wordpress.org/export/1.2/')
$ns.AddNamespace('excerpt','http://wordpress.org/export/1.2/excerpt/')

function Normalize-Url([string]$u) {
  if ([string]::IsNullOrWhiteSpace($u)) { return '' }
  return $u.Trim().TrimEnd('/').ToLowerInvariant()
}

$targetNorm = Normalize-Url $targetUrl
$targetSlug = 'microsoft-defender-for-identity-npcap-driver-update'
$targetYear = 2022
$targetMonth = 8

$items = $doc.SelectNodes('/rss/channel/item')
$publishedPosts = @($items | Where-Object {
  ($_.SelectSingleNode('wp:post_type',$ns).InnerText -eq 'post') -and
  ($_.SelectSingleNode('wp:status',$ns).InnerText -eq 'publish')
})

$candidates = foreach ($item in $publishedPosts) {
  $link = $item.SelectSingleNode('link').InnerText
  $linkNorm = Normalize-Url $link
  $slug = $item.SelectSingleNode('wp:post_name',$ns).InnerText
  $pubDateText = $item.SelectSingleNode('pubDate').InnerText
  $dt = $null
  [void][datetime]::TryParse($pubDateText, [ref]$dt)
  $dateMatch = ($dt -and $dt.Year -eq $targetYear -and $dt.Month -eq $targetMonth)

  $score = 0
  if ($linkNorm -eq $targetNorm) { $score = 100 }
  elseif (($slug -eq $targetSlug) -and $dateMatch) { $score = 50 }

  [pscustomobject]@{
    Score = $score
    Item = $item
    PubDate = $pubDateText
  }
}

$best = $candidates | Sort-Object -Property @{Expression='Score';Descending=$true}, @{Expression='PubDate';Descending=$true} | Select-Object -First 1
if (-not $best -or $best.Score -le 0) {
  throw 'No matching post found by link or slug+date.'
}

$item = $best.Item
$contentNode = $item.SelectSingleNode('content:encoded',$ns)
$excerptNode = $item.SelectSingleNode('excerpt:encoded',$ns)
$content = if ($contentNode) { $contentNode.InnerText } else { '' }
$excerpt = if ($excerptNode) { $excerptNode.InnerText } else { '' }
$categories = @($item.SelectNodes('category') | ForEach-Object {
  [pscustomobject]@{
    domain = $_.GetAttribute('domain')
    nicename = $_.GetAttribute('nicename')
    text = $_.InnerText
  }
})

$urls = New-Object System.Collections.Generic.HashSet[string]
if ($content) {
  [regex]::Matches($content,"<img[^>]*?\\s(?:src|data-src)\\s*=\\s*['\"']([^'\"']+)['\"']",'IgnoreCase') | ForEach-Object {
    [void]$urls.Add($_.Groups[1].Value)
  }
  [regex]::Matches($content,"<img[^>]*?\\ssrcset\\s*=\\s*['\"']([^'\"']+)['\"']",'IgnoreCase') | ForEach-Object {
    foreach ($entry in ($_.Groups[1].Value -split ',')) {
      $u = ($entry.Trim() -split '\\s+')[0]
      if ($u) { [void]$urls.Add($u) }
    }
  }
}

$result = [ordered]@{
  match = [ordered]@{
    score = $best.Score
    matchedBy = if ($best.Score -eq 100) { 'link' } else { 'slug+pubDate(2022/08)' }
    targetUrl = $targetUrl
  }
  post = [ordered]@{
    title = $item.SelectSingleNode('title').InnerText
    link = $item.SelectSingleNode('link').InnerText
    pubDate = $item.SelectSingleNode('pubDate').InnerText
    post_date = $item.SelectSingleNode('wp:post_date',$ns).InnerText
    post_date_gmt = $item.SelectSingleNode('wp:post_date_gmt',$ns).InnerText
    post_name = $item.SelectSingleNode('wp:post_name',$ns).InnerText
    excerpt_encoded = $excerpt
    categories = $categories
    creator = $item.SelectSingleNode('dc:creator',$ns).InnerText
    guid = $item.SelectSingleNode('guid').InnerText
    content_length = $content.Length
    content_preview_1200 = if ($content.Length -gt 1200) { $content.Substring(0,1200) } else { $content }
  }
  image_src_urls_unique = @($urls)
}

$result | ConvertTo-Json -Depth 8
