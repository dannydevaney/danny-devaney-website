#!/usr/bin/env python3
"""Update the exported site's SEO origin after choosing a permanent domain."""
import argparse
import re
from pathlib import Path
from urllib.parse import urlsplit

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('url', help='Final HTTPS website origin, without a path')
args = parser.parse_args()
target = urlsplit(args.url.strip())
if (target.scheme != 'https' or not target.hostname or target.username
        or target.password or target.query or target.fragment
        or target.path not in ('', '/') or target.port):
    parser.error('Use an HTTPS origin such as https://www.example.com, without a path or port.')
new_origin = 'https://' + target.netloc.lower()
root = Path(__file__).resolve().parents[1] / 'dist'
html = (root / 'index.html').read_text(encoding='utf-8')
match = re.search(r'<link\s+rel="canonical"\s+href="(https://[^"/]+)', html)
if not match:
    parser.error('Could not identify the current canonical origin; no files were changed.')
old_origin = match.group(1)
files = [root / name for name in ('index.html', 'sitemap.xml', 'robots.txt', 'llms.txt')]
contents = [(p, p.read_text(encoding='utf-8')) for p in files]
for path, text in contents:
    path.write_text(text.replace(old_origin, new_origin), encoding='utf-8')
print(f'Updated SEO origin from {old_origin} to {new_origin} in four files.')
print('Commit these changes to GitHub to trigger your connected Cloudflare Pages deployment.')
