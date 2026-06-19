# HANDOFF — taiwan-bilingual.org

兩件事：**(A) 首頁 hero 換成台灣風景美圖**、**(B) 全站每一頁的頁首都要有動感**。

- 本機 repo：`~/Documents/Claude/repos/taiwan-bilingual`（GitHub `lukelin7429/taiwan-bilingual`，apex，GitHub Pages）
- 先讀 memory：`project_taiwan_bilingual_hub`、`reference_taiwan_bilingual_motion`、`feedback_no_gimmick_tts_hero`、`feedback_web_developer_excellence`、`feedback_image_orientation`

## 現況
22 縣市頁與 `/counties/` 已深度改寫並有動效；全站動效層已建：
- `assets/css/motion.css` — hub 的 `.pg-band` 漂浮光球＋進場，已 link 進 9 個 hub 頁
- `assets/css/county.css` 的 `.cty-band` 也有動效（涵蓋 22 縣市頁）
- 首頁 `.hero` 有動效；hero 右側目前是「翡翠漸層台灣島地圖徽章」（`index.html` 的 `.hero-art > .hero-map > svg.hero-isle`，CSS 在 `main.css`）

## 鐵律（先看 feedback_no_gimmick_tts_hero）
- 主視覺要用「能代表台灣的高質感實體」：真實風景照（這次要做）或地圖徽章。**禁止用機器 TTS 唸瑣碎句子當裝飾。**
- 🔊 Web Speech 只保留在真正的學習內容（縣市頁 Say-it-in-English、WOTD、地圖 hover 唸地名），不要加到 hero 當花俏。
- 中文字型用 PingFang TC 系統字；英文美式拼法；中英並陳。
- 所有動畫都要包 `@media (prefers-reduced-motion: reduce)` 關閉。

## 任務 A：首頁 hero 台灣美景照片
1. 用免授權、可商用、免署名的圖（Pexels／Unsplash）。下載自存到 `assets/img/`（不要 hotlink）。用 **Pillow** 處理縮放/壓縮（`sips` 會留 EXIF orientation 害瀏覽器轉向，見 `feedback_image_orientation`）。選一張壯闊、能代表台灣的橫向風景（日月潭／太魯閣／合歡山雲海／台北 101 天際線／池上伯朗大道稻田／九份，擇一最美者）。

   Pexels 候選直連（自行挑最美、確認可下載；不行就再搜更多）：
   - `https://images.pexels.com/photos/924012/pexels-photo-924012.jpeg` — 山中廟宇俯瞰海
   - `https://images.pexels.com/photos/29021850/pexels-photo-29021850.jpeg` — 台北山景城市天際線夕陽
   - `https://images.pexels.com/photos/156847/pexels-photo-156847.jpeg` — 海岸步道與翠綠山丘
   - `https://images.pexels.com/photos/31227898/pexels-photo-31227898.jpeg` — 翠綠山稜遠望海平面
   - `https://images.pexels.com/photos/29781075/pexels-photo-29781075.jpeg` — 茶壺山涼亭俯瞰海岸
   - `https://images.pexels.com/photos/33474517/pexels-photo-33474517.jpeg` — 台東池上稻田與群山

   下載可加參數取較大尺寸，例：`...jpeg?auto=compress&cs=tinysrgb&w=1600`；存檔後確認是有效 JPEG。
2. 把 hero 右側改成這張照片（保留左側深色文字＋雙 CTA、進場 fade-up、背景光球）。建議：右欄一塊高、圓角、`object-fit:cover` 的照片面板（或右側滿版出血），加 **緩慢 Ken-Burns（scale 1→1.08 + 輕微位移，約 18s ease-in-out infinite）**；底部柔和漸層 scrim 放一行地點小標（例：日月潭 · Sun Moon Lake）。文字務必清晰。手機可隱藏或改為頂部小幅 banner。台灣島地圖徽章可移除或保留於別處，自行判斷。
3. 圖片壓到合理大小（hero 寬約 1400–1600px、JPEG 質量約 80、盡量 <300KB）。

## 任務 B：每頁都要動感（補齊死角）
- 稽核每一頁的頁首/hero 是否都有動效。已覆蓋：首頁、9 個 hub 頁（`.pg-band`）、22 縣市頁（`.cty-band`）。
- 待補：Partner 頁 `/edward-huang/`、`/dom-jones/`（有自己的識別配色與 CSS，band class 不同），以及任何尚未套到的頁。給它們相同等級的動效（漂浮光球 + 標題交錯進場），沿用 motion 命名風格，並包 `prefers-reduced-motion`。
- 新增的 hub 頁若用 `.pg-band`，記得在該頁 inline `</style>` 之後、`</head>` 之前補 `<link rel="stylesheet" href="/assets/css/motion.css">`。

## 驗證與交付
- 預覽用 launch.json 設定名 **tw-bilingual**（python http.server 8731 serve repo root）。
- ⚠️ 瀏覽器會快取 `main.css`/`county.css`/`motion.css`——驗證時對每個 `<link>` 加 `?v=Date.now()` 或硬重新整理，否則看不到更新。
- 每頁桌機(≥1280)＋手機(390) 都要看，確認**零 console error**、文字清晰、圖片載入正常。
- 分批 commit + push；commit 訊息用英文，結尾加：

  ```
  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
  ```
- 圖片授權：Pexels/Unsplash License（可商用免署名）即可；若改用 Wikimedia CC-BY 需在頁尾或圖說註明作者與授權。
