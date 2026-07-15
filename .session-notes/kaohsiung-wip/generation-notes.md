# Kaohsiung Session A → Session B handoff notes

Read this FIRST before dispatching Session B generation agents — these are cross-batch special cases discovered during research that need special handling, beyond what's already noted inline in each `researched_batch_NN.txt` file.

## Schools to SKIP (do not generate a page)

- **廣應國小** (guangying-es, Batch13, Linyuan District) — research strongly indicates this school does not exist. Kaohsiung's official Linyuan District Office lists exactly 6 elementary schools + 1 JH; no 廣應國小 appears. "廣應" is a real village name served by 王公國小, not a separate school. Leave as "Coming soon" in the county directory, flag to Luke, matching the Hsinchu County 香園國小 / Taitung 垂柳國小 precedent. Remove this row from whatever genlist a generation agent is given, or explicitly instruct the agent not to build it.
- **高鳳工家** (Batch05, Siaogang District — not on the original genlist as a school to build, but flagged during research as closed since 2020, confirm it isn't accidentally on any genlist before generation)

## Slug/genlist corrections already applied

- **六龜高級中學** (Batch13): 高雄市立六龜高級中學 and 六龜高級中學附屬國民中學 are confirmed to be ONE institution (a 完全中學, same pattern as 林園高中's own JH division). `genlist_Batch13.txt` has been corrected so BOTH rows use slug `liugui-hs` — build ONE page covering both divisions.

## Name corrections to apply during generation (keep genlist name as badge-matching key)

- **新庄國小 / 新莊國小** (shanlin-xinzhuang-es, Batch14, Shanlin District): the genlist and county directory list this school as 新莊國小 (character 莊), but the school's actual official name is 新庄國小 (character 庄) — confirmed from the school's own site and all primary sources. Build the page under the CORRECT name 新庄國小, but keep 新莊國小 (the directory's name) as the badge-matching key when running the badge-update script — same "Magong pattern" used for prior counties' directory-name errors.

## Combined institutions (single page, both directory rows route to same slug — already reflected in genlists)

- **國立高科實驗高級中等學校** (gaoke-hs, Batch14, Ciaotou District) — combined JH+SH, both genlist rows already use slug `gaoke-hs`. Brand-new (formally established Aug 2025), currently operating temporarily in Nanzi District while its permanent Ciaotou campus is built (~2028 target) — note this honestly, don't claim it's physically in Ciaotou yet.
- **巴楠花部落中小學** (banahua-jhes, Batch14, Shanlin District) — combined ES+JH, both genlist rows already use slug `banahua-jhes`. Bunun Indigenous-focus school; the "padan/silvergrass" name-origin story MUST be framed explicitly as the school's own account/oral tradition, not asserted as verified etymology.
- **翠屏國民中小學** (cuiping-jhes, Batch07, Nanzih District) — appears only ONCE in the directory (tagged junior-high) despite being a combined ES+JH institution by its own name and structure. Build with "Grades: K-9" or "Combined Elementary & Junior High" quick-fact, no dual-row routing needed since only one directory row exists.

## Sensitive histories — handle with dignity, no sensationalizing

- **小林國小** (Xiaolin ES, Batch18, Jiaxian District) — the original village and school were destroyed in the Aug 9 2009 Typhoon Morakot landslide-dammed-lake breach; ~491 people missing/deceased. Rebuilt at Wuli-pu, reopened 2012. The community identifies as Taivoan (a Siraya-related Plains Indigenous group); frame the "as long as the culture remains, Xiaolin will remain" sentiment as the community's own stated account, not an outside anthropological classification. Write factually, respectfully, no dramatization.
- **民權國小** (Namasia, Batch18) — original campus buried by a Morakot landslide 2009, rebuilt 2011 with Diamond-level green building certification, now also serves as a typhoon-season community shelter. Honest, dignified treatment.
- **紅毛港國小** (Batch17/Qianzhen area — check which batch has this) — complex village-relocation history (Hongmaogang fishing village demolished for port expansion, four school name changes, one-year enrollment suspension 2007). Verify secondary-source dates against the school's own site before publishing exact years.
- **鳳林國小** (Batch05, Xiaogang District) — tied to the ongoing Dalinpu village relocation for port/steel expansion; its "last" 100th-anniversary celebration was in 2017 anticipating the original campus becoming disused. Verify current operating status before publishing (may have relocated since).

## Indigenous-community schools — name legends must be framed as oral tradition, not literal fact

- **那瑪夏國中/民權國小/民生國小** (Namasia District, Batch18) — Kanakanavu/Bunun community; the "Namasia/Maasia" young-hero legend must be presented as the community's own oral tradition (two variant tellings exist), not literal history.
- **茂林國中/國小、多納國小** (Maolin District, Batch18) — Rukai territory, home to the famous purple crow butterfly valley. 茂林國中 and 茂林國小 share the SAME founding institution (1917 Aboriginal Children's Education Institute) before splitting into separate schools in 1999/2005 — write their histories consistently as siblings, not independent foundings. 多納國小 became an official Rukai-language experimental school (2017, "Kungadavane Rukai Ethnic Experimental Elementary School").
- **桃源國中/國小、建山國小、樟山實驗國民小學、寶山國小、興中國小** (Taoyuan District — a mountain district of Kaohsiung City, NOT Taoyuan City) — Bunun-majority with some Hla'alua community; the "Bunun families migrated from Nantou/Taitung ~180 years ago, Hla'alua as earliest inhabitants" narrative is the community's own account, present accordingly.
  - FLAG: 興中國小's continuity is unconfirmed — sources describe a 興中分班 merged into 建山國小 in 1970 (ceasing separate existence), yet 興中國小 exists today as an independent school with no explained re-establishment. Build honestly with available facts, flag the gap rather than inventing a continuity narrative.
  - FLAG: 樟山實驗國民小學's "實驗" (experimental) designation in the genlist name is not corroborated by any source found (all call it plainly 樟山國民小學) — double check, and if unconfirmed, don't assert an experimental-education claim not otherwise supported.
- **博屋瑪國小-style legend framing applies generally**: any Indigenous place/school-name legend in this county (Kanakanavu, Rukai, Bunun, Siraya/Taivoan, Makatao) should use the same "presented as the community's own account, not verified fact" language established in prior counties (Taichung's Bowuma, New Taipei's Wulai).

## Recurring cross-county and cross-district name collisions (informational — slugs already handle these via ks- prefix or township qualifiers, listed here just so generation agents don't get confused mid-write)

- 中正國小/中正高中/中正高工 — THREE separate Kaohsiung institutions sharing "中正" (Lingya ES+HS, Qianzhen VS) — do not merge.
- 忠孝國小 — appears in Fongshan, Yancheng, plus a separate 忠孝國中 — all confirmed distinct Kaohsiung schools; nationally there are 5+ "忠孝國中" alone.
- 鼓山國小 (Gushan District) vs 姑山國小 (Dashu District) vs 鼓岩國小 (also Gushan District!) vs a Qishan District namesake — FOUR similar-sounding schools, all confirmed genuinely distinct. Double-check slugs match: qishan-gushan-es (Qishan), gushan-es (Gushan's own), dashu-gushan-es (Dashu's 姑山), plus 鼓岩國小 (Guyan, separate slug) in Gushan too.
- 右昌國小 vs 油廠國小 (both Nanzih District) — confirmed genuinely distinct (1918 Japanese-era school vs 1947 CPC refinery-workers' school).
- 五林國小 (Ciaotou) vs 烏林國小 (Renwu) — different characters, same pinyin, confirmed distinct, township-qualified slugs already applied.
- 福安國小 (Meinong) vs 復安國小 (Alian) — different characters, same pinyin, confirmed distinct, township-qualified slugs already applied.
- 大社國小 — TWO genuinely distinct schools (Dashe District's own-name school, and Lujhu District's — the older, larger one that spawned 路竹國小).
- 蚵寮國小/蚵寮國中 (Ziguan District, Kaohsiung) — confirmed distinct from an unrelated same-named 蚵寮國小 in Beimen District, Tainan City.
- 民權國小 — appears in Cianjhen District (modern, 1999) AND Namasia District (1904, Indigenous-community) — confirmed genuinely distinct, ks- prefix disambiguates.
- 木柵國小 (Neimen District, Kaohsiung) — confirmed distinct from Taipei's 木柵國小 (Wenshan District).

## University-affiliated / special institutional notes

- **國立高雄師範大學附屬高級中學** (nknu-fushu-hs, Batch11, Lingya) — NKNU-affiliated but built as a regular senior-high page like Taichung's NCHU-affiliated schools, not a university page.
- **國光高級中學** (Batch07, Nanzih) — founded 1959 as a PRIVATE CPC (oil company) employee-children's school, went public and became affiliated with National Sun Yat-sen University in 2005. Flag this "formerly private + now university-affiliated" history explicitly.
- **七賢國中** (Gushan District, this project's slug) — founded 1969 in Qianjin District, only relocated to its current Gushan District campus 2009-2012. Institutional history (1969) predates its physical Gushan location — write both facts honestly.

## Polyphone / transliteration notes

- **茄萣** (Cieding District) — 茄 is read "jiā" here (as in "jiading"), NOT "qié" as in the common word for eggplant. Slugs already use "jiading."
- No other new polyphone issues beyond the standing checklist (重、都、假、藏、量、少、率、長) were found this county.

## Founding-year handling reminders (per standing project rule)

- Pre-1945 foundings: show Western year + "(Japanese colonial era)," never force an awkward ROC-year conversion. Several schools in this county use pre-ROC dates like "民國前5年" (甲仙國小, ~1907) — these ARE valid negative-ROC-year notations for pre-1912 dates, treat exactly like any other Japanese-colonial-era founding, don't try to "convert" them into a positive ROC year.
- Unknown founding years: omit gracefully, never fabricate. This county's research turned up an unusually high number of "not found" founding years (many schools have JS/frame-rendered official sites that block scraping) — this is expected and fine, just be honest on the page.
