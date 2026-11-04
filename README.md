# Danny Devaney — website export

Complete editable static website, exported from published version 20 (source commit `547731ba49d4783e64209ba364154dadcdab5e21`). This includes the latest “Danny being Danny” photo, responsive layout, sliders, animations, coloring sheet and SEO files.

## Start here

1. Extract this ZIP.
2. Create a GitHub repository, for example `danny-devaney-website`. A private repository is suitable.
3. Upload the **contents** of this extracted folder to the repository, keeping `dist` as a folder at the repository root. Do not upload the ZIP itself or add another parent folder.
4. In Cloudflare, open **Workers & Pages**, create a **Pages** project and choose **Import an existing Git repository**. Connect GitHub and select this repository.
5. Use these settings:

| Setting | Value |
| --- | --- |
| Production branch | `main` (or the branch you uploaded) |
| Framework preset | None |
| Build command | `exit 0` |
| Build output directory | `dist` |
| Root directory | Leave blank (repository root) |
| Environment variables | None required |

6. Deploy. Open the `pages.dev` address Cloudflare returns and check mobile layout, photos, sliders, video and coloring-sheet download.
7. Add your domain in the Pages project's **Custom domains** settings. Follow Cloudflare's DNS instructions for the exact domain. Do not change email/MX records. Keep the current website live until the new site and HTTPS work.

Cloudflare's labels can change. Choose **Pages**, not a Worker application requiring a Worker entrypoint. Subsequent GitHub commits will automatically redeploy the connected Pages project.

## Set the final domain before launch

The export preserves the current canonical address:
`https://danny-devaney-the-show.nielsduinker.chatgpt.site`

When the permanent domain is known, update the old origin in these four files:

- `dist/index.html` — canonical URL, social sharing metadata and structured data.
- `dist/sitemap.xml`
- `dist/robots.txt`
- `dist/llms.txt`

An optional Python helper updates all four together. From this extracted folder run:

```sh
python3 tools/set-site-url.py https://YOUR-FINAL-DOMAIN
```

Replace the example with the real HTTPS domain, then commit the changed files to GitHub. Choose one canonical host (www or non-www) and redirect the other to it. Submit the new `/sitemap.xml` in Google Search Console after verifying domain ownership. Hosting alone does not transfer existing search rankings or configure redirects from the previous host.

## Edit and preview

- `dist/index.html`: copy, layout, links and most page images.
- `dist/style.css`: desktop/mobile layout, crops, colors and animation styles.
- `dist/script.js`: routine content, sliders, menus, video and falling props.
- `dist/assets/`: photographs, graphics, GIF, icons and coloring sheet.

No npm installation, compile step, API keys, database or ChatGPT subscription is needed to serve the exported site. For a local preview run:

```sh
python3 -m http.server 8000 --directory dist
```

Then open `http://localhost:8000`. Stop with Ctrl+C.

## External services and assets

Photos and local graphics are included. Any remote venue logos that could be retrieved during export were bundled into `dist/assets` and their references updated in this export only. See `external-images.txt` for image URLs that remain remote, if any.

Google Fonts remains an online dependency. YouTube videos remain embedded and require internet access; the export does not download third-party videos. Booking still links to Danny's existing contact page. Social media, ticketing, reviews, book and podcast links continue to open their respective websites. The export is source code, not an admin CMS; edit files or ask for help with updates. Existing photo/logo/quote rights remain applicable; no new content license is granted by exporting.

The original Sites project, access settings, Git history, credentials and platform-specific hosting files are intentionally excluded. The live Sites website has not been changed by this export.

## Official setup references

- https://developers.cloudflare.com/pages/framework-guides/deploy-anything/
- https://developers.cloudflare.com/pages/get-started/git-integration/
- https://developers.cloudflare.com/pages/configuration/custom-domains/

