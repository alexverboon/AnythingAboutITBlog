# Post Migration Helper

Use this helper to speed up Hugo post migrations after you extract and convert content from WordPress XML.

## Script

`scripts/migrate-post.ps1`

## Required Inputs

- Metadata: title, date, slug, description, year, month
- Source image folder and referenced image filenames
- Hero image source file
- Markdown body file path (body only, no front matter)

## Example

```powershell
pwsh ./scripts/migrate-post.ps1 \
  -RepoRoot "C:\Dev\Alex\blog\AnythingAboutITBlog" \
  -Title "Users can create AzureAD tenants" \
  -DateIso "2022-11-22T22:13:09Z" \
  -Slug "users-can-create-azuread-tenants" \
  -Description "Review and monitor the Azure AD setting that allows users to create new tenants, with KQL detection queries." \
  -Year "2022" \
  -Month "11" \
  -SourceImageDir "C:\Dev\Alex\NewBlog\wp-source\uploads\2022\11" \
  -ImageNames "112222_2202_Userscancre1.png","112222_2202_Userscancre2.png" \
  -HeroSourceImage "C:\Dev\Alex\NewBlog\wp-source\uploads\2022\11\CREATETENANT.png" \
  -BodyMarkdownPath "C:\Temp\body.md" \
  -Tags "AllowedToCreateTenants","AzureAD","KQL" \
  -Categories "Azure Active Directory","KQL","Security"
```

## Notes

- Use `-Force` to overwrite existing files.
- Hero image is automatically copied to `static/img/post-heroes/<slug>.png`.
- The script creates `content/post/<year>/<month>/<slug>/index.md` with front matter + body.
