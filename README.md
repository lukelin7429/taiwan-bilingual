# Taiwan Bilingual · 跨縣市雙語校園

Cross-county umbrella hub for bilingual campus pages of schools **outside Changhua**.
Served at **https://taiwan-bilingual.org** via GitHub Pages.

Changhua-county schools live separately at https://changhua-bilingual.org.

## Architecture

This repo serves the apex landing page only. Each school keeps its **own repo**,
hosted on a subdomain:

| Subdomain | School | Repo | County |
|-----------|--------|------|--------|
| `tbps.taiwan-bilingual.org`  | 太保國小 Taibao Elementary       | `tbps-bilingual`  | 嘉義縣 |
| `tpjh.taiwan-bilingual.org`  | 太保國中 Taibao Junior High      | `tpjh-bilingual`  | 嘉義縣 |
| `klnes.taiwan-bilingual.org` | 槺榔國小 KangLang Elementary     | `klnes-bilingual` | 臺中市 |
| `ycsh.taiwan-bilingual.org`  | 永慶高中 Young Docents           | `ycsh-bilingual`  | 嘉義縣 |

## Adding a new school

1. Build the school in its own repo (5-file structure, relative links only).
2. Add a `CNAME` file to that repo: `<slug>.taiwan-bilingual.org`
3. Add a Cloudflare DNS record: `CNAME  <slug>  lukelin7429.github.io  (DNS only)`
4. Add a card to this repo's `index.html`.
5. After the cert goes green in the school repo's Settings → Pages, enable Enforce HTTPS.
