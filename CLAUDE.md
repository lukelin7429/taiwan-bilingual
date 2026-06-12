# CLAUDE.md — taiwan-bilingual.org 跨縣市學校雙語站家族

> 這份每次在本 repo 工作都會自動載入。動任何頁面前先讀三大鐵律。
> 架構＝**彰化以外**的學校，**每校一個獨立 repo + 子網域**掛 `taiwan-bilingual.org`（**不可**用 changhua-bilingual.org，那是彰化專屬）。
> 設計規範與彰化各校**完全一致**（同一個 Luke、同一套品味）——以下鐵律違反過太多次，是硬規則不是建議。

---

## 🔴 交付前三大鐵律（每次動工逐項檢查，不可略過）

### 1. Banner / Hero 照片 — 禁全幅遮罩
- 照片清晰時，**不要**蓋全幅色彩/暗化 overlay（橘黃紅染色、整片暗化）——會弄得「髒髒的」。
- 文字可讀性只用**底部單一漸層 scrim**：`linear-gradient(180deg, transparent 0%, transparent ~40%, rgba(10,20,42,.62) 100%)`，再給**字**加 `text-shadow:0 1px 10px rgba(0,0,0,.5)`。
- 本家族 tbps/tpjh 的 banner 已是此做法，照著做。
- 細節：memory `feedback_banner_no_muddy_overlay`

### 2. 字體 — body ≥20/23px、次要文字 ≥17/19px、絕對 px、禁 rem
- **禁** `1rem` / `clamp(1rem,…)` 當 body 或重要段落（換算後桌機 14–18px = Luke 眼中「小到可怕」）。
- 下限：body ≥ **20px** mobile / **22–23px** desktop；**任何要被讀的文字**（caption、中文補述、list item、卡片小標、對話框）≥ **17px / 19px**；純裝飾 eyebrow/badge 才可 12–14px。
- 斷點 **720px**。font stack：`'Inter'/'Playfair Display'/'Lato' + 'PingFang TC','Apple LiGothic Medium','Microsoft JhengHei',sans-serif`、白底 #fff。
- **字級母版**＝彰化 repo `schools/yangming-jhs/`（`~/Documents/Claude/repos/changhua-bilingual/schools/yangming-jhs/index.html` 的 :root + 字級表）；本家族各 repo 已照此建立，新頁沿用本 repo 既有 CSS、不要憑直覺改小。
- 細節 + 完整字級表：memory `feedback_school_site_typography`

### 3. Word of the Day / Lessons 分類 — 主題色卡片網格（大莊母版）
- WOTD / 課程落地頁用大莊那套「主題色 emoji 卡片網格」：`.units` grid（1→2→3 欄）+ 每分類自己的漸層主題色 + 巨型 emoji hero + hover 上浮。
- 母版：彰化 repo `schools/dajuang/lessons/`。
- 細節：memory `reference_dajuang_wotd_category_design`

---

## 🟠 跨縣市專屬鐵律

### A. 每校鎖定主色，不可撞（含彰化各校）
| Repo | 子網域 | 學校 | 鎖定主色 |
|---|---|---|---|
| `taiwan-bilingual` | apex | 傘站首頁 | island-jade `#2f5d4f` |
| `klnes-bilingual` | klnes. | 槺榔國小（台中清水） | teal |
| `tbps-bilingual` | tbes. | 太保國小（嘉義·Luke 故鄉校） | 墨藍 `#1F3A5F` + 赭金 `#B07D3C` |
| `tpjh-bilingual` | tbjh. | 太保國中（Luke 母校） | garnet `#7A2A3A` + bronze |
| `ycsh-bilingual` | ycsh. | 永慶高中（嘉義） | 墨黑 `#23262b` + 朱砂 `#b5392e` |
改某校時用該校自己的主色，不要套到別校、也不要撞色。

### B. 不對接彰化縣府/教育處
跨縣市校不放彰化縣相關內容、配色脈絡。

### C. 部署 SOP（子網域，非 apex）
每校 repo 自帶 `CNAME` 檔（`<slug>.taiwan-bilingual.org`）+ Cloudflare `CNAME <slug> lukelin7429.github.io (DNS only)`。**先設好 DNS 再 push CNAME，憑證變綠才勾 Enforce HTTPS**——憑證簽發非同步，推完內容立刻停手（memory `feedback_no_inline_tls_changes`）。apex 用 4 條 A 紀錄。

---

## ☑ 交付前自檢（mobile viewport 從頭滑到尾）
1. ☐ Banner 沒有全幅遮罩，照片乾淨？
2. ☐ body ≥20/23px、次要文字 ≥17/19px、**完全沒有 rem**？
3. ☐ WOTD/Lessons 頁用了主題色卡片網格？
4. ☐ 用的是**本校鎖定主色**、沒撞其他校？
5. ☐ 滿版白底、不鎖中央窄欄？

**只要有一段中文小到要瞇眼、banner 霧濁、或撞到別校配色，就是不及格，重做後才交付。**

---

## 其他常踩規則（細節在 memory）
- 每頁都要 banner，子頁不重用首頁那張；用校門/校舍/校徽/地景，不用人物照、不放會變動數字
- News 頁**不外連中文官網**，用英文摘要卡自包（memory `feedback_no_link_to_chinese_official_site`）
- 卡片/logo 左上角**不放單一中文字**，用 emoji 或英文數字（memory `feedback_no_chinese_char_corner_badge`）
- 學生測驗**選項純英文**，中文只在提示與答後解析（memory `feedback_quiz_options_english_only`）；測驗走自製 HTML + Apps Script，不用 Google Forms
- 雙語頁全 inline single-page；只列校長不列主任；每校客製不複用模板

> 各校完整脈絡（含製作方向決策 04）見 vault `組織事務/人師教育協會/跨縣市學校服務/[縣市]/[校名]/`，與 memory `project_cross_county_school_service`。
