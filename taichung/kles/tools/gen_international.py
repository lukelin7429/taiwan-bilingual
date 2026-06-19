# -*- coding: utf-8 -*-
"""
Generate KangLang Elementary's International Education section:
  international/index.html                  (hub — newest first card grid)
  international/<slug>/index.html           (one news-style report per exchange)

Content is adapted from the school's own bilingual write-ups
(vault .../槺榔國小/國際教育/<date>/*.docx), rewritten into the News voice with
American spelling. Photos were curated + resized into each <slug>/ folder
(photo_01.jpg ...). Run from the repo root:  python3 tools/gen_international.py
"""
import os

# ------------------------------------------------------------------ DATA
# Order = newest first (this also drives prev/next + the hub grid).
DATA = [

{
 "slug":"indonesia-bang-chhun-hong", "flag":"🇮🇩",
 "tag_en":"International Exchange · Arts","tag_zh":"國際交流・藝術文化",
 "date_iso":"2026-06-09","date_en":"June 9, 2026","date_zh":"2026 年 6 月 9 日",
 "klass":"Grades 5A & 5B · 五年甲乙班","partner":"KidsStar School, South Sulawesi, Indonesia · 印尼",
 "title":"A Taiwanese Song<br>Travels to Indonesia","title_zh":"一首望春風，唱到印尼",
 "lede_en":"For our second meeting with Indonesia, we did not bring more English sentences — we brought a song. Class 5B sang the Taiwanese Hokkien classic Bang Chhun Hong, and Class 5A played it on recorders.",
 "lede_zh":"第二次與印尼連線，我們帶去的不是更多英文句子，而是一首歌。五年乙班唱起閩南語經典〈望春風〉，五年甲班用直笛伴奏。",
 "media":{"type":"slideshow","n":9,
   "cap_en":"<b>KangLang × KidsStar</b> · a music-and-dance exchange across the sea","cap_zh":"槺榔國小 × 印尼 KidsStar 學校・一場跨海的音樂與舞蹈交流"},
 "body":[
   {"h_en":"Music Across the Sea","h_zh":"跨海的音樂",
    "paras":[
     ("This was our second international exchange with KidsStar School in South Sulawesi, Indonesia. To share Taiwan's rich and varied culture, we prepared a special performance of the Hokkien classic <strong>Bang Chhun Hong</strong> (Longing for the Spring Breeze). Class 5B sang, Class 5A played the recorder, and together we introduced the song's history, its composer and lyricist, its style, and its lasting place in Taiwanese music.",
      "這是我們第二次與印尼南蘇拉威西省 KidsStar 學校交流。為了分享台灣多元豐富的文化，我們特別準備了閩南語經典〈望春風〉：五年乙班演唱、五年甲班以直笛伴奏，並向印尼師生介紹這首歌的創作背景、作詞作曲家、曲風，以及它在台灣樂壇上深遠的影響。")
    ]},
   {"h_en":"A Bridge Built of Art","h_zh":"用藝術搭起的橋",
    "paras":[
     ("In return, the Indonesian students brought wonderful dancing and singing, and introduced their own traditional dances and folk instruments. Through their lively performance, we felt the color and energy of Indonesian culture.",
      "印尼的小朋友也回贈了精彩的舞蹈與歌唱，介紹他們的傳統舞蹈與在地特色樂器。透過充滿活力的演出，我們感受到印尼藝術文化的繽紛與熱情。"),
     ("This exchange showed us that connecting with the world is about more than practicing English. Through music, dance, and performance, we crossed the language barrier, shared our cultures, and made friends — art really is one of the most beautiful bridges between people.",
      "這場交流讓我們明白，國際交流不只是英文對話。透過音樂、舞蹈與表演，我們跨越了語言的限制，分享文化、建立友誼——藝術，真是連結世界最美好的橋樑之一。")
    ]}
 ],
 "pullquote":{"en":"Art is one of the most beautiful bridges between people.","zh":"藝術是連結世界最美好的橋樑之一。"},
 "keywords":[
   {"w":"song","p":"n.","zh":"歌曲","en":"We shared a famous Taiwanese song with our friends.","z":"我們和朋友分享了一首有名的台灣歌曲。"},
   {"w":"recorder","p":"n.","zh":"直笛","en":"Class 5A played the song on the recorder.","z":"五年甲班用直笛演奏這首歌。"},
   {"w":"perform","p":"v.","zh":"表演","en":"Both schools performed for each other.","z":"兩校互相為對方表演。"},
   {"w":"traditional","p":"adj.","zh":"傳統的","en":"They showed us a traditional Indonesian dance.","z":"他們表演了一支傳統的印尼舞蹈。"},
   {"w":"culture","p":"n.","zh":"文化","en":"Music is a wonderful way to share our culture.","z":"音樂是分享文化的好方法。"},
   {"w":"instrument","p":"n.","zh":"樂器","en":"They played a special folk instrument.","z":"他們演奏了一種特別的民俗樂器。"},
   {"w":"bridge","p":"n.","zh":"橋樑","en":"Art can be a bridge between two countries.","z":"藝術可以是兩國之間的橋樑。"},
   {"w":"friendship","p":"n.","zh":"友誼","en":"Our friendship grew through music.","z":"我們的友誼因音樂而成長。"}
 ],
 "dialogue":{"scene_en":"After the recorder piece, an Indonesian student asks about the song.","scene_zh":"直笛演奏後，一位印尼學生問起這首歌。",
   "lines":[
     ("B","What is the name of your song?","你們這首歌叫什麼名字？"),
     ("A","It is called Bang Chhun Hong. It is a famous Taiwanese song.","它叫〈望春風〉，是一首有名的台灣歌曲。"),
     ("B","It sounds beautiful. Who wrote it?","好好聽。是誰寫的？"),
     ("A","A Taiwanese composer wrote it long ago.","很久以前一位台灣作曲家寫的。"),
     ("B","Now we will show you our traditional dance.","現在換我們表演傳統舞蹈給你看。"),
     ("A","Thank you! Music and dance make us good friends.","謝謝你！音樂和舞蹈讓我們成為好朋友。")
   ]}
},

{
 "slug":"russia-landmarks", "flag":"🇷🇺",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2026-06-02","date_en":"June 2, 2026","date_zh":"2026 年 6 月 2 日",
 "klass":"Grade 6 · 六年級","partner":"A partner school in Russia · 俄羅斯",
 "title":"A Tour of Russia,<br>Guided by an Older Friend","title_zh":"俄羅斯姐姐帶我們看世界",
 "lede_en":"An eighth-grade student from Russia — only two years older than us — confidently introduced her country in English: its faith and festivals, its food and clothing, and a string of breathtaking landmarks.",
 "lede_zh":"一位只比我們大兩歲的俄羅斯八年級姐姐，自信地用英文介紹她的國家——信仰與節慶、食物與服飾，還有一座座令人驚嘆的地標。",
 "media":{"type":"slideshow","n":9,
   "cap_en":"<b>A journey through Russia</b> · culture, history, and famous landmarks","cap_zh":"一趟俄羅斯之旅・文化、歷史與著名地標"},
 "body":[
   {"h_en":"Landmarks That Tell a Story","h_zh":"會說故事的地標",
    "paras":[
     ("In this exchange, an eighth grader from Russia introduced us sixth graders to her country's culture — its religion, traditional clothing, home cooking, and famous buildings. What impressed us most were the landmarks: the grand <strong>Kremlin</strong>, the towering <strong>Motherland Calls</strong> statue, the cliff-top <strong>Swallow's Nest</strong> castle, the elegant <strong>Catherine Palace</strong>, and the <strong>Main Cathedral of the Russian Armed Forces</strong>, now a museum.",
      "這次交流，由俄羅斯八年級的姐姐向我們六年級同學介紹她的國家——宗教信仰、傳統服飾、家常美食與著名建築。最令我們印象深刻的是那些地標：氣勢恢宏的<strong>克里姆林宮</strong>、高聳的<strong>「祖國呼喚」</strong>雕塑、坐落懸崖上的<strong>「燕子巢」</strong>城堡、典雅的<strong>凱薩琳宮</strong>，以及如今作為博物館的<strong>武裝部隊主教堂</strong>。"),
     ("Each building was not only beautiful to look at but full of history. Through her lively introduction, it felt as if we had set off on a journey through a faraway land.",
      "每一座建築不僅外觀驚人，更承載著豐富的歷史。在姐姐生動的介紹下，我們彷彿展開了一場異國文化與歷史之旅。")
    ]},
   {"h_en":"The Courage to Speak","h_zh":"開口的勇氣",
    "paras":[
     ("After the presentation, we eagerly asked our own questions, and she answered each one patiently. Through this two-way exchange we learned things no textbook could teach us.",
      "介紹結束後，我們踴躍提問，姐姐也一一耐心解答。透過雙向交流，我們學到了課本之外的知識。"),
     ("Most of all, we admired her courage. Only two years older, she stood in front of students far away in Taiwan and spoke with confidence. We hope that one day we too can share so bravely on an international stage.",
      "我們最佩服的，是她的勇氣。只比我們大兩歲，卻能自信從容地對遠在台灣的我們簡報。我們希望有一天，也能像她一樣，在國際舞台上勇敢分享。")
    ]}
 ],
 "pullquote":{"en":"One day, I hope to speak as bravely as she did.","zh":"希望有一天，我也能像她一樣勇敢開口。"},
 "keywords":[
   {"w":"landmark","p":"n.","zh":"地標","en":"The Kremlin is a famous landmark in Russia.","z":"克里姆林宮是俄羅斯著名的地標。"},
   {"w":"culture","p":"n.","zh":"文化","en":"She taught us about Russian culture.","z":"她教我們認識俄羅斯文化。"},
   {"w":"palace","p":"n.","zh":"宮殿","en":"Catherine Palace is elegant and grand.","z":"凱薩琳宮典雅又壯麗。"},
   {"w":"history","p":"n.","zh":"歷史","en":"Each building carries a long history.","z":"每座建築都承載著悠久的歷史。"},
   {"w":"introduce","p":"v.","zh":"介紹","en":"She introduced her country to us.","z":"她向我們介紹了她的國家。"},
   {"w":"question","p":"n.","zh":"問題","en":"We asked many questions after the talk.","z":"演講後我們問了很多問題。"},
   {"w":"confident","p":"adj.","zh":"有自信的","en":"She gave the talk in a confident voice.","z":"她用充滿自信的聲音簡報。"},
   {"w":"brave","p":"adj.","zh":"勇敢的","en":"We want to be brave and speak up too.","z":"我們也想勇敢地開口說。"}
 ],
 "dialogue":{"scene_en":"After her presentation, a KangLang student asks the Russian student a question.","scene_zh":"簡報後，一位槺榔學生向俄羅斯姐姐提問。",
   "lines":[
     ("A","Your landmarks are amazing! Which one is your favorite?","你們的地標好驚人！你最喜歡哪一個？"),
     ("B","I love the Kremlin. It is very old and grand.","我喜歡克里姆林宮，它非常古老又壯麗。"),
     ("A","How do you feel speaking English to us?","用英文跟我們說話，你覺得如何？"),
     ("B","A little nervous, but I like to try.","有點緊張，但我喜歡嘗試。"),
     ("A","You are very brave. Thank you for teaching us.","你很勇敢，謝謝你教我們。"),
     ("B","Thank you! I hope we can meet again.","謝謝你！希望我們能再見面。")
   ]}
},

{
 "slug":"india-sdgs", "flag":"🇮🇳",
 "tag_en":"International Exchange · Sustainability","tag_zh":"國際交流・永續教育",
 "date_iso":"2026-05-05","date_en":"May 5, 2026","date_zh":"2026 年 5 月 5 日",
 "klass":"Grade 6 · 六年級","partner":"Him Academy Public School, India · 印度",
 "title":"Talking About the Planet<br>with Friends in India","title_zh":"與印度學生聊聊我們的地球",
 "lede_en":"Reduce, reuse, recycle. Our sixth graders met students from Him Academy in India to share how each country looks after the Earth, built around the United Nations Sustainable Development Goals.",
 "lede_zh":"減量、再利用、回收。六年級的孩子與印度 Him Academy 的學生連線，圍繞聯合國永續發展目標，分享兩國如何照顧我們的地球。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>KangLang × Him Academy</b> · an exchange on the UN Sustainable Development Goals","cap_zh":"槺榔國小 × 印度 Him Academy・聯合國永續發展目標（SDGs）交流"},
 "body":[
   {"h_en":"Two Goals, Two Countries","h_zh":"兩個目標，兩個國家",
    "paras":[
     ("Our sixth graders held an international exchange with students from <strong>Him Academy Public School</strong> in India, built around the United Nations <strong>Sustainable Development Goals</strong>. The focus was on <strong>SDG 12</strong>, responsible consumption and production, and <strong>SDG 13</strong>, climate action — with the &ldquo;three Rs&rdquo; at its heart: reduce, reuse, recycle.",
      "六年級學生與印度 Him Academy Public School 進行了一場結合聯合國<strong>永續發展目標（SDGs）</strong>的交流，聚焦 <strong>SDG 12</strong>「負責任的消費與生產」與 <strong>SDG 13</strong>「氣候行動」，核心是「三 R」——減量、再利用、回收。"),
     ("In groups, our students presented Taiwan's recycling system and showed how everyday objects can be reused — even turning plastic bottles, paper, and cardboard into useful tools and creative toys. The Indian students gave individual reports on how the three Rs work in their own community.",
      "我們分組簡報，介紹台灣完善的資源回收制度，示範如何重複使用物品，甚至把寶特瓶、紙張與紙板做成實用工具或創意玩具。印度學生則以個人報告，分享他們在當地實踐三 R 的做法。")
    ]},
   {"h_en":"A Real Reason to Speak English","h_zh":"練好英文的真實理由",
    "paras":[
     ("Throughout the reports our students did their very best in English, while the Indian students spoke wonderfully fluently. The exchange widened everyone's view of the world.",
      "報告過程中，我們努力以英文呈現最佳表現，印度學生則展現出流利的英語能力。這次交流也拓展了大家的國際視野。"),
     ("More than that, it gave our students a real reason to keep improving — so that one day they can connect with the world even more confidently.",
      "更重要的是，它讓孩子有了持續進步的真實動機——期許未來能更自信、流暢地與世界接軌。")
    ]}
 ],
 "pullquote":{"en":"We are different countries, but we both love the planet.","zh":"我們是不同的國家，但我們都愛這個星球。"},
 "keywords":[
   {"w":"planet","p":"n.","zh":"星球（地球）","en":"We all live on the same planet.","z":"我們都住在同一個星球上。"},
   {"w":"reduce","p":"v.","zh":"減少","en":"We try to reduce the trash we make.","z":"我們試著減少製造的垃圾。"},
   {"w":"reuse","p":"v.","zh":"再利用","en":"We reuse plastic bottles to make toys.","z":"我們把寶特瓶再利用，做成玩具。"},
   {"w":"recycle","p":"v.","zh":"回收","en":"Please recycle your paper and cans.","z":"請回收你的紙張和罐子。"},
   {"w":"waste","p":"n.","zh":"廢棄物、垃圾","en":"Reusing things helps cut down waste.","z":"重複使用東西能減少垃圾。"},
   {"w":"climate","p":"n.","zh":"氣候","en":"Climate action protects our future.","z":"氣候行動保護我們的未來。"},
   {"w":"responsible","p":"adj.","zh":"負責任的","en":"Being responsible means we do not waste things.","z":"負責任表示我們不浪費東西。"},
   {"w":"connect","p":"v.","zh":"連結、交流","en":"English helps us connect with the world.","z":"英語幫助我們和世界交流。"}
 ],
 "dialogue":{"scene_en":"During the video call, a student from India asks about recycling in Taiwan.","scene_zh":"視訊交流時，一位印度學生問起台灣的回收。",
   "lines":[
     ("B","Hello! How do you recycle in Taiwan?","哈囉！你們在台灣怎麼回收？"),
     ("A","We sort our trash into paper, plastic, and cans.","我們把垃圾分成紙、塑膠和罐子。"),
     ("B","That is great. Do you reuse things too?","太棒了。你們也會再利用東西嗎？"),
     ("A","Yes! We make toys from plastic bottles.","會！我們用寶特瓶做玩具。"),
     ("B","We do the three Rs in India too.","我們在印度也做三 R。"),
     ("A","We are different countries, but we both love the planet.","我們是不同的國家，但我們都愛這個星球。")
   ]}
},

{
 "slug":"vietnam-landmarks", "flag":"🇻🇳",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2026-04-28","date_en":"April 28, 2026","date_zh":"2026 年 4 月 28 日",
 "klass":"Grade 5 · 五年級","partner":"Vinschool, Vietnam · 越南",
 "title":"Traveling Between<br>Taiwan and Vietnam","title_zh":"在台灣與越南之間旅行",
 "lede_en":"Without boarding a single plane, our fifth graders &ldquo;visited&rdquo; both countries through a screen — sharing Taiwan's most beautiful places and discovering Vietnam's famous sights in return.",
 "lede_zh":"沒搭上任何一班飛機，五年級的孩子透過螢幕「走訪」了兩個國家——分享台灣最美的地方，也認識越南的著名景點。",
 "media":{"type":"slideshow","n":9,
   "cap_en":"<b>KangLang × Vinschool</b> · a tour of Taiwan and Vietnam, screen to screen","cap_zh":"槺榔國小 × 越南 Vinschool・隔著螢幕，一場台越之旅"},
 "body":[
   {"h_en":"Showing Off the Island We Love","h_zh":"介紹我們深愛的島嶼",
    "paras":[
     ("This was our fifth graders' second international exchange, and after their first time they were noticeably calmer and more confident. Connecting online with <strong>Vinschool</strong> in Vietnam, the classroom suddenly reached across a border.",
      "這是五年級的第二次國際交流。有了第一次的經驗，大家明顯多了一份從容與自信。與越南 <strong>Vinschool</strong> 線上連線，教室瞬間跨越了國界。"),
     ("In groups, our students introduced Taiwan's famous spots — sunny <strong>Kenting</strong>, picture-perfect <strong>Sun Moon Lake</strong>, the old streets of <strong>Lukang</strong>, and the mountain town of <strong>Jiufen</strong>. One group proudly introduced our own hometown, <strong>Qingshui</strong>.",
      "我們分組介紹台灣的特色景點——陽光熱情的<strong>墾丁</strong>、風景如畫的<strong>日月潭</strong>、古色古香的<strong>鹿港</strong>、山城風情的<strong>九份</strong>，還有一組驕傲地介紹我們的家鄉<strong>清水</strong>。")
    ]},
   {"h_en":"A Window Onto Vietnam","h_zh":"望向越南的一扇窗",
    "paras":[
     ("In return, the Vietnamese students introduced their own famous sights: the spectacular <strong>Dragon Bridge</strong>, the dreamy <strong>Ba Na Hills</strong>, the much-photographed <strong>Golden Bridge</strong>, and the natural beauty of the <strong>Marble Mountains</strong>.",
      "越南的小朋友也介紹了他們的著名景點：壯觀的<strong>龍橋（Dragon Bridge）</strong>、夢幻的<strong>巴拿山（Ba Na Hills）</strong>、吸引無數遊客的<strong>金橋（Golden Bridge）</strong>，以及自然景觀豐富的<strong>五行山（Marble Mountains）</strong>。"),
     ("Through each other's sharing, the children opened a window onto a different country. Even without leaving the classroom, they took a memorable trip across two lands.",
      "透過彼此的分享，孩子們打開了一扇望向不同國家的窗。即使沒離開教室，也走了一場難忘的雙國之旅。")
    ]}
 ],
 "pullquote":{"en":"We traveled to two countries without leaving the classroom.","zh":"我們沒離開教室，就旅行了兩個國家。"},
 "keywords":[
   {"w":"travel","p":"v.","zh":"旅行","en":"We can travel through a screen.","z":"我們可以透過螢幕去旅行。"},
   {"w":"famous","p":"adj.","zh":"著名的","en":"Sun Moon Lake is a famous place in Taiwan.","z":"日月潭是台灣著名的地方。"},
   {"w":"hometown","p":"n.","zh":"家鄉","en":"Our hometown is Qingshui.","z":"我們的家鄉是清水。"},
   {"w":"bridge","p":"n.","zh":"橋","en":"The Golden Bridge in Vietnam is amazing.","z":"越南的金橋很驚人。"},
   {"w":"introduce","p":"v.","zh":"介紹","en":"Each group introduced a beautiful place.","z":"每一組介紹一個美麗的地方。"},
   {"w":"mountain","p":"n.","zh":"山","en":"The Marble Mountains have caves to explore.","z":"五行山裡有可以探索的洞穴。"},
   {"w":"scenery","p":"n.","zh":"風景","en":"The scenery in both countries is beautiful.","z":"兩個國家的風景都很美。"},
   {"w":"confident","p":"adj.","zh":"有自信的","en":"This time we felt more confident.","z":"這次我們更有自信了。"}
 ],
 "dialogue":{"scene_en":"Two students compare their favorite places.","scene_zh":"兩位學生比較彼此最喜歡的地方。",
   "lines":[
     ("A","Welcome! Let me show you Sun Moon Lake.","歡迎！讓我介紹日月潭給你。"),
     ("B","It looks beautiful! We have the Dragon Bridge.","好美！我們有龍橋。"),
     ("A","A dragon bridge? That sounds amazing.","龍橋？聽起來好酷。"),
     ("B","Yes, it breathes fire on weekends!","對，週末它還會噴火！"),
     ("A","Wow! I want to visit Vietnam one day.","哇！我有一天想去越南。"),
     ("B","And I want to visit Taiwan. Let us be friends.","我也想去台灣。我們當朋友吧。")
   ]}
},

{
 "slug":"indonesia-first-exchange", "flag":"🇮🇩",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2026-03-31","date_en":"March 31, 2026","date_zh":"2026 年 3 月 31 日",
 "klass":"Grade 5 · 五年級","partner":"KidsStar School, South Sulawesi, Indonesia · 印尼",
 "title":"Our First International<br>Exchange","title_zh":"我們的第一次國際交流",
 "lede_en":"Thirty seconds in front of the camera, in English, with new friends in Indonesia watching. Excited and a little nervous — and braver by the end.",
 "lede_zh":"面對鏡頭、用英文、三十秒——印尼的新朋友正看著。既期待又有點緊張，但到最後，變得更勇敢了。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>KangLang × KidsStar</b> · our fifth graders' very first international exchange","cap_zh":"槺榔國小 × 印尼 KidsStar 學校・五年級的第一次國際交流"},
 "body":[
   {"h_en":"Thirty Brave Seconds","h_zh":"勇敢的三十秒",
    "paras":[
     ("Our fifth graders had their very first international exchange today — excited and a little nervous all at once. Through an online call, they connected with <strong>KidsStar School</strong> in South Sulawesi, Indonesia. One by one, every student stepped up to the camera and introduced themselves in English for about thirty seconds.",
      "五年級的小朋友今天迎來第一次國際交流，既期待又有點緊張。我們透過線上連線，與印尼南蘇拉威西省的 <strong>KidsStar 學校</strong>交流。每位同學都要上台，面對鏡頭用英文進行約三十秒的自我介紹。"),
     ("Short as it was, those thirty seconds took a lot of practice. The children rehearsed again and again to get their pronunciation and their lines just right, and their teachers praised how quickly they improved.",
      "短短三十秒，背後是反覆的練習。孩子們一次又一次地練，把發音和內容做到最好，老師們也讚賞大家進步神速。")
    ]},
   {"h_en":"Dreams on the Other Side of the Screen","h_zh":"螢幕另一端的夢想",
    "paras":[
     ("Then we listened to the Indonesian students share their dreams — one wanted to be a soccer player, another an astronaut, another a doctor. They seemed so natural and relaxed in front of the camera.",
      "接著我們專心聆聽印尼小朋友的自我介紹。他們分享了各自的夢想：有人想當足球員、有人想當太空人或醫生，而且在鏡頭前顯得自然又大方。"),
     ("We were shy at first, but slowly we relaxed and grew braver. Meeting friends our own age on the other side of the world, we saw both how alike and how different we are — and we cannot wait for the next exchange.",
      "我們一開始有些害羞，但慢慢放鬆、變得更勇敢。認識了遠在世界另一端、和我們同年紀的朋友，我們看見了彼此的相同與不同，也更加期待下一次的交流。")
    ]}
 ],
 "pullquote":{"en":"We were shy at first — but braver by the end.","zh":"我們一開始害羞，到最後卻更勇敢了。"},
 "keywords":[
   {"w":"introduce","p":"v.","zh":"介紹（自己）","en":"I will introduce myself in English.","z":"我要用英文介紹自己。"},
   {"w":"camera","p":"n.","zh":"鏡頭、相機","en":"We spoke in front of the camera.","z":"我們在鏡頭前說話。"},
   {"w":"nervous","p":"adj.","zh":"緊張的","en":"I felt nervous before my turn.","z":"輪到我之前，我覺得緊張。"},
   {"w":"practice","p":"v.","zh":"練習","en":"We practiced our lines many times.","z":"我們把台詞練習了很多次。"},
   {"w":"dream","p":"n.","zh":"夢想","en":"My dream is to be a doctor.","z":"我的夢想是當醫生。"},
   {"w":"brave","p":"adj.","zh":"勇敢的","en":"By the end, we felt brave.","z":"到最後，我們覺得很勇敢。"},
   {"w":"exchange","p":"n.","zh":"交流","en":"This was our first exchange.","z":"這是我們的第一次交流。"},
   {"w":"friend","p":"n.","zh":"朋友","en":"We made new friends in Indonesia.","z":"我們在印尼交了新朋友。"}
 ],
 "dialogue":{"scene_en":"Two fifth graders meet for the first time and share their dreams.","scene_zh":"兩位五年級學生第一次見面，分享彼此的夢想。",
   "lines":[
     ("A","Hello! My name is Mei. Nice to meet you.","哈囉！我叫小美，很高興認識你。"),
     ("B","Hi Mei! I am Budi. Where are you from?","嗨小美！我是 Budi。你來自哪裡？"),
     ("A","I am from Taiwan. What is your dream?","我來自台灣。你的夢想是什麼？"),
     ("B","I want to be a soccer player. And you?","我想當足球員。你呢？"),
     ("A","I want to be a doctor and help people.","我想當醫生，幫助別人。"),
     ("B","That is a great dream. Let us be friends!","那是很棒的夢想。我們當朋友吧！")
   ]}
},

{
 "slug":"israel-graduation-video", "flag":"🇮🇱",
 "tag_en":"Video Exchange","tag_zh":"影片交流",
 "date_iso":"2025-05-30","date_en":"May 30, 2025","date_zh":"2025 年 5 月 30 日",
 "klass":"Grade 6 · 六年級","partner":"Sister school in Israel · 以色列",
 "title":"A Graduation Trip,<br>Sung Across the World","title_zh":"用一首歌，把畢業旅行寄到以色列",
 "lede_en":"In the second year of our Sister School Program, our sixth graders filmed their graduation trip and set it to a song they had practiced for almost a whole year — then sent it all the way to Israel.",
 "lede_zh":"姐妹校計畫邁入第二年，六年級的孩子把畢業旅行拍成影片，配上練了將近一年的歌，寄到了遙遠的以色列。",
 "media":{"type":"video","yt":"nZ3DfmRgVLM",
   "cap_en":"<b>Children of the World</b> · an English song woven with two Taiwanese Hokkien folk songs, Tiam-a-ka and Se-pak-hoo","cap_zh":"〈Children of the World〉・一首英文歌與兩首閩南語歌謠〈點仔膠〉〈西北雨〉的組曲"},
 "body":[
   {"h_en":"Beating the Time Zones","h_zh":"克服時差的方法",
    "paras":[
     ("KangLang's <strong>Ministry of Education Sister School Program</strong> has reached its second year. Alongside many live video calls, our sixth graders made a student-centered film about their <strong>graduation trip</strong> to share with a partner school in Israel. A film like this lets us share our school life and, at the same time, slip past the problem of time-zone differences.",
      "槺榔國小執行教育部<strong>姐妹校計畫</strong>已邁入第二年。除了多場線上交流，六年級的孩子以<strong>畢業旅行</strong>為主題，錄製了一支以學生為主角的影片，分享給以色列的學校。這樣的影片不只能分享校園生活，也巧妙地化解了國際交流的時差問題。")
    ]},
   {"h_en":"A Song Worth a Whole Year","h_zh":"練了一整年的一首歌",
    "paras":[
     ("The music deserves a special mention. For nearly a whole year, our fifth and sixth graders practiced the soundtrack — learning the English lyrics word by word and rehearsing line by line.",
      "影片的配樂特別值得一提。為了這首歌，槺榔五、六年級的孩子練習了將近一整年，從英文歌詞逐字學起，一句一句反覆練唱。"),
     ("The result is a medley that weaves the English song <strong>Children of the World</strong> together with two beloved Taiwanese Hokkien folk songs, <em>Tiam-a-ka</em> and <em>Se-pak-hoo</em>. Press play and listen along.",
      "成果是一首組曲，把英文歌〈<strong>Children of the World</strong>〉與兩首動人的閩南語歌謠〈點仔膠〉〈西北雨〉交織在一起。按下播放，一起聆聽吧。")
    ]}
 ],
 "pullquote":{"en":"They learned the lyrics word by word, for almost a whole year.","zh":"他們把歌詞一字一字學起，練了將近一整年。"},
 "keywords":[
   {"w":"graduation","p":"n.","zh":"畢業","en":"We filmed our graduation trip.","z":"我們拍下了畢業旅行。"},
   {"w":"video","p":"n.","zh":"影片","en":"We sent a video to our friends in Israel.","z":"我們寄了一支影片給以色列的朋友。"},
   {"w":"lyrics","p":"n.","zh":"歌詞","en":"We learned the English lyrics by heart.","z":"我們把英文歌詞記在心裡。"},
   {"w":"practice","p":"v.","zh":"練習","en":"We practiced the song for almost a year.","z":"這首歌我們練了將近一年。"},
   {"w":"folk song","p":"n.","zh":"民謠","en":"We added two Taiwanese folk songs.","z":"我們加入了兩首台灣民謠。"},
   {"w":"share","p":"v.","zh":"分享","en":"We share our school life on film.","z":"我們用影片分享校園生活。"},
   {"w":"medley","p":"n.","zh":"組曲","en":"The medley mixes three songs together.","z":"這首組曲把三首歌結合在一起。"},
   {"w":"world","p":"n.","zh":"世界","en":"Children of the world can be friends.","z":"世界的孩子都能成為朋友。"}
 ],
 "dialogue":{"scene_en":"A KangLang student tells an Israeli friend about the video.","scene_zh":"一位槺榔學生向以色列朋友介紹這支影片。",
   "lines":[
     ("A","We made a video of our graduation trip for you.","我們為你做了一支畢業旅行的影片。"),
     ("B","Thank you! What is the song?","謝謝你！這首歌是什麼？"),
     ("A","It is called Children of the World.","它叫〈Children of the World〉。"),
     ("B","Did you sing it in English?","你們用英文唱嗎？"),
     ("A","Yes, and we added two Taiwanese folk songs too.","對，我們還加了兩首台灣民謠。"),
     ("B","That is wonderful. I will watch it now!","太棒了，我現在就來看！")
   ]}
},

{
 "slug":"israel-endangered-animals", "flag":"🇮🇱",
 "tag_en":"International Exchange · Ecology","tag_zh":"國際交流・生態保育",
 "date_iso":"2025-05-26","date_en":"May 26, 2025","date_zh":"2025 年 5 月 26 日",
 "klass":"Class 602 · 六年乙班","partner":"A partner school in Israel · 以色列",
 "title":"Saving Animals,<br>a Shared Job for the World","title_zh":"保護動物，是全世界的事",
 "lede_en":"On the theme of endangered animals, Class 602 introduced Israel to Taiwan's rare wildlife — and learned, in return, about animals they had never heard of before.",
 "lede_zh":"以「瀕臨絕種的動物」為主題，六年乙班向以色列介紹台灣珍稀的野生動物，也認識了一群從沒聽過的動物。",
 "media":{"type":"slideshow","n":6,
   "cap_en":"<b>Endangered Animals</b> · a conservation exchange between Taiwan and Israel","cap_zh":"瀕臨絕種的動物・一場台灣與以色列的保育交流"},
 "body":[
   {"h_en":"Taiwan's Precious Few","h_zh":"台灣珍貴的牠們",
    "paras":[
     ("Today was a special day for Class 602. In an online exchange with a school in Israel on the theme of <strong>endangered animals</strong>, we introduced some of Taiwan's rarest creatures: the <strong>Formosan black bear</strong>, the <strong>grass owl</strong>, the <strong>leopard cat</strong>, and the <strong>Taiwan pangolin</strong>. Using simple English and pictures, we explained what they look like, where they live, and why they are in danger.",
      "今天是六年乙班特別的一天。我們與以色列學校以<strong>瀕臨絕種的動物</strong>為主題進行線上交流，向他們介紹台灣珍稀的動物：<strong>台灣黑熊</strong>、<strong>草鴞</strong>、<strong>石虎</strong>與<strong>台灣穿山甲</strong>。我們用簡單的英文和圖片，介紹牠們的特徵、棲地，以及面臨滅絕的原因。")
    ]},
   {"h_en":"Animals We Had Never Met","h_zh":"從沒見過的動物",
    "paras":[
     ("The Israeli students were just as well prepared. They introduced endangered animals from their own country — the <strong>striped hyena</strong>, the <strong>lesser kestrel</strong>, the <strong>griffon vulture</strong>, the <strong>Arabian oryx</strong>, and the <strong>sea turtle</strong>. Many of these were completely new to us, and they sparked our curiosity about the natural world.",
      "以色列的小朋友也準備得非常用心，介紹了他們國家正在保育的動物：<strong>條紋鬣狗</strong>、<strong>小紅隼</strong>、<strong>禿鷲</strong>、<strong>阿拉伯羚羊</strong>與<strong>海龜</strong>。許多動物我們從沒聽過，覺得很新奇，也激發了我們對自然生態的好奇。"),
     ("Beyond the new English words, we learned something bigger: protecting endangered animals is a responsibility we all share, everywhere in the world.",
      "除了學到許多新單字，我們也明白了一件更重要的事：保育動物，是全世界共同的責任。")
    ]}
 ],
 "pullquote":{"en":"Protecting endangered animals is a job we all share.","zh":"保護瀕危動物，是我們共同的責任。"},
 "keywords":[
   {"w":"endangered","p":"adj.","zh":"瀕臨絕種的","en":"The leopard cat is an endangered animal.","z":"石虎是瀕臨絕種的動物。"},
   {"w":"animal","p":"n.","zh":"動物","en":"We introduced four rare animals.","z":"我們介紹了四種珍稀動物。"},
   {"w":"protect","p":"v.","zh":"保護","en":"We must protect these animals.","z":"我們必須保護這些動物。"},
   {"w":"habitat","p":"n.","zh":"棲息地","en":"This bird is losing its habitat.","z":"這種鳥正在失去牠的棲息地。"},
   {"w":"bear","p":"n.","zh":"熊","en":"The Formosan black bear lives in the mountains.","z":"台灣黑熊住在山裡。"},
   {"w":"turtle","p":"n.","zh":"海龜","en":"The sea turtle needs a clean ocean.","z":"海龜需要乾淨的海洋。"},
   {"w":"nature","p":"n.","zh":"大自然","en":"We care about nature and wildlife.","z":"我們關心大自然與野生動物。"},
   {"w":"responsibility","p":"n.","zh":"責任","en":"Caring for animals is everyone's responsibility.","z":"照顧動物是每個人的責任。"}
 ],
 "dialogue":{"scene_en":"Two students compare the endangered animals of their countries.","scene_zh":"兩位學生比較各自國家的瀕危動物。",
   "lines":[
     ("A","In Taiwan, we protect the Formosan black bear.","在台灣，我們保護台灣黑熊。"),
     ("B","In Israel, we protect the Arabian oryx.","在以色列，我們保護阿拉伯羚羊。"),
     ("A","I have never heard of that animal!","我從來沒聽過那種動物！"),
     ("B","It is a beautiful desert animal. Why is your bear in danger?","牠是美麗的沙漠動物。你們的熊為什麼瀕危？"),
     ("A","It is losing its habitat in the mountains.","牠在山裡的棲息地正在消失。"),
     ("B","We must protect them. It is our shared job.","我們得保護牠們，這是我們共同的責任。")
   ]}
},

{
 "slug":"india-song-videos", "flag":"🇮🇳",
 "tag_en":"Video Exchange","tag_zh":"影片交流",
 "date_iso":"2025-05-14","date_en":"May 14, 2025","date_zh":"2025 年 5 月 14 日",
 "klass":"Grades 5–6 · 五、六年級","partner":"Sister school in India · 印度",
 "title":"Sports Day and a Country Walk,<br>Filmed for India","title_zh":"把運動會與鄉野踏查，拍給印度看",
 "lede_en":"In year two of our Sister School Program, our fifth graders turned their sports day and a local field trip into films for India — carried along by a song they had practiced for almost a year.",
 "lede_zh":"姐妹校計畫第二年，五年級的孩子把運動會與鄉野踏查拍成影片寄給印度，背景音樂是練了將近一年的一首歌。",
 "media":{"type":"video","yt":"DX1tXjF8k-w",
   "cap_en":"<b>Children of the World</b> · woven with the Taiwanese Hokkien folk songs Tiam-a-ka and Se-pak-hoo","cap_zh":"〈Children of the World〉・與閩南語歌謠〈點仔膠〉〈西北雨〉交織而成的組曲"},
 "body":[
   {"h_en":"School Life on Film","h_zh":"用影片記錄校園生活",
    "paras":[
     ("KangLang's <strong>Ministry of Education Sister School Program</strong> entered its second year. Beyond live video calls, our fifth graders made two themed films — one about our <strong>sports day</strong>, one about a <strong>local field walk</strong> — to share with our partner school in India. Filming this way lets us show our daily school life while getting past the obstacle of time-zone differences.",
      "槺榔國小執行教育部<strong>姐妹校計畫</strong>邁入第二年。除了多場線上交流，五年級的孩子以<strong>運動會</strong>與<strong>鄉野踏查</strong>為主題，錄製了兩支影片分享給印度的學校。以影片呈現，既能分享校園生活的點滴，也消弭了國際交流的時差限制。")
    ]},
   {"h_en":"A Year of Singing Practice","h_zh":"練唱一整年",
    "paras":[
     ("The soundtrack is worth a special mention: our fifth and sixth graders practiced it for almost a whole year, learning the English lyrics word by word and rehearsing line by line.",
      "影片的配樂特別值得一提：五、六年級的孩子練習了將近一整年，從英文歌詞逐字學起，一句句反覆練唱，著實費了不少心力。"),
     ("Listen to the medley that joins the English song <strong>Children of the World</strong> with two local Hokkien folk songs, <em>Tiam-a-ka</em> and <em>Se-pak-hoo</em>.",
      "歡迎一起聆聽這首組曲——英文歌〈<strong>Children of the World</strong>〉結合兩首在地閩南語歌謠〈點仔膠〉與〈西北雨〉。")
    ]}
 ],
 "pullquote":{"en":"A film can leap across any time zone.","zh":"一支影片，可以跨越任何時差。"},
 "keywords":[
   {"w":"video","p":"n.","zh":"影片","en":"We made two videos for India.","z":"我們為印度做了兩支影片。"},
   {"w":"sports day","p":"n.","zh":"運動會","en":"Our sports day is full of energy.","z":"我們的運動會充滿活力。"},
   {"w":"field trip","p":"n.","zh":"戶外踏查","en":"We went on a field trip near our school.","z":"我們在學校附近進行戶外踏查。"},
   {"w":"lyrics","p":"n.","zh":"歌詞","en":"We learned the lyrics word by word.","z":"我們逐字學會了歌詞。"},
   {"w":"practice","p":"v.","zh":"練習","en":"We practiced singing all year.","z":"我們練唱了一整年。"},
   {"w":"share","p":"v.","zh":"分享","en":"We share our school life on film.","z":"我們用影片分享校園生活。"},
   {"w":"time zone","p":"n.","zh":"時區","en":"A video helps us beat the time zone.","z":"影片幫我們克服時差。"},
   {"w":"folk song","p":"n.","zh":"民謠","en":"We sang two Taiwanese folk songs.","z":"我們唱了兩首台灣民謠。"}
 ],
 "dialogue":{"scene_en":"A KangLang student introduces the film to a friend in India.","scene_zh":"一位槺榔學生向印度朋友介紹這支影片。",
   "lines":[
     ("A","We filmed our sports day for you to see.","我們把運動會拍下來給你看。"),
     ("B","Great! What music did you use?","太好了！你們用什麼音樂？"),
     ("A","A song called Children of the World.","一首叫〈Children of the World〉的歌。"),
     ("B","Did it take long to learn?","學了很久嗎？"),
     ("A","Almost a whole year of practice!","練了將近一整年！"),
     ("B","Wow. I will watch your video right now.","哇，我現在就來看你們的影片。")
   ]}
},

{
 "slug":"india-street-food-5b", "flag":"🇮🇳",
 "tag_en":"International Exchange · Culture","tag_zh":"國際交流・文化",
 "date_iso":"2025-05-08","date_en":"May 8, 2025","date_zh":"2025 年 5 月 8 日",
 "klass":"Class 5B · 五年乙班","partner":"A partner school in India · 印度",
 "title":"Street Food, Games,<br>and a Festival of Color","title_zh":"街頭小吃、遊戲，與繽紛的節慶",
 "lede_en":"In their second exchange with India, Class 5B feasted their eyes on Indian street food, learned brand-new games, and met the color and light of Holi — then danced their hearts out in return.",
 "lede_zh":"與印度的第二次交流，五年乙班看遍印度街頭小吃、學了全新的遊戲、認識了光與色彩的荷麗節——也回敬了一場賣力的熱舞。",
 "media":{"type":"slideshow","n":7,
   "cap_en":"<b>Class 5B × India</b> · street food, games, and the colors of Holi","cap_zh":"五年乙班 × 印度・街頭小吃、傳統遊戲與荷麗節的色彩"},
 "body":[
   {"h_en":"A Table Full of New Words","h_zh":"一桌子的新單字",
    "paras":[
     ("For their second online exchange with a school in India, our fifth graders were buzzing with excitement. The Indian students introduced a whole table of local street foods — <strong>aloo tikki</strong>, <strong>kachori</strong>, <strong>bhelpuri</strong>, <strong>samosa</strong>, and <strong>gol gappa</strong> — and every one of them sounded delicious.",
      "與印度學校的第二次線上交流，五年級的孩子興奮極了。印度學生介紹了一整桌的街頭小吃——<strong>aloo tikki</strong>、<strong>kachori</strong>、<strong>bhelpuri</strong>、<strong>samosa</strong> 和 <strong>gol gappa</strong>，每一道聽起來都令人垂涎。"),
     ("We also learned their favorite traditional games, including <strong>kho kho</strong>, <strong>gilli danda</strong>, <strong>kabaddi</strong>, and <strong>top</strong> — all new and full of fun.",
      "我們還學到他們喜愛的傳統遊戲，包括 <strong>kho kho</strong>、<strong>gilli danda</strong>、<strong>kabaddi</strong> 和 <strong>top</strong>，每一種都新奇有趣。")
    ]},
   {"h_en":"Color, Light, and a Dance","h_zh":"色彩、燈火，與一支舞",
    "paras":[
     ("Then came their festivals: the colorful <strong>Holi</strong> with its clouds of bright powder, the delicate hand art of <strong>mehndi</strong>, the little <strong>diya</strong> oil lamps, and <strong>rangoli</strong> patterns drawn from rice flour and colored sand. Even their banknotes were full of local character.",
      "接著是他們的節慶：用彩粉慶祝、繽紛熱鬧的<strong>荷麗節（Holi）</strong>、畫在手上的<strong>指甲花彩繪（mehndi）</strong>、節慶用的<strong>油燈（diya）</strong>，以及用米粉與彩沙創作的<strong>地畫（rangoli）</strong>。連他們的貨幣設計都充滿地方特色。"),
     ("The happiest moment was our own dance. As our classmates danced their hearts out, the Indian students laughed and smiled on the other side of the screen — and we felt proud and joyful all at once.",
      "最開心的，是我們準備的熱舞。當同學賣力跳舞時，螢幕另一頭的印度同學笑得好開心，讓我們既驕傲又快樂。")
    ]}
 ],
 "pullquote":{"en":"As we danced, our new friends laughed and clapped along.","zh":"我們跳舞時，新朋友在螢幕那頭笑著鼓掌。"},
 "keywords":[
   {"w":"festival","p":"n.","zh":"節慶","en":"Holi is a colorful festival in India.","z":"荷麗節是印度繽紛的節慶。"},
   {"w":"street food","p":"n.","zh":"街頭小吃","en":"Samosa is a popular street food.","z":"咖哩角是受歡迎的街頭小吃。"},
   {"w":"game","p":"n.","zh":"遊戲","en":"Kabaddi is a fun team game.","z":"卡巴迪是有趣的團隊遊戲。"},
   {"w":"color","p":"n.","zh":"顏色","en":"People throw bright colors at Holi.","z":"人們在荷麗節灑出鮮豔的色彩。"},
   {"w":"lamp","p":"n.","zh":"燈","en":"A diya is a small oil lamp.","z":"diya 是一種小油燈。"},
   {"w":"dance","p":"v.","zh":"跳舞","en":"We danced for our Indian friends.","z":"我們為印度朋友跳舞。"},
   {"w":"taste","p":"v.","zh":"品嚐","en":"I want to taste Indian street food.","z":"我想嚐嚐印度街頭小吃。"},
   {"w":"proud","p":"adj.","zh":"驕傲的","en":"We felt proud of our performance.","z":"我們對自己的表演感到驕傲。"}
 ],
 "dialogue":{"scene_en":"Two students swap their favorite foods and games.","scene_zh":"兩位學生交換彼此最愛的食物和遊戲。",
   "lines":[
     ("B","Have you ever tried samosa?","你吃過咖哩角嗎？"),
     ("A","No, but it sounds delicious! What is it?","沒有，但聽起來好好吃！那是什麼？"),
     ("B","It is a crispy snack with potato inside.","是一種裡面包馬鈴薯的酥脆點心。"),
     ("A","Yum! We want to show you a Taiwanese dance.","好想吃！我們想表演一支台灣舞蹈給你看。"),
     ("B","Please do! We love to watch you dance.","快表演！我們最愛看你們跳舞了。"),
     ("A","Here we go — one, two, three!","來囉——一、二、三！")
   ]}
},

{
 "slug":"india-culture-5a", "flag":"🇮🇳",
 "tag_en":"International Exchange · Culture","tag_zh":"國際交流・文化",
 "date_iso":"2025-05-05","date_en":"May 5, 2025","date_zh":"2025 年 5 月 5 日",
 "klass":"Class 5A · 五年甲班","partner":"ASN Senior Secondary School, India · 印度",
 "title":"Five Groups,<br>Two Cultures","title_zh":"五個小組，兩種文化",
 "lede_en":"Split into five groups, Class 5A introduced Taiwan piece by piece — and watched, spellbound, as an Indian girl in traditional dress performed a graceful dance.",
 "lede_zh":"分成五組，五年甲班一塊一塊地介紹台灣——也看得入迷：一位身著傳統服飾的印度小女孩，跳起了優雅的舞。",
 "media":{"type":"slideshow","n":7,
   "cap_en":"<b>Class 5A × ASN Senior Secondary School</b> · a second cultural exchange with India","cap_zh":"五年甲班 × 印度 ASN Senior Secondary School・第二次文化交流"},
 "body":[
   {"h_en":"Taiwan, in Five Parts","h_zh":"五個部分的台灣",
    "paras":[
     ("Class 5A held their second online cultural exchange with <strong>ASN Senior Secondary School</strong> in India. We split the class into five groups, each one introducing a different slice of Taiwan: our <strong>snacks</strong>, our <strong>toys</strong>, our <strong>cultural objects</strong>, our <strong>currency</strong>, and our <strong>festivals</strong>.",
      "五年甲班與印度 <strong>ASN Senior Secondary School</strong> 進行第二次線上文化交流。我們把全班分成五組，分別介紹台灣的<strong>零食</strong>、<strong>玩具</strong>、<strong>文物</strong>、<strong>貨幣</strong>與<strong>節慶</strong>。")
    ]},
   {"h_en":"A Dance We Will Remember","h_zh":"難忘的一支舞",
    "paras":[
     ("In return, the Indian students shared their <strong>five stones game</strong>, the famous <strong>blue pottery of Jaipur</strong>, and street foods like <strong>aloo chaat</strong> and <strong>kachori</strong>.",
      "印度同學則分享了他們的<strong>五顆石頭遊戲</strong>、著名的<strong>齋浦爾藍陶</strong>，以及 <strong>aloo chaat</strong>、<strong>kachori</strong> 等街頭小吃。"),
     ("The most memorable moment came when an Indian girl, dressed in traditional clothing, performed a graceful dance — a beautiful glimpse of her country's culture. The exchange deepened our understanding of India and gave us the chance to share Taiwan with friends far away.",
      "最難忘的一刻，是一位身穿傳統服飾的印度小女孩，優雅地表演了一支舞，展現濃厚的民族風情。這次交流加深了我們對印度的認識，也讓我們有機會向遠方的朋友介紹台灣。")
    ]}
 ],
 "pullquote":{"en":"An Indian girl in traditional dress danced — and we could not look away.","zh":"一位身著傳統服飾的印度女孩跳起舞，我們看得目不轉睛。"},
 "keywords":[
   {"w":"culture","p":"n.","zh":"文化","en":"We shared our culture with India.","z":"我們和印度分享我們的文化。"},
   {"w":"group","p":"n.","zh":"小組","en":"Each group introduced one topic.","z":"每一組介紹一個主題。"},
   {"w":"snack","p":"n.","zh":"零食","en":"We showed them our favorite snacks.","z":"我們介紹了最愛的零食。"},
   {"w":"currency","p":"n.","zh":"貨幣","en":"We introduced Taiwan's currency.","z":"我們介紹了台灣的貨幣。"},
   {"w":"pottery","p":"n.","zh":"陶器","en":"The blue pottery of Jaipur is famous.","z":"齋浦爾的藍陶很有名。"},
   {"w":"traditional","p":"adj.","zh":"傳統的","en":"She wore a traditional dress.","z":"她穿著傳統的服飾。"},
   {"w":"perform","p":"v.","zh":"表演","en":"An Indian girl performed a dance.","z":"一位印度女孩表演了一支舞。"},
   {"w":"graceful","p":"adj.","zh":"優雅的","en":"Her dance was very graceful.","z":"她的舞蹈非常優雅。"}
 ],
 "dialogue":{"scene_en":"After the dance, two students talk about what they saw.","scene_zh":"舞蹈之後，兩位學生聊起剛剛看到的表演。",
   "lines":[
     ("A","Your dance was so graceful! Thank you.","你的舞好優雅！謝謝你。"),
     ("B","Thank you! Your snacks look yummy too.","謝謝你！你們的零食看起來也好好吃。"),
     ("A","We have five groups, each with a topic.","我們有五組，每組一個主題。"),
     ("B","Nice! Tell me about Taiwanese festivals.","真好！跟我說說台灣的節慶吧。"),
     ("A","We have lantern festivals with bright lights.","我們有充滿燈光的燈節。"),
     ("B","I would love to see them one day.","真希望有一天能親眼看到。")
   ]}
},

{
 "slug":"spain-reply-letters", "flag":"🇪🇸",
 "tag_en":"Postcard Exchange","tag_zh":"明信片交流",
 "date_iso":"2025-04-17","date_en":"April 17, 2025","date_zh":"2025 年 4 月 17 日",
 "klass":"Grade 6 · 六年級","partner":"CEIP Boqueres, Spain · 西班牙",
 "title":"A Reply Arrives<br>From Spain","title_zh":"來自西班牙的回信",
 "lede_en":"The postcards we sent last semester finally came home with a reply — neat English, hand-drawn pictures, woven bracelets, and even Spanish candy. The English was hard, but we cracked it together.",
 "lede_zh":"上學期寄出的明信片，終於收到回音——工整的英文、手繪的圖畫、編織的手環，還有西班牙糖果。英文很難，但我們一起破解了。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>A letter from CEIP Boqueres</b> · opened together, decoded together","cap_zh":"來自 CEIP Boqueres 的信・一起打開、一起讀懂"},
 "body":[
   {"h_en":"What the Envelope Held","h_zh":"信封裡的驚喜",
    "paras":[
     ("The postcards our sixth graders mailed to Spain last semester finally received a reply! With great excitement, the children opened the long-awaited letters from <strong>CEIP Boqueres</strong>. Inside were neatly written English messages, elegant hand-drawn illustrations, beautifully woven friendship bracelets, and even some Spanish candies — one delightful surprise after another.",
      "六年級的孩子上學期寄到西班牙的明信片，終於收到回音了！大家興奮地打開遠從 <strong>CEIP Boqueres</strong> 寄來的信。信裡有工整的英文、雅緻的手繪插圖、精巧的手工編織手環，還有西班牙糖果，驚喜接連不斷。")
    ]},
   {"h_en":"Cracking the Code Together","h_zh":"一起破解密碼",
    "paras":[
     ("Faced with a long string of unfamiliar English, the students did not give up. Instead they discussed, helped one another, and worked together to figure out what the letters said.",
      "面對一大串看不懂的英文，同學們並不氣餒，反而主動討論、彼此幫忙，一起破解信件的內容。"),
     ("Through this cross-cultural exchange, the children felt the richness of a different culture — and discovered the joy of learning a language and the power of working as a team.",
      "透過這段跨國交流，孩子們不只感受到文化的多樣，也在過程中發現了語言的樂趣與團隊合作的力量。")
    ]}
 ],
 "pullquote":{"en":"The English was hard — so we read it together.","zh":"英文很難，所以我們一起讀。"},
 "keywords":[
   {"w":"letter","p":"n.","zh":"信","en":"We opened a letter from Spain.","z":"我們打開了一封來自西班牙的信。"},
   {"w":"reply","p":"n.","zh":"回信","en":"We waited a long time for the reply.","z":"我們等了很久才等到回信。"},
   {"w":"bracelet","p":"n.","zh":"手環","en":"They sent us woven bracelets.","z":"他們寄來了編織的手環。"},
   {"w":"surprise","p":"n.","zh":"驚喜","en":"The envelope was full of surprises.","z":"信封裡滿滿都是驚喜。"},
   {"w":"understand","p":"v.","zh":"理解","en":"We tried hard to understand the English.","z":"我們努力理解那些英文。"},
   {"w":"teamwork","p":"n.","zh":"團隊合作","en":"Teamwork helped us read the letter.","z":"團隊合作幫我們讀懂了信。"},
   {"w":"culture","p":"n.","zh":"文化","en":"We learned about Spanish culture.","z":"我們認識了西班牙文化。"},
   {"w":"candy","p":"n.","zh":"糖果","en":"They even sent us Spanish candy.","z":"他們甚至寄來了西班牙糖果。"}
 ],
 "dialogue":{"scene_en":"Two classmates open the letter from Spain together.","scene_zh":"兩位同學一起打開來自西班牙的信。",
   "lines":[
     ("A","Look! A reply finally came from Spain.","你看！西班牙終於回信了。"),
     ("B","There are bracelets and candy inside!","裡面有手環和糖果！"),
     ("A","The English is hard. Can you read this part?","英文好難。這一段你看得懂嗎？"),
     ("B","Let me try. I think it says thank you.","我試試看，我猜是在說謝謝。"),
     ("A","Yes! Together we can understand it.","對！我們一起就能讀懂。"),
     ("B","Reading with a friend is more fun.","和朋友一起讀更有趣。")
   ]}
},

{
 "slug":"israel-culture-box", "flag":"🇮🇱",
 "tag_en":"Culture Box","tag_zh":"文化箱交流",
 "date_iso":"2025-03-31","date_en":"March 31, 2025","date_zh":"2025 年 3 月 31 日",
 "klass":"Class 6B · 六年乙班","partner":"A partner school in Israel · 以色列",
 "title":"A Box Arrives<br>From Israel","title_zh":"以色列寄來的文化箱",
 "lede_en":"Salty olives, peanutty Bamba, a game of Snakes and Ladders, and a set of special cups for the Sabbath — a box from Israel that taught us about a faraway way of life.",
 "lede_zh":"鹹鹹的橄欖、花生味的 Bamba、一副蛇梯棋，還有一組安息日專用的杯子——一只以色列寄來的箱子，教我們認識遙遠的生活方式。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>A culture box from Israel</b> · olives, Bamba, a board game, and Shabbat cups","cap_zh":"來自以色列的文化箱・橄欖、Bamba、桌遊與安息日的杯子"},
 "body":[
   {"h_en":"Opening the Box","h_zh":"打開箱子",
    "paras":[
     ("Class 6B received a culture box from Israel! Inside was a jar of <strong>olives</strong> — salty and a little sour. We each took a small taste, and the flavor was truly one of a kind. There was also a bag of <strong>Bamba</strong>, a popular Israeli corn snack with a rich peanut flavor, and a classic board game, <strong>Snakes and Ladders</strong>, that Israeli friends often play together.",
      "六年乙班收到了來自以色列的文化箱！箱子裡有一罐<strong>橄欖</strong>，鹹鹹酸酸的，我們淺嚐一口，味道真的很特別；還有一包<strong>Bamba</strong>——一款花生口味的玉米點心；以及一副經典桌遊<strong>蛇梯棋</strong>，是以色列朋友間常玩、增進感情的遊戲。")
    ]},
   {"h_en":"Cups for a Sacred Day","h_zh":"獻給神聖日子的杯子",
    "paras":[
     ("The most special item was a set of cups for <strong>Shabbat</strong>, the Jewish Sabbath. Shabbat is an important religious tradition in Israel, and the cups stand for its blessings and the togetherness of family.",
      "箱子裡最特別的，是一個個代表<strong>安息日（Shabbat）</strong>的杯子。安息日是以色列文化中重要的宗教傳統，這個杯子象徵著安息日的祝福與團聚。"),
     ("These gifts from far away helped us understand Israel's culture and traditions far more deeply than any textbook could.",
      "這些來自遠方的禮物，讓我們對以色列的文化與傳統，有了比課本更深刻的理解。")
    ]}
 ],
 "pullquote":{"en":"A box from far away taught us a whole way of life.","zh":"一只遠方的箱子，教會我們一種生活方式。"},
 "keywords":[
   {"w":"box","p":"n.","zh":"箱子","en":"We opened a culture box from Israel.","z":"我們打開了以色列的文化箱。"},
   {"w":"taste","p":"v.","zh":"品嚐","en":"We tasted the olives carefully.","z":"我們小心地品嚐橄欖。"},
   {"w":"snack","p":"n.","zh":"零食","en":"Bamba is a peanut snack from Israel.","z":"Bamba 是以色列的花生零食。"},
   {"w":"flavor","p":"n.","zh":"味道","en":"The olives had a special flavor.","z":"橄欖有著特別的味道。"},
   {"w":"tradition","p":"n.","zh":"傳統","en":"Shabbat is an important tradition.","z":"安息日是重要的傳統。"},
   {"w":"blessing","p":"n.","zh":"祝福","en":"The cup is a sign of blessing.","z":"這個杯子象徵著祝福。"},
   {"w":"culture","p":"n.","zh":"文化","en":"The box taught us about Israeli culture.","z":"這個箱子讓我們認識以色列文化。"},
   {"w":"together","p":"adv.","zh":"一起","en":"Families share the Sabbath together.","z":"家人一起度過安息日。"}
 ],
 "dialogue":{"scene_en":"Two students unbox the gifts from Israel.","scene_zh":"兩位學生一起拆開以色列的禮物。",
   "lines":[
     ("A","Try this olive. It is salty and sour!","嚐嚐這顆橄欖，又鹹又酸！"),
     ("B","Wow, what a special flavor. What is this snack?","哇，味道好特別。這個零食是什麼？"),
     ("A","It is Bamba. It tastes like peanuts.","它叫 Bamba，吃起來像花生。"),
     ("B","And these cups? They look important.","那這些杯子呢？看起來很重要。"),
     ("A","They are for Shabbat, a special day in Israel.","它們是安息日用的，以色列的特別日子。"),
     ("B","Now I understand their culture better.","現在我更懂他們的文化了。")
   ]}
},

{
 "slug":"japan-class-5b", "flag":"🇯🇵",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2025-02-27","date_en":"February 27, 2025","date_zh":"2025 年 2 月 27 日",
 "klass":"Class 5B · 五年乙班","partner":"Muneoka Daisan Elementary, Japan · 日本",
 "title":"School Days,<br>Shared with Japan","title_zh":"和日本分享校園的日常",
 "lede_en":"Class 5B introduced Japan to Taiwan's Indigenous cultures and rare animals — and heard, in return, all about sports festivals and singing contests at a school in Saitama.",
 "lede_zh":"五年乙班向日本介紹台灣的原住民文化與特有動物，也聽見了埼玉一所小學裡的運動會與歌唱比賽。",
 "media":{"type":"slideshow","n":7,
   "cap_en":"<b>Class 5B × Muneoka Daisan Elementary</b> · a warm exchange with Shiki City, Saitama","cap_zh":"五年乙班 × 日本宗岡第三小學・與埼玉縣志木市的溫暖交流"},
 "body":[
   {"h_en":"The Treasures of Taiwan","h_zh":"台灣的瑰寶",
    "paras":[
     ("Class 5B had a wonderful online exchange with <strong>Muneoka Daisan Elementary School</strong> in Shiki City, Saitama, Japan. After greetings and a tour of our beautiful campus, both sides moved into smaller groups for a deeper chat.",
      "五年乙班與日本埼玉縣志木市<strong>宗岡第三國小</strong>進行了一場精彩的線上交流。在問候、介紹完我們美麗的校園後，雙方進入更深入的分組交流。"),
     ("Our students introduced Taiwan's <strong>Indigenous cultures</strong>, our <strong>unique animals</strong>, our <strong>national treasures</strong>, and our food and famous places.",
      "我們向日本小朋友介紹了台灣的<strong>原住民文化</strong>、<strong>特有動物</strong>、<strong>國寶</strong>，以及台灣的美食與景點。")
    ]},
   {"h_en":"A Look Inside a Japanese School","h_zh":"走進日本的校園",
    "paras":[
     ("In return, the Japanese students shared their school life and campus activities — their <strong>sports festival</strong> and their <strong>singing contest</strong> among them.",
      "日本的小朋友則向我們介紹了他們的校園生活與活動，包括<strong>運動會</strong>與<strong>歌唱比賽</strong>。"),
     ("Their sharing let us feel the warmth of Japanese school culture, and see how schools in two different countries can each have their own atmosphere.",
      "他們的分享讓我們感受到日本校園文化的溫暖，也看見了兩個國家校園各自不同的氛圍。")
    ]}
 ],
 "pullquote":{"en":"Two schools, two countries, one warm afternoon.","zh":"兩所學校、兩個國家，一個溫暖的午後。"},
 "keywords":[
   {"w":"campus","p":"n.","zh":"校園","en":"We showed them our beautiful campus.","z":"我們向他們介紹了美麗的校園。"},
   {"w":"Indigenous","p":"adj.","zh":"原住民的","en":"We introduced Taiwan's Indigenous cultures.","z":"我們介紹了台灣的原住民文化。"},
   {"w":"treasure","p":"n.","zh":"國寶、珍寶","en":"The pangolin is a national treasure.","z":"穿山甲是國寶級動物。"},
   {"w":"sports festival","p":"n.","zh":"運動會","en":"Their sports festival looked exciting.","z":"他們的運動會看起來很精彩。"},
   {"w":"contest","p":"n.","zh":"比賽","en":"They hold a singing contest every year.","z":"他們每年舉辦歌唱比賽。"},
   {"w":"share","p":"v.","zh":"分享","en":"Both schools shared their school life.","z":"兩校都分享了校園生活。"},
   {"w":"group","p":"n.","zh":"小組","en":"We talked in small groups.","z":"我們以小組方式交流。"},
   {"w":"warm","p":"adj.","zh":"溫暖的","en":"It was a warm and friendly exchange.","z":"這是一場溫暖友善的交流。"}
 ],
 "dialogue":{"scene_en":"A KangLang and a Japanese student compare their schools.","scene_zh":"槺榔與日本的學生互相介紹自己的學校。",
   "lines":[
     ("B","Konnichiwa! Tell us about your school.","你好！跟我們說說你們的學校吧。"),
     ("A","We learn about Taiwan's Indigenous cultures.","我們會學習台灣的原住民文化。"),
     ("B","That is interesting! We have a big sports festival.","好有趣！我們有盛大的運動會。"),
     ("A","We love sports too. What else do you do?","我們也喜歡運動。你們還有什麼活動？"),
     ("B","We have a singing contest every year.","我們每年都有歌唱比賽。"),
     ("A","Maybe one day we can sing together!","也許有一天我們能一起唱歌！")
   ]}
},

{
 "slug":"japan-class-5a", "flag":"🇯🇵",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2025-02-26","date_en":"February 26, 2025","date_zh":"2025 年 2 月 26 日",
 "klass":"Class 501 · 五年甲班","partner":"Muneoka Daisan Elementary, Japan · 日本",
 "title":"Five Groups<br>Meet Japan","title_zh":"五個小組，認識日本",
 "lede_en":"Class 501 split into five groups to introduce Taiwan's landmarks, wildlife, history, food, and money — then gathered for a happy Taiwan–Japan group photo.",
 "lede_zh":"五年甲班分成五組，介紹台灣的景點、動植物、歷史人物、美食與貨幣，最後拍下一張開心的台日大合照。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>Class 501 × Muneoka Daisan Elementary</b> · introducing Taiwan, group by group","cap_zh":"五年甲班 × 日本宗岡第三小學・一組一組介紹台灣"},
 "body":[
   {"h_en":"Taiwan in Five Groups","h_zh":"五組介紹台灣",
    "paras":[
     ("Class 501 had an enjoyable online exchange with <strong>Muneoka Daisan Elementary School</strong> in Shiki City, Saitama, Japan. After greeting our Japanese friends, we introduced our own small-but-beautiful school.",
      "五年甲班與日本埼玉縣志木市<strong>宗岡第三國小</strong>進行了一場充滿趣味的線上交流。我們先與日方學生打招呼，介紹了我們小而美的槺榔國小。"),
     ("Then both sides split into five groups, taking turns to share the special things about their countries. Our students presented Taiwan's <strong>famous landmarks</strong>, our <strong>unique plants and animals</strong>, our <strong>historical figures</strong>, our <strong>traditional foods</strong>, and the <strong>New Taiwan Dollar</strong>.",
      "接著，雙方分成五組，輪流介紹各自國家的特色。我們向日本小朋友介紹了台灣的<strong>知名景點</strong>、<strong>特有動植物</strong>、<strong>歷史人物</strong>、<strong>傳統美食</strong>與<strong>新台幣</strong>。")
    ]},
   {"h_en":"A Photo to Remember","h_zh":"值得紀念的合照",
    "paras":[
     ("In return, the Japanese students introduced their school, their local snacks, and their own distinctive culture.",
      "日本的小朋友也依序向我們介紹了他們的學校、當地的小吃，以及獨特的文化特色。"),
     ("At the very end, both sides came together for a big Taiwan–Japan group photo, capturing the joy of a meaningful afternoon.",
      "活動的最後，台日雙方一起拍了一張大合照，記錄下這場愉快而有意義的交流。")
    ]}
 ],
 "pullquote":{"en":"Taking turns, group by group, we showed them all of Taiwan.","zh":"一組接著一組，我們把整個台灣介紹給他們。"},
 "keywords":[
   {"w":"landmark","p":"n.","zh":"地標、景點","en":"We introduced Taiwan's famous landmarks.","z":"我們介紹了台灣著名的景點。"},
   {"w":"animal","p":"n.","zh":"動物","en":"Taiwan has many unique animals.","z":"台灣有許多特有的動物。"},
   {"w":"history","p":"n.","zh":"歷史","en":"We shared Taiwan's historical figures.","z":"我們分享了台灣的歷史人物。"},
   {"w":"food","p":"n.","zh":"食物","en":"Taiwanese food is delicious.","z":"台灣美食很好吃。"},
   {"w":"money","p":"n.","zh":"錢、貨幣","en":"We showed them the New Taiwan Dollar.","z":"我們介紹了新台幣。"},
   {"w":"group","p":"n.","zh":"小組","en":"We worked in five groups.","z":"我們分成五組進行。"},
   {"w":"photo","p":"n.","zh":"照片","en":"We took a group photo at the end.","z":"最後我們拍了一張大合照。"},
   {"w":"introduce","p":"v.","zh":"介紹","en":"Each group introduced one topic.","z":"每一組介紹一個主題。"}
 ],
 "dialogue":{"scene_en":"Two students introduce their countries and pose for a photo.","scene_zh":"兩位學生介紹自己的國家，並一起拍照。",
   "lines":[
     ("A","Our group will introduce Taiwanese food.","我們這組要介紹台灣美食。"),
     ("B","Great! What is your favorite dish?","太好了！你最喜歡哪一道？"),
     ("A","I love beef noodle soup. How about you?","我最愛牛肉麵。你呢？"),
     ("B","I like sushi and ramen very much.","我很喜歡壽司和拉麵。"),
     ("A","Let us take a group photo together!","我們一起拍張合照吧！"),
     ("B","Yes! One, two, three — smile!","好！一、二、三——笑一個！")
   ]}
},

{
 "slug":"israel-taiwan-treasures", "flag":"🇮🇱",
 "tag_en":"International Exchange · Culture","tag_zh":"國際交流・文化",
 "date_iso":"2025-02-24","date_en":"February 24, 2025","date_zh":"2025 年 2 月 24 日",
 "klass":"Class 602 · 六年乙班","partner":"Ofek–Giat Zeev School, Israel · 以色列",
 "title":"Swapping the Treasures<br>of Two Countries","title_zh":"交換兩國的寶物",
 "lede_en":"Class 602 introduced Israel to Taiwanese snacks, folk toys, cultural objects, and our coins and bills — and agreed to mail each other a box of treasures across the world.",
 "lede_zh":"六年乙班向以色列介紹台灣的傳統點心、童玩、文物與新台幣，並約定互寄一箱寶物到地球的另一端。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>Class 602 × Ofek–Giat Zeev School</b> · a treasure-swap with Israel","cap_zh":"六年乙班 × 以色列 Ofek–Giat Zeev 學校・一場跨國的寶物交換"},
 "body":[
   {"h_en":"Treasures from Taiwan","h_zh":"來自台灣的寶物",
    "paras":[
     ("Class 602 had an exciting online exchange with <strong>Ofek–Giat Zeev School</strong> in Israel. Our students introduced all sorts of Taiwanese treasures: our <strong>traditional snacks</strong>, our <strong>folk toys</strong>, our <strong>cultural objects</strong>, and the different coins and bills of the <strong>New Taiwan Dollar</strong>. The Israeli students shared their own cultural items on the same themes.",
      "六年乙班與以色列 <strong>Ofek–Giat Zeev 學校</strong>進行了一場有趣的線上交流。我們介紹了台灣的各種寶物：<strong>傳統點心</strong>、<strong>傳統童玩</strong>、<strong>文化物品</strong>，以及<strong>新台幣</strong>的各種幣值。以色列的小朋友也以相同的主題，分享了他們的文化物品。")
    ]},
   {"h_en":"The Exchange Continues by Mail","h_zh":"交流，靠郵寄繼續",
    "paras":[
     ("Even though we come from different cultures, everyone spoke in English, and the conversation flowed smoothly and happily.",
      "雖然我們來自不同的文化背景，但大家都用英語溝通，讓交流更加順利愉快。"),
     ("And the meeting was only the beginning. We agreed to mail the Taiwanese items we had shown to Israel, while the Israeli students would send their treasures to Taiwan. We could not wait for the box to arrive — a memory in the making.",
      "而這場線上會面只是開始。我們約定把介紹過的台灣物品寄到以色列，以色列的小朋友也會把他們的寶物寄到台灣。我們迫不及待地期待那只箱子的到來——一段正在發生的回憶。")
    ]}
 ],
 "pullquote":{"en":"The call ended, but the friendship was only beginning.","zh":"視訊結束了，友誼才剛開始。"},
 "keywords":[
   {"w":"treasure","p":"n.","zh":"寶物","en":"We shared our cultural treasures.","z":"我們分享了文化寶物。"},
   {"w":"snack","p":"n.","zh":"點心","en":"We introduced traditional snacks.","z":"我們介紹了傳統點心。"},
   {"w":"toy","p":"n.","zh":"玩具","en":"Folk toys are fun to play with.","z":"傳統童玩玩起來很有趣。"},
   {"w":"coin","p":"n.","zh":"硬幣","en":"We showed them our coins and bills.","z":"我們介紹了硬幣和紙鈔。"},
   {"w":"communicate","p":"v.","zh":"溝通","en":"We communicated in English.","z":"我們用英語溝通。"},
   {"w":"mail","p":"v.","zh":"郵寄","en":"We will mail a box to Israel.","z":"我們要寄一個箱子到以色列。"},
   {"w":"exchange","p":"n.","zh":"交流","en":"The exchange was smooth and happy.","z":"這場交流順利又愉快。"},
   {"w":"culture","p":"n.","zh":"文化","en":"We come from different cultures.","z":"我們來自不同的文化。"}
 ],
 "dialogue":{"scene_en":"Two students plan to swap boxes of treasures.","scene_zh":"兩位學生約定互寄一箱寶物。",
   "lines":[
     ("A","This is a Taiwanese spinning top. It is a folk toy.","這是台灣的陀螺，一種傳統童玩。"),
     ("B","So cool! We have special treasures too.","好酷！我們也有特別的寶物。"),
     ("A","Let us mail our items to each other.","我們把東西互相寄給對方吧。"),
     ("B","Yes! I will send you a box from Israel.","好！我會從以色列寄一個箱子給你。"),
     ("A","I cannot wait to open it!","我等不及要打開了！"),
     ("B","Me too. Our friendship is just starting.","我也是。我們的友誼才剛開始。")
   ]}
},

{
 "slug":"turkiye-culture-box", "flag":"🇹🇷",
 "tag_en":"Culture Box","tag_zh":"文化箱交流",
 "date_iso":"2025-01-13","date_en":"January 13, 2025","date_zh":"2025 年 1 月 13 日",
 "klass":"Grade 5 · 五年級","partner":"İstanbul Ticaret Odası BİLSEM, Türkiye · 土耳其",
 "title":"Unboxing a Gift<br>From Türkiye","title_zh":"開箱！土耳其的文化禮物",
 "lede_en":"After the end-of-term ceremony came the moment our fifth graders had waited for — opening a culture box from Türkiye, full of handwritten cards, bookmarks, a woven backpack, and the famous blue evil-eye charm.",
 "lede_zh":"結業式之後，五年級孩子引頸期盼的時刻到了——打開來自土耳其的文化箱，裡頭有手寫卡片、書籤、編織背包，還有著名的藍眼睛護身符。",
 "media":{"type":"slideshow","n":9,
   "cap_en":"<b>A culture box from İstanbul</b> · cards, bookmarks, a backpack, and the blue evil-eye charm","cap_zh":"來自伊斯坦堡的文化箱・卡片、書籤、背包與藍眼睛護身符"},
 "body":[
   {"h_en":"The Long-Awaited Unboxing","h_zh":"期待已久的開箱",
    "paras":[
     ("Our fifth graders received a culture box from <strong>İstanbul Ticaret Odası BİLSEM</strong> in Türkiye! The long-awaited unboxing took place right after our end-of-semester ceremony.",
      "五年級的孩子收到了土耳其 <strong>İstanbul Ticaret Odası BİLSEM</strong> 寄來的文化箱！這場引頸期盼的開箱活動，就在學期結業式之後進行。"),
     ("Inside the box were handwritten cards, İstanbul-style <strong>bookmarks</strong>, an ethnic-patterned <strong>backpack</strong>, a charming folding <strong>mirror</strong>, and Türkiye's famous blue <strong>&ldquo;evil eye&rdquo; charm</strong>.",
      "土耳其寄來的箱子裡，不只裝著一張張手寫卡片，還有伊斯坦堡風的<strong>書籤</strong>、富有民族風的<strong>背包</strong>、精巧的<strong>摺疊鏡</strong>，以及土耳其著名的藍色<strong>「邪眼」護身符</strong>。")
    ]},
   {"h_en":"Words That Became Friendship","h_zh":"化作友誼的文字",
    "paras":[
     ("Every handwritten card was filled with warm words of friendship. As we read them, those words turned into a quiet, fluttering joy in our hearts.",
      "每一張手寫卡片裡，滿滿的文字，都是滿滿的友誼。讀著讀著，那些字句化作我們心田裡翩翩飛舞的感動。")
    ]}
 ],
 "pullquote":{"en":"Each card was filled with words of friendship.","zh":"每一張卡片，都寫滿了友誼。"},
 "keywords":[
   {"w":"unbox","p":"v.","zh":"開箱","en":"We could not wait to unbox the gift.","z":"我們迫不及待地開箱。"},
   {"w":"card","p":"n.","zh":"卡片","en":"Each card was handwritten with care.","z":"每張卡片都是用心手寫的。"},
   {"w":"bookmark","p":"n.","zh":"書籤","en":"They sent us Istanbul-style bookmarks.","z":"他們寄來伊斯坦堡風的書籤。"},
   {"w":"backpack","p":"n.","zh":"背包","en":"The woven backpack has ethnic patterns.","z":"這個編織背包有民族風的圖案。"},
   {"w":"charm","p":"n.","zh":"護身符","en":"The blue evil-eye charm is famous in Türkiye.","z":"藍眼睛護身符在土耳其很有名。"},
   {"w":"gift","p":"n.","zh":"禮物","en":"The box was full of lovely gifts.","z":"箱子裡滿是可愛的禮物。"},
   {"w":"friendship","p":"n.","zh":"友誼","en":"The cards were full of friendship.","z":"卡片裡滿滿都是友誼。"},
   {"w":"receive","p":"v.","zh":"收到","en":"We received a box from far away.","z":"我們收到了來自遠方的箱子。"}
 ],
 "dialogue":{"scene_en":"Two students unbox the gift from Türkiye.","scene_zh":"兩位學生一起拆開土耳其的禮物。",
   "lines":[
     ("A","Look, a box came all the way from Türkiye!","你看，一個箱子大老遠從土耳其來了！"),
     ("B","What is inside? Open it, open it!","裡面有什麼？快打開、快打開！"),
     ("A","There are bookmarks and a blue charm.","有書籤，還有一個藍色護身符。"),
     ("B","The charm is called the evil eye. It is for good luck.","那個護身符叫邪眼，是用來祈求好運的。"),
     ("A","And so many handwritten cards!","還有好多手寫卡片！"),
     ("B","Each one is full of friendship.","每一張都寫滿了友誼。")
   ]}
},

{
 "slug":"turkiye-postcards-sent", "flag":"🇹🇷",
 "tag_en":"Postcard Exchange","tag_zh":"明信片交流",
 "date_iso":"2025-01-06","date_en":"January 6, 2025","date_zh":"2025 年 1 月 6 日",
 "klass":"Grade 5 · 五年級","partner":"İstanbul Ticaret Odası BİLSEM, Türkiye · 土耳其",
 "title":"Postcards on Their Way<br>to Türkiye","title_zh":"寄往土耳其的明信片",
 "lede_en":"Our fifth graders handwrote postcards for a gifted-and-talented school in İstanbul, and tucked in Taiwanese snacks and KangLang souvenirs — opening a window onto the wider world.",
 "lede_zh":"五年級的孩子親手寫下明信片，寄給伊斯坦堡一所資優學校，還附上台灣零食與槺榔的文創紀念品——為自己推開一扇通往世界的窗。",
 "media":{"type":"slideshow","n":6,
   "cap_en":"<b>Handwritten for İstanbul</b> · postcards, snacks, and KangLang souvenirs","cap_zh":"親手寫給伊斯坦堡・明信片、零食與槺榔文創"},
 "body":[
   {"h_en":"A Window and a Door","h_zh":"一扇窗，一道門",
    "paras":[
     ("Our fifth graders handwrote self-introduction postcards to send to <strong>İstanbul Ticaret Odası BİLSEM</strong> in Türkiye. This is a special school for gifted and talented students, chosen through careful selection. By writing to them, our fifth graders not only opened a window onto the world — they also pushed open a door into a very different school system.",
      "五年級的孩子親手書寫自我介紹的明信片，寄到土耳其 <strong>İstanbul Ticaret Odası BİLSEM</strong>。這是一所特殊教育學校，裡面的孩子都是經過測驗篩選的菁英。透過與他們交流，我們的五年級孩子不只打開了通往國際的窗，也推開了體驗不同教育體制的門。")
    ]},
   {"h_en":"A Taste of Taiwan in the Parcel","h_zh":"包裹裡的台灣味",
    "paras":[
     ("Alongside the postcards full of Taiwanese flavor, our students packed some of their favorite Taiwanese snacks and a few creative souvenirs from KangLang, to share with their new friends in Türkiye.",
      "除了充滿台灣味的明信片，我們的包裹裡還裝了孩子們喜歡的台灣點心，以及槺榔國小的文創紀念品，要和土耳其的新朋友分享。")
    ]}
 ],
 "pullquote":{"en":"A postcard opened a window onto the wider world.","zh":"一張明信片，推開了通往世界的窗。"},
 "keywords":[
   {"w":"postcard","p":"n.","zh":"明信片","en":"We handwrote a postcard for our friends.","z":"我們親手為朋友寫了明信片。"},
   {"w":"handwrite","p":"v.","zh":"手寫","en":"Each student handwrote their card.","z":"每位學生都親手寫卡片。"},
   {"w":"introduce","p":"v.","zh":"介紹（自己）","en":"The postcard introduces who we are.","z":"明信片介紹了我們是誰。"},
   {"w":"snack","p":"n.","zh":"零食","en":"We packed Taiwanese snacks to share.","z":"我們裝了台灣零食要分享。"},
   {"w":"souvenir","p":"n.","zh":"紀念品","en":"We added souvenirs from KangLang.","z":"我們放入了槺榔的紀念品。"},
   {"w":"parcel","p":"n.","zh":"包裹","en":"We sent a parcel all the way to Türkiye.","z":"我們把包裹一路寄到土耳其。"},
   {"w":"talented","p":"adj.","zh":"有天賦的","en":"It is a school for talented students.","z":"那是一所資優學生的學校。"},
   {"w":"share","p":"v.","zh":"分享","en":"We love to share Taiwan with friends.","z":"我們喜歡和朋友分享台灣。"}
 ],
 "dialogue":{"scene_en":"Two students get a parcel ready to mail to İstanbul.","scene_zh":"兩位學生準備把包裹寄往伊斯坦堡。",
   "lines":[
     ("A","I finished my postcard. I wrote about my hobbies.","我寫好明信片了，我介紹了我的興趣。"),
     ("B","Nice! Let us add some Taiwanese snacks.","真好！我們再放些台灣零食吧。"),
     ("A","Good idea. And a KangLang souvenir too.","好主意，再加一個槺榔的紀念品。"),
     ("B","I hope our friends in İstanbul like it.","希望伊斯坦堡的朋友會喜歡。"),
     ("A","Writing to them feels like meeting the world.","寫信給他們，感覺像認識了世界。"),
     ("B","Let us mail it today!","我們今天就寄出去吧！")
   ]}
},

{
 "slug":"spain-postcards-sent", "flag":"🇪🇸",
 "tag_en":"Postcard Exchange","tag_zh":"明信片交流",
 "date_iso":"2025-01-05","date_en":"January 5, 2025","date_zh":"2025 年 1 月 5 日",
 "klass":"Grade 6 · 六年級","partner":"CEIP Boqueres, Spain · 西班牙",
 "title":"Postcards and<br>Warm Wishes for Spain","title_zh":"寄給西班牙的明信片與祝福",
 "lede_en":"Our sixth graders made self-introduction videos and postcards bursting with Taiwanese flavor for a school in Spain — and added their heartfelt wishes after hearing of the floods in Valencia.",
 "lede_zh":"六年級的孩子為西班牙的學校準備了自我介紹影片與充滿台灣味的明信片，也在得知瓦倫西亞水災後，捎上最誠摯的祝福。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>For CEIP Boqueres</b> · self-introduction videos and Taiwanese postcards","cap_zh":"寄給 CEIP Boqueres・自我介紹影片與台灣味的明信片"},
 "body":[
   {"h_en":"A Greeting With Taiwanese Flavor","h_zh":"帶著台灣味的問候",
    "paras":[
     ("Our sixth graders got everything ready to send to <strong>CEIP Boqueres</strong> in Spain: short self-introduction videos, and beautifully designed postcards bursting with Taiwanese flavor.",
      "六年級的孩子準備好了要寄到西班牙 <strong>CEIP Boqueres</strong> 的東西：一支支自我介紹的影片，還有設計得美美的、充滿台灣味的明信片。")
    ]},
   {"h_en":"Wishes Across the Water","h_zh":"越過海洋的祝福",
    "paras":[
     ("Then we saw the news that the <strong>Valencia</strong> region of Spain had been hit by severe flooding the month before. We sincerely hoped that all the teachers and students at CEIP Boqueres were safe and well.",
      "後來我們看到新聞，西班牙<strong>瓦倫西亞</strong>地區在上個月經歷了一場嚴重的水災。我們衷心希望 CEIP Boqueres 的師生們都平安無事。"),
     ("Through each small postcard, we sent our warmest wishes to our friends in Spain.",
      "藉由一張張小小的明信片，我們把最誠摯的祝福，捎給西班牙的朋友們。")
    ]}
 ],
 "pullquote":{"en":"Through each small postcard, we sent our warmest wishes.","zh":"藉由一張張小小的明信片，捎上我們最誠摯的祝福。"},
 "keywords":[
   {"w":"postcard","p":"n.","zh":"明信片","en":"We designed postcards for Spain.","z":"我們為西班牙設計了明信片。"},
   {"w":"video","p":"n.","zh":"影片","en":"We made self-introduction videos.","z":"我們製作了自我介紹影片。"},
   {"w":"design","p":"v.","zh":"設計","en":"We designed each card with care.","z":"我們用心設計每一張卡片。"},
   {"w":"flood","p":"n.","zh":"水災","en":"A flood hit the Valencia region.","z":"瓦倫西亞地區發生了水災。"},
   {"w":"safe","p":"adj.","zh":"平安的","en":"We hope everyone is safe and well.","z":"我們希望大家平安健康。"},
   {"w":"wish","p":"n.","zh":"祝福","en":"We sent our warmest wishes.","z":"我們捎上最溫暖的祝福。"},
   {"w":"sincere","p":"adj.","zh":"誠摯的","en":"Our wishes were sincere.","z":"我們的祝福很誠摯。"},
   {"w":"friend","p":"n.","zh":"朋友","en":"We care about our friends in Spain.","z":"我們關心西班牙的朋友。"}
 ],
 "dialogue":{"scene_en":"Two students prepare their postcards and wishes for Spain.","scene_zh":"兩位學生準備寄給西班牙的明信片與祝福。",
   "lines":[
     ("A","I finished my postcard for CEIP Boqueres.","我寫好給 CEIP Boqueres 的明信片了。"),
     ("B","Did you hear about the floods in Valencia?","你聽說瓦倫西亞水災了嗎？"),
     ("A","Yes. I hope everyone there is safe.","聽說了，希望那裡的人都平安。"),
     ("B","Let us add a few words of comfort.","我們加幾句安慰的話吧。"),
     ("A","Good idea. Stay safe, friends in Spain.","好主意。西班牙的朋友，要平安喔。"),
     ("B","Our wishes will travel with the postcards.","我們的祝福會隨著明信片一起寄出。")
   ]}
},

{
 "slug":"israel-christmas-recorder", "flag":"🇮🇱",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2024-12-26","date_en":"December 26, 2024","date_zh":"2024 年 12 月 26 日",
 "klass":"Class 602 · 六年乙班","partner":"Ofek–Giat Zeev School, Israel · 以色列",
 "title":"A Christmas Song<br>for Israel","title_zh":"吹給以色列的聖誕歌",
 "lede_en":"Class 602 learned about Israel's food, language, and famous people — and answered with a Christmas carol on the recorder, sending joy and peace to the other side of the world.",
 "lede_zh":"六年乙班認識了以色列的食物、語言與名人，也用中音笛吹奏聖誕歌曲回應，把喜悅與和平送到地球的另一端。",
 "media":{"type":"slideshow","n":7,
   "cap_en":"<b>Class 602 × Ofek–Giat Zeev School</b> · a Christmas exchange with Israel","cap_zh":"六年乙班 × 以色列 Ofek–Giat Zeev 學校・聖誕節的交流"},
 "body":[
   {"h_en":"A Lesson in Israeli Culture","h_zh":"一堂以色列文化課",
    "paras":[
     ("Class 602 had an online exchange with <strong>Ofek–Giat Zeev School</strong> in Israel. After warming up with self-introductions at our first meeting, the Israeli students gave us a rich tour of their country — its <strong>food</strong>, its <strong>schools</strong>, its <strong>language</strong> and <strong>capital city</strong>, its <strong>inventions</strong>, and its famous people and singers. It felt like a whole lesson in Israeli culture.",
      "六年乙班與以色列 <strong>Ofek–Giat Zeev 學校</strong>進行了線上交流。第一次見面、以自我介紹暖身之後，以色列的小朋友詳細地向我們介紹了他們的<strong>食物</strong>、<strong>學校</strong>、<strong>語言</strong>與<strong>首都</strong>、<strong>發明</strong>，還有名人與歌手，讓我們上了豐富的一課以色列文化。")
    ]},
   {"h_en":"Joy and Peace, on the Recorder","h_zh":"用直笛吹出喜悅與和平",
    "paras":[
     ("In return, we performed something we had learned in music class — a <strong>Christmas song</strong> on the <strong>alto recorder</strong>.",
      "我們則向以色列的小朋友表演了在音樂課所學——用<strong>中音笛</strong>吹奏一首<strong>聖誕歌曲</strong>。"),
     ("In the warm, festive spirit of Christmas, we sent happiness, love, and peace all the way to the other side of the Earth.",
      "在聖誕歡樂的節慶氣氛裡，我們把快樂、喜悅、愛與和平，傳送到地球的另一端。")
    ]}
 ],
 "pullquote":{"en":"We sent joy, love, and peace across the Earth.","zh":"我們把喜悅、愛與和平，傳送到地球的另一端。"},
 "keywords":[
   {"w":"recorder","p":"n.","zh":"直笛","en":"We played a song on the recorder.","z":"我們用直笛吹了一首歌。"},
   {"w":"Christmas","p":"n.","zh":"聖誕節","en":"We played a Christmas song.","z":"我們吹奏了一首聖誕歌曲。"},
   {"w":"language","p":"n.","zh":"語言","en":"They taught us about their language.","z":"他們教我們認識他們的語言。"},
   {"w":"capital","p":"n.","zh":"首都","en":"They showed us their capital city.","z":"他們介紹了他們的首都。"},
   {"w":"invention","p":"n.","zh":"發明","en":"Israel has many famous inventions.","z":"以色列有許多著名的發明。"},
   {"w":"perform","p":"v.","zh":"表演","en":"We performed for our new friends.","z":"我們為新朋友表演。"},
   {"w":"peace","p":"n.","zh":"和平","en":"We send peace to the whole world.","z":"我們把和平送給全世界。"},
   {"w":"culture","p":"n.","zh":"文化","en":"We learned a lot about their culture.","z":"我們學到很多他們的文化。"}
 ],
 "dialogue":{"scene_en":"At Christmas, two students share songs and greetings.","scene_zh":"聖誕節時，兩位學生互相分享歌曲與問候。",
   "lines":[
     ("B","Merry Christmas! Tell us about your music class.","聖誕快樂！跟我們說說你們的音樂課。"),
     ("A","We are learning a Christmas song on the recorder.","我們正在用直笛學一首聖誕歌。"),
     ("B","Will you play it for us?","可以吹給我們聽嗎？"),
     ("A","Yes! Please listen carefully.","好！請仔細聽喔。"),
     ("B","That was beautiful. Thank you so much.","好好聽，太謝謝你了。"),
     ("A","We send you joy and peace from Taiwan.","我們從台灣送上喜悅與和平。")
   ]}
},

{
 "slug":"israel-language-swap", "flag":"🇮🇱",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2024-12-24","date_en":"December 24, 2024","date_zh":"2024 年 12 月 24 日",
 "klass":"Class 601 · 六年甲班","partner":"Bet Hinuch Shimon Peres–Rosh HaAyin, Israel · 以色列",
 "title":"Little Teachers<br>of Two Languages","title_zh":"互當小老師，教彼此的語言",
 "lede_en":"Meeting students from Israel for the first time, Class 601 took turns being little teachers — we taught everyday Chinese, they taught everyday Hebrew, and we introduced our small but charming school.",
 "lede_zh":"第一次見到以色列的學生，六年甲班輪流當起小老師——我們教日常中文，他們教日常希伯來文，還介紹了我們小而美的學校。",
 "media":{"type":"slideshow","n":7,
   "cap_en":"<b>Class 601 × Bet Hinuch Shimon Peres–Rosh HaAyin</b> · our first meeting with Israel","cap_zh":"六年甲班 × 以色列 Bet Hinuch Shimon Peres–Rosh HaAyin・第一次見面"},
 "body":[
   {"h_en":"Breaking the Ice","h_zh":"打破隔閡",
    "paras":[
     ("Class 601 had an online exchange with <strong>Bet Hinuch Shimon Peres–Rosh HaAyin</strong> in Israel. Since it was the first time the two schools had met, everyone began with a round of self-introductions to break the ice.",
      "六年甲班與以色列 <strong>Bet Hinuch Shimon Peres–Rosh HaAyin 學校</strong>進行了線上交流。這是雙方第一次見面，不能免俗地，每個人都先來一段自我介紹當作暖身。")
    ]},
   {"h_en":"Teaching Each Other","h_zh":"互相教學",
    "paras":[
     ("The highlight came next: we took turns being little teachers, each side teaching the other its own language. We taught the Israeli students some everyday <strong>Chinese</strong> phrases, and they taught us some everyday <strong>Hebrew</strong>.",
      "接下來是活動的高潮：我們互相當起小老師，教導對方自己的語言。我們教以色列的小朋友一些日常生活的<strong>中文</strong>用語，他們也教我們一些日常的<strong>希伯來文</strong>。"),
     ("To finish, we gave a polished presentation introducing KangLang — our small but charming school by the sea.",
      "最後，我們用一份精美的簡報，向以色列的小朋友介紹槺榔國小——這所小而美、靠近海邊的學校。")
    ]}
 ],
 "pullquote":{"en":"We took turns being little teachers of our own languages.","zh":"我們輪流當小老師，教彼此自己的語言。"},
 "keywords":[
   {"w":"introduce","p":"v.","zh":"介紹","en":"We introduced ourselves first.","z":"我們先自我介紹。"},
   {"w":"language","p":"n.","zh":"語言","en":"We taught each other our languages.","z":"我們互相教對方的語言。"},
   {"w":"teach","p":"v.","zh":"教","en":"We took turns to teach.","z":"我們輪流當老師教學。"},
   {"w":"Chinese","p":"n.","zh":"中文","en":"We taught them some Chinese phrases.","z":"我們教他們一些中文用語。"},
   {"w":"Hebrew","p":"n.","zh":"希伯來文","en":"They taught us some Hebrew.","z":"他們教我們一些希伯來文。"},
   {"w":"phrase","p":"n.","zh":"片語、用語","en":"We learned everyday phrases.","z":"我們學了日常用語。"},
   {"w":"presentation","p":"n.","zh":"簡報","en":"We gave a presentation about our school.","z":"我們做了一份介紹學校的簡報。"},
   {"w":"meet","p":"v.","zh":"見面","en":"It was the first time we met.","z":"這是我們第一次見面。"}
 ],
 "dialogue":{"scene_en":"At their first meeting, two students teach each other a word.","scene_zh":"第一次見面，兩位學生互相教對方一個字。",
   "lines":[
     ("A","Hi! In Chinese, hello is ni hao.","嗨！中文的「你好」就是 ni hao。"),
     ("B","Ni hao! Now you try Hebrew: shalom.","Ni hao！換你試試希伯來文：shalom。"),
     ("A","Shalom! Does it mean hello?","Shalom！它是「你好」的意思嗎？"),
     ("B","Yes, and it also means peace.","對，它也有「和平」的意思。"),
     ("A","I love learning your language!","我好喜歡學你們的語言！"),
     ("B","Me too. We are little teachers today.","我也是。我們今天都是小老師。")
   ]}
},

{
 "slug":"india-first-meet", "flag":"🇮🇳",
 "tag_en":"International Exchange","tag_zh":"國際交流",
 "date_iso":"2024-10-28","date_en":"October 28, 2024","date_zh":"2024 年 10 月 28 日",
 "klass":"Senior Grades · 高年級","partner":"An elementary school in India · 印度",
 "title":"Our Very First<br>Meeting with India","title_zh":"與印度的第一次相見",
 "lede_en":"After months of preparation, our long-awaited first exchange with India arrived. Two schools of children greeted each other warmly, and every English sentence we had practiced finally found its moment.",
 "lede_zh":"籌備已久，我們與印度的第一次交流終於登場。兩校的孩子熱情相見，那些練了又練的英文句子，總算派上了用場。",
 "media":{"type":"slideshow","n":8,
   "cap_en":"<b>KangLang × a school in India</b> · our very first international exchange","cap_zh":"槺榔國小 × 印度小學・我們的第一次國際交流"},
 "body":[
   {"h_en":"Months of Practice","h_zh":"練習了好幾個月",
    "paras":[
     ("After months of preparation, our long-awaited international exchange with an elementary school in India finally took place. Students from both schools greeted each other warmly and took turns introducing themselves. Through interactive conversation, our children had the perfect chance to put their English to real use.",
      "籌備已久，我們與印度一所小學的國際交流活動，今天終於登場。雙方的學生熱情相見，輪流介紹自己。透過互動式的對話，孩子們有機會把所學的英文真正派上用場。"),
     ("To get ready, the students had practiced for weeks — repeating each sentence over and over, carefully refining their pronunciation — all to present their very best to their new friends.",
      "為了今天，學生們練習已久，每一個句子一而再、再而三地複習練講，仔細打磨發音，只為把最好的一面呈現在對方眼前。")
    ]},
   {"h_en":"More Than a Class","h_zh":"不只是一堂課",
    "paras":[
     ("Everyone in the room was eager and full of energy, ready to take part and share.",
      "在場的每個人都摩拳擦掌、興奮極了，準備好參與、準備好分享。"),
     ("This was far more than an online class — it was a real, cross-cultural experience. Many students said afterward that they felt a strong sense of achievement.",
      "這不僅僅是一堂線上交流課，更是一次真實的跨國體驗。許多學生在活動後直呼：好有成就感！")
    ]}
 ],
 "pullquote":{"en":"Every sentence we practiced finally found its moment.","zh":"那些練了又練的句子，終於等到登場的這一刻。"},
 "keywords":[
   {"w":"prepare","p":"v.","zh":"準備","en":"We prepared for months.","z":"我們準備了好幾個月。"},
   {"w":"greet","p":"v.","zh":"打招呼","en":"Both schools greeted each other warmly.","z":"兩校熱情地互相問候。"},
   {"w":"introduce","p":"v.","zh":"介紹","en":"We took turns to introduce ourselves.","z":"我們輪流自我介紹。"},
   {"w":"practice","p":"v.","zh":"練習","en":"We practiced every sentence many times.","z":"每個句子我們都練了很多次。"},
   {"w":"pronunciation","p":"n.","zh":"發音","en":"We worked hard on our pronunciation.","z":"我們努力練習發音。"},
   {"w":"conversation","p":"n.","zh":"對話","en":"We had a real English conversation.","z":"我們進行了一場真正的英語對話。"},
   {"w":"achievement","p":"n.","zh":"成就感","en":"We felt a strong sense of achievement.","z":"我們有滿滿的成就感。"},
   {"w":"experience","p":"n.","zh":"體驗","en":"It was a real cross-cultural experience.","z":"這是一次真實的跨文化體驗。"}
 ],
 "dialogue":{"scene_en":"At the very first meeting, two students say hello.","scene_zh":"第一次見面，兩位學生互相打招呼。",
   "lines":[
     ("A","Hello! My name is Wei. Nice to meet you!","哈囉！我叫小維，很高興認識你！"),
     ("B","Hi Wei! I am Arjun, from India.","嗨小維！我是 Arjun，來自印度。"),
     ("A","We practiced English a lot for today.","為了今天，我們練了好多英文。"),
     ("B","You speak very well! I am happy to meet you.","你說得很好！很開心認識你。"),
     ("A","This is our first exchange. I feel proud!","這是我們第一次交流，我覺得好驕傲！"),
     ("B","Me too. Let us be good friends.","我也是。我們當好朋友吧。")
   ]}
},

]

# ------------------------------------------------------------------ TEMPLATES
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">')

def topbar(prefix, active):
    def cls(name): return ' class="is-active"' if name==active else ''
    return f'''<div class="topbar">
  <div class="wrap topbar-inner">
    <div class="topbar-brand">
      <div class="topbar-name">
        <a href="{prefix}" style="color:inherit;text-decoration:none;">
          KangLang Elementary
          <small>臺中市清水區槺榔國民小學</small>
        </a>
      </div>
    </div>
    <nav class="topbar-nav">
      <a href="{prefix}"{cls('home')}>Home</a>
      <a href="{prefix}principal/"{cls('principal')}>Principal</a>
      <a href="{prefix}news/"{cls('news')}>News</a>
      <a href="{prefix}international/"{cls('intl')}>International Education</a>
    </nav>
  </div>
</div>'''

FOOTER = '''<footer>
  <div class="wrap">
    <div>© 2026 臺中市清水區槺榔國民小學 · KangLang Elementary School</div>
    <div class="partner">Bilingual page by <a href="https://www.mycultureconnect.org/" target="_blank" rel="noopener">My Culture Connect 人師教育協會</a> &middot; provided free of charge</div>
  </div>
</footer>'''

def slideshow_html(slug, n, cap_en, cap_zh):
    slides=''.join(
        f'    <div class="slideshow__slide" aria-hidden="{"false" if i==1 else "true"}"><img src="photo_{i:02d}.jpg" alt="{slug} photo {i}" loading="{"eager" if i==1 else "lazy"}"></div>\n'
        for i in range(1,n+1))
    dots=''.join(
        f'<button class="slideshow__dot{" is-active" if i==1 else ""}" aria-label="Go to photo {i}"></button>'
        for i in range(1,n+1))
    return f'''<div class="slideshow" aria-label="Photo slideshow">
  <div class="slideshow__kicker">
    <span class="lbl">📸 Photo Story · 影像故事</span>
    <span class="slideshow__count"><b class="slideshow__cur">1</b> / {n}</span>
  </div>
  <div class="slideshow__viewport">
    <div class="slideshow__track">
{slides}    </div>
    <button class="slideshow__arrow slideshow__arrow--prev" aria-label="Previous photo">‹</button>
    <button class="slideshow__arrow slideshow__arrow--next" aria-label="Next photo">›</button>
  </div>
  <div class="slideshow__dots">{dots}</div>
  <p class="slideshow__cap">{cap_en}<br><span style="opacity:.85">{cap_zh}</span></p>
</div>'''

def video_html(yt, cap_en, cap_zh):
    return f'''<div class="intl-video">
  <div class="intl-video__frame">
    <iframe src="https://www.youtube-nocookie.com/embed/{yt}" title="KangLang International Education video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
  <p class="intl-video__cap">{cap_en}<br><span style="opacity:.85">{cap_zh}</span></p>
</div>'''

def body_html(body, pull):
    out=[]
    for sec in body:
        out.append('    <div class="body-text">')
        out.append(f'      <h3>{sec["h_en"]} <span class="zh">{sec["h_zh"]}</span></h3>')
        for en,zh in sec["paras"]:
            out.append(f'      <p>{en}</p>')
            out.append(f'      <p class="zh">{zh}</p>')
        out.append('    </div>')
    out.append('    <div class="pullquote">')
    out.append(f'      <p class="pullquote__text">&ldquo;{pull["en"]}&rdquo;</p>')
    out.append(f'      <p class="pullquote__zh">{pull["zh"]}</p>')
    out.append('    </div>')
    return '\n'.join(out)

def kw_html(keywords):
    cards=[]
    for i,k in enumerate(keywords,1):
        cards.append(f'''      <div class="kw">
        <div class="kw__top">
          <span class="kw__num">{i}</span>
          <div class="kw__word">
            <div class="kw__en">{k["w"]}<span class="kw__pos">({k["p"]})</span></div>
            <div class="kw__zh">{k["zh"]}</div>
          </div>
          <button class="speak" data-speak="{k["w"]}" aria-label="Listen to {k["w"]}">🔊</button>
        </div>
        <div class="kw__eg">
          <div class="kw__eg-txt">
            <div class="kw__eg-en">{k["en"]}</div>
            <div class="kw__eg-zh">{k["z"]}</div>
          </div>
          <button class="speak speak--sm" data-speak="{k["en"]}" aria-label="Listen to the sentence">🔊</button>
        </div>
      </div>''')
    return '\n'.join(cards)

def dlg_html(d):
    lines=[]
    for who,en,zh in d["lines"]:
        b=' b' if who=='B' else ''
        lines.append(f'''        <div class="line{b}" data-say="{en}">
          <div class="line__who">{who}</div>
          <div class="line__txt">
            <div class="line__en">{en}</div>
            <div class="line__zh">{zh}</div>
          </div>
          <button class="speak speak--sm" data-speak="{en}" aria-label="Listen to this line">🔊</button>
        </div>''')
    return '\n'.join(lines)

def story_nav(idx):
    # prev = newer (idx-1), next = older (idx+1)
    parts=['    <nav class="story-nav">']
    if idx>0:
        p=DATA[idx-1]
        parts.append(f'''      <a href="../{p["slug"]}/" class="prev">
        <div class="label">← Newer Report</div>
        <div class="title">{p["flag"]} {plain(p["title"])}</div>
        <div class="title-zh">{p["date_zh"]}</div>
      </a>''')
    else:
        parts.append('''      <a href="../" class="prev">
        <div class="label">← Back</div>
        <div class="title">All International Reports</div>
        <div class="title-zh">所有國際教育報導</div>
      </a>''')
    if idx<len(DATA)-1:
        nx=DATA[idx+1]
        parts.append(f'''      <a href="../{nx["slug"]}/" class="next">
        <div class="label">Older Report →</div>
        <div class="title">{nx["flag"]} {plain(nx["title"])}</div>
        <div class="title-zh">{nx["date_zh"]}</div>
      </a>''')
    else:
        parts.append('''      <a href="../" class="next">
        <div class="label">More →</div>
        <div class="title">All International Reports</div>
        <div class="title-zh">所有國際教育報導</div>
      </a>''')
    parts.append('    </nav>')
    return '\n'.join(parts)

def plain(title):
    return title.replace('<br>',' ')

def report_page(idx):
    d=DATA[idx]
    media = (slideshow_html(d["slug"], d["media"]["n"], d["media"]["cap_en"], d["media"]["cap_zh"])
             if d["media"]["type"]=="slideshow"
             else video_html(d["media"]["yt"], d["media"]["cap_en"], d["media"]["cap_zh"]))
    title_plain = plain(d["title"])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_plain} · {d["title_zh"]} — KangLang Elementary 槺榔國小</title>
<meta name="description" content="{d['lede_en']}">
<meta property="og:title" content="{title_plain} · {d['title_zh']}">
<meta property="og:description" content="{d['lede_en']}">
{'<meta property="og:image" content="photo_01.jpg">' if d["media"]["type"]=="slideshow" else ''}
<meta property="og:type" content="article">

{FONTS}

<link rel="stylesheet" href="../../assets/css/main.css">
<link rel="stylesheet" href="../../assets/css/news.css">
<link rel="stylesheet" href="../../assets/css/intl.css">
</head>
<body>

{topbar('../../','intl')}

<nav class="crumb">
  <div class="crumb__inner">
    <a href="../">← International Education · 國際教育</a>
  </div>
</nav>

<!-- ===== Story ===== -->
<article class="article">
  <div class="wrap-narrow">
    <div class="story-tag">{d['flag']} {d['tag_en']} · {d['tag_zh']}</div>
    <h1 class="story-title">{d['title']}</h1>
    <div class="story-title-zh">{d['title_zh']}</div>
    <div class="story-rule"></div>
    <div class="story-meta">
      <time datetime="{d['date_iso']}">{d['date_en']}</time>
      <span class="dot">·</span><span>{d['date_zh']}</span>
      <span class="dot">·</span><span>{d['klass']}</span>
      <span class="dot">·</span><span>{d['partner']}</span>
    </div>
    <p class="story-lede">{d['lede_en']}</p>
    <p class="story-lede-zh">{d['lede_zh']}</p>
  </div>

  <div class="wrap">
    {media}
  </div>

  <div class="wrap-narrow" style="margin-top:40px;">
{body_html(d['body'], d['pullquote'])}
  </div>
</article>

<!-- ===== Learning Zone ===== -->
<section class="lz">
  <div class="lz__inner">
    <span class="lz__eyebrow">📚 English Learning Zone</span>
    <h2 class="lz__title">Learn the Words from This Story</h2>
    <div class="lz__title-zh">英語學習區 · 從這篇報導學英文</div>
    <p class="lz__sub">Key words from the story, a sentence for each, and a short conversation to try out loud. Tap 🔊 to listen.<br><span style="color:var(--ink-soft)">關鍵字、每個字一個例句，還有一段可以唸出聲的對話。點 🔊 聽發音。</span></p>

    <div class="lz__sectlabel"><span class="num">1</span>Key Words</div>
    <div class="lz__sectlabel-zh">關鍵字 · 點 🔊 聽單字，再點小喇叭聽整句</div>
    <div class="kw-grid">
{kw_html(d['keywords'])}
    </div>

    <div class="lz__sectlabel"><span class="num">2</span>Try the Conversation</div>
    <div class="lz__sectlabel-zh">對話練習 · 兩個人一組，A 和 B 輪流唸</div>
    <div class="dlg-head">
      <button class="playall" id="playAll">▶ Play the whole conversation</button>
    </div>
    <div class="dlg-scene">🎬 <b>Scene</b> · {d['dialogue']['scene_en']}<br>情境：{d['dialogue']['scene_zh']}</div>
    <div class="dlg" id="dlg">
{dlg_html(d['dialogue'])}
    </div>

    <div class="lz__sectlabel"><span class="num">3</span>More Reports</div>
    <div class="lz__sectlabel-zh">看更多國際教育報導</div>
{story_nav(idx)}
  </div>
</section>

{FOOTER}

<script src="../../assets/js/news-speak.js"></script>
<script src="../../assets/js/intl-slideshow.js"></script>
</body>
</html>
'''

def hub_card(d):
    if d["media"]["type"]=="slideshow":
        img=f'<div class="news-card__img"><img src="{d["slug"]}/photo_01.jpg" alt="{plain(d["title"])}" loading="lazy"></div>'
    else:
        img='<div class="news-card__img news-card__img--video"><span class="play">▶</span></div>'
    return f'''      <a href="{d['slug']}/" class="news-card">
        {img}
        <div class="news-card__body">
          <div class="news-card__tag">{d['flag']} {d['tag_en']} · {d['tag_zh']}</div>
          <h3>{plain(d['title'])}<span class="zh">{d['title_zh']}</span></h3>
          <div class="news-card__date">{d['date_en']} · {d['date_zh']}</div>
          <p class="news-card__hook">{d['lede_en']}</p>
          <p class="news-card__hook-zh">{d['lede_zh']}</p>
          <span class="news-card__cta">Read the report</span>
        </div>
      </a>'''

def hub_page():
    # unique countries in chronological order of first appearance for the flag rail
    flags=[("🇮🇳","India · 印度"),("🇮🇱","Israel · 以色列"),("🇪🇸","Spain · 西班牙"),
           ("🇹🇷","Türkiye · 土耳其"),("🇯🇵","Japan · 日本"),("🇮🇩","Indonesia · 印尼"),
           ("🇻🇳","Vietnam · 越南"),("🇷🇺","Russia · 俄羅斯")]
    rail=''.join(f'<span class="flag"><span class="emoji">{e}</span>{n}</span>' for e,n in flags)
    cards='\n\n'.join(hub_card(d) for d in DATA)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>International Education · 國際教育 — KangLang Elementary 槺榔國小</title>
<meta name="description" content="KangLang Elementary's International Education program — online exchanges, postcards, and culture boxes with friends in India, Israel, Spain, Türkiye, Japan, Indonesia, Vietnam, and Russia. Each report has a photo slideshow and an English Learning Zone. 槺榔國小國際教育：與八個國家的線上交流、明信片與文化箱，每篇附影像輪播與英語學習區。">
<meta property="og:title" content="International Education · 國際教育 — KangLang Elementary">
<meta property="og:description" content="Meeting friends around the world, one country at a time. 一次認識一個國家的好朋友。">
<meta property="og:type" content="website">

{FONTS}

<link rel="stylesheet" href="../assets/css/main.css">
<link rel="stylesheet" href="../assets/css/news.css">
<link rel="stylesheet" href="../assets/css/intl.css">
</head>
<body>

{topbar('../','intl')}

<!-- ============ HERO ============ -->
<header class="news-hero">
  <div class="wrap">
    <span class="globe">🌏</span>
    <span class="eyebrow">Qingshui · Taichung · 國際教育</span>
    <h1>International Education
      <span class="zh">國際教育・和世界做朋友</span>
    </h1>
  </div>
</header>

<!-- ============ INTRO ============ -->
<section class="intro">
  <div class="wrap-narrow">
    <p class="lead">From video calls and handwritten postcards to culture boxes that travel across the sea &mdash; a small village school meeting the world, one country at a time.</p>
    <p class="lead-zh">從視訊連線、手寫明信片，到漂洋過海的文化箱——一所海邊的村落小學，一次認識一個國家的好朋友。每一篇報導下方都有「<strong>影像輪播</strong>」與「<strong>English Learning Zone 英語學習區</strong>」：關鍵字（點 🔊 聽發音）、例句，還有一段可以跟著唸的對話。</p>
    <div class="flag-rail">{rail}</div>
  </div>
</section>

<!-- ============ REPORTS GRID ============ -->
<section>
  <div class="wrap">
    <div class="news-grid">

{cards}

    </div>
  </div>
</section>

{FOOTER}

<script src="../assets/js/news-speak.js"></script>
</body>
</html>
'''

# ------------------------------------------------------------------ WRITE
def main():
    root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    intl=os.path.join(root,'international')
    # hub
    with open(os.path.join(intl,'index.html'),'w',encoding='utf-8') as f:
        f.write(hub_page())
    # reports
    for i,d in enumerate(DATA):
        folder=os.path.join(intl,d['slug']); os.makedirs(folder,exist_ok=True)
        with open(os.path.join(folder,'index.html'),'w',encoding='utf-8') as f:
            f.write(report_page(i))
    print(f'Wrote hub + {len(DATA)} reports to {intl}')

if __name__=='__main__':
    main()
