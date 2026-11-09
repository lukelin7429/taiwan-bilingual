# -*- coding: utf-8 -*-
"""Lesson content for Settle In Taiwan.

Pinyin is written by hand, one numbered syllable per Chinese character
(5 = neutral tone), using Taiwan readings and the tone changes of 一 and 不
as Taiwanese textbooks print them. build_content.py turns it into tone-marked
pinyin and zhuyin, and checks that every character has a syllable.

Phrase fields: zh, py, en, and optionally
  note  - a short usage tip (English)
  hv    - a Sino-Vietnamese link (English with Vietnamese), only where certain
"""

UNITS = [
    {
        "id": "hello",
        "emoji": "👋",
        "color": "#2f5d4f",
        "title": "Hello & Introductions",
        "zh": "打招呼",
        "intro": "Greet people, say who you are, and ask people to slow down.",
        "phrases": [
            {"zh": "你好", "py": "ni3 hao3", "en": "Hello."},
            {"zh": "早安", "py": "zao3 an1", "en": "Good morning."},
            {"zh": "謝謝", "py": "xie4 xie5", "en": "Thank you.",
             "hv": "Vietnamese cảm ơn comes from 感恩 (gǎn'ēn), \"to feel grateful.\""},
            {"zh": "不客氣", "py": "bu2 ke4 qi4", "en": "You're welcome."},
            {"zh": "不好意思", "py": "bu4 hao3 yi4 si5", "en": "Excuse me. / Sorry.",
             "note": "Used all the time: to get someone's attention, to squeeze past, or for a small apology."},
            {"zh": "對不起", "py": "dui4 bu5 qi3", "en": "I'm sorry.",
             "note": "A real apology. For small things, 不好意思 is more natural."},
            {"zh": "請問", "py": "qing3 wen4", "en": "Excuse me, may I ask…",
             "note": "Start any question to a stranger with 請問."},
            {"zh": "你叫什麼名字？", "py": "ni3 jiao4 shen2 me5 ming2 zi5", "en": "What's your name?"},
            {"zh": "我叫小玉。", "py": "wo3 jiao4 xiao3 yu4", "en": "My name is Xiao Yu.",
             "hv": "Ngọc is 玉 (yù, jade) in Chinese, so 小玉 is a friendly Chinese nickname for Ngoc."},
            {"zh": "我是越南人。", "py": "wo3 shi4 yue4 nan2 ren2", "en": "I'm Vietnamese.",
             "hv": "越南 = Việt Nam."},
            {"zh": "我是大學生。", "py": "wo3 shi4 da4 xue2 sheng1", "en": "I'm a college student.",
             "hv": "大學 = đại học."},
            {"zh": "我在銘傳大學讀書。", "py": "wo3 zai4 ming2 chuan2 da4 xue2 du2 shu1", "en": "I study at Ming Chuan University."},
            {"zh": "我會說一點中文。", "py": "wo3 hui4 shuo1 yi4 dian3 zhong1 wen2", "en": "I can speak a little Chinese.",
             "hv": "中文 = Trung văn."},
            {"zh": "請說慢一點。", "py": "qing3 shuo1 man4 yi4 dian3", "en": "Please speak a little more slowly."},
            {"zh": "很高興認識你。", "py": "hen3 gao1 xing4 ren4 shi4 ni3", "en": "Nice to meet you."},
            {"zh": "再見", "py": "zai4 jian4", "en": "Goodbye.", "hv": "再見 = tái kiến."},
        ],
        "signs": [
            {"zh": "男", "py": "nan2", "en": "Men's restroom"},
            {"zh": "女", "py": "nv3", "en": "Women's restroom"},
            {"zh": "禁止吸菸", "py": "jin4 zhi3 xi1 yan1", "en": "No smoking"},
        ],
        "dialogue": {
            "title": "Meeting a classmate",
            "cast": {"A": "阿明 (a Taiwanese student)", "B": "阿玲 (a new student from Vietnam)"},
            "lines": [
                ["A", "你好！你是新同學嗎？", "ni3 hao3 ni3 shi4 xin1 tong2 xue2 ma5", "Hi! Are you a new classmate?"],
                ["B", "對，我叫阿玲。", "dui4 wo3 jiao4 a1 ling2", "Yes, my name is A-Ling."],
                ["A", "你從哪裡來？", "ni3 cong2 na3 li3 lai2", "Where are you from?"],
                ["B", "我從越南來。", "wo3 cong2 yue4 nan2 lai2", "I'm from Vietnam."],
                ["A", "你的中文很好！", "ni3 de5 zhong1 wen2 hen3 hao3", "Your Chinese is very good!"],
                ["B", "謝謝！我會說一點中文。請說慢一點。", "xie4 xie5 wo3 hui4 shuo1 yi4 dian3 zhong1 wen2 qing3 shuo1 man4 yi4 dian3", "Thanks! I can speak a little Chinese. Please speak more slowly."],
                ["A", "好！我叫阿明。很高興認識你。", "hao3 wo3 jiao4 a1 ming2 hen3 gao1 xing4 ren4 shi4 ni3", "Sure! I'm A-Ming. Nice to meet you."],
                ["B", "我也很高興認識你。", "wo3 ye3 hen3 gao1 xing4 ren4 shi4 ni3", "Nice to meet you, too."],
            ],
            "quiz": [
                {"q": "Where is A-Ling from?", "a": "Vietnam", "wrong": ["Taiwan", "Japan", "Thailand"]},
                {"q": "What does A-Ling ask A-Ming to do?", "a": "Speak more slowly", "wrong": ["Speak louder", "Write it down", "Speak English"]},
                {"q": "Who is the new classmate?", "a": "A-Ling", "wrong": ["A-Ming", "Both of them", "Neither of them"]},
            ],
        },
        "write": ["你", "好", "我", "人", "大", "中", "男", "女"],
        "culture": [
            ["Family name first", "Chinese names put the family name first, just like Vietnamese names. In 林小玉, the family name is 林 (Lín)."],
            ["不好意思 is everywhere", "Taiwanese people say 不好意思 to get attention, to pass someone, or to soften a request. It is polite, not a big apology."],
            ["\"Have you eaten?\"", "Older people may greet you with 你吃飽了嗎？ (\"Have you eaten?\"). It just means hello. Answer 吃飽了 (\"I have\") with a smile."],
            ["Teachers", "Call teachers 老師 (lǎoshī), even outside class: 林老師, 王老師."],
        ],
    },
    {
        "id": "store",
        "emoji": "🏪",
        "color": "#c0572b",
        "title": "Convenience Store",
        "zh": "便利商店",
        "intro": "Pay, heat up food, use your EasyCard, and answer the questions clerks always ask.",
        "hv": "便利 = tiện lợi, so 便利商店 is literally a \"tiện lợi\" store.",
        "phrases": [
            {"zh": "歡迎光臨！", "py": "huan1 ying2 guang1 lin2", "en": "Welcome!",
             "note": "Clerks say this every time the door opens. You don't need to answer.",
             "hv": "歡迎 = hoan nghênh."},
            {"zh": "要袋子嗎？", "py": "yao4 dai4 zi5 ma5", "en": "Do you need a bag?",
             "note": "Plastic bags are not free in Taiwan, so clerks always ask."},
            {"zh": "不用，謝謝。", "py": "bu2 yong4 xie4 xie5", "en": "No, thank you."},
            {"zh": "好，要一個。", "py": "hao3 yao4 yi2 ge5", "en": "Yes, one please."},
            {"zh": "有載具嗎？", "py": "you3 zai4 ju4 ma5", "en": "Do you have an e-receipt barcode?",
             "note": "A 載具 is a barcode on your phone that saves your receipts. If you don't have one, just say 沒有 (méiyǒu)."},
            {"zh": "沒有。", "py": "mei2 you3", "en": "No, I don't."},
            {"zh": "要加熱嗎？", "py": "yao4 jia1 re4 ma5", "en": "Do you want it heated up?"},
            {"zh": "好，麻煩你。", "py": "hao3 ma2 fan2 ni3", "en": "Yes, please.",
             "note": "麻煩你 (\"sorry to trouble you\") is a polite way to say yes, please."},
            {"zh": "這個多少錢？", "py": "zhe4 ge5 duo1 shao3 qian2", "en": "How much is this?"},
            {"zh": "一共多少錢？", "py": "yi2 gong4 duo1 shao3 qian2", "en": "How much is it altogether?"},
            {"zh": "一百二十五元。", "py": "yi4 bai3 er4 shi2 wu3 yuan2", "en": "125 dollars (NT$125)."},
            {"zh": "可以用悠遊卡嗎？", "py": "ke3 yi3 yong4 you1 you2 ka3 ma5", "en": "Can I use my EasyCard?"},
            {"zh": "可以刷卡嗎？", "py": "ke3 yi3 shua1 ka3 ma5", "en": "Can I pay by credit card?"},
            {"zh": "請問有賣雨傘嗎？", "py": "qing3 wen4 you3 mai4 yu3 san3 ma5", "en": "Excuse me, do you sell umbrellas?"},
            {"zh": "廁所在哪裡？", "py": "ce4 suo3 zai4 na3 li3", "en": "Where is the restroom?"},
        ],
        "signs": [
            {"zh": "出口", "py": "chu1 kou3", "en": "Exit"},
            {"zh": "入口", "py": "ru4 kou3", "en": "Entrance"},
            {"zh": "推", "py": "tui1", "en": "Push (on doors)"},
            {"zh": "拉", "py": "la1", "en": "Pull (on doors)"},
            {"zh": "廁所", "py": "ce4 suo3", "en": "Restroom"},
        ],
        "dialogue": {
            "title": "Buying lunch at the store",
            "cast": {"A": "店員 (the clerk)", "B": "客人 (a customer)"},
            "lines": [
                ["A", "歡迎光臨！", "huan1 ying2 guang1 lin2", "Welcome!"],
                ["B", "你好，這個便當可以加熱嗎？", "ni3 hao3 zhe4 ge5 bian4 dang1 ke3 yi3 jia1 re4 ma5", "Hi, can you heat up this lunch box?"],
                ["A", "可以。要袋子嗎？", "ke3 yi3 yao4 dai4 zi5 ma5", "Sure. Do you need a bag?"],
                ["B", "不用，謝謝。可以用悠遊卡嗎？", "bu2 yong4 xie4 xie5 ke3 yi3 yong4 you1 you2 ka3 ma5", "No, thanks. Can I use my EasyCard?"],
                ["A", "可以。一共八十九元。有載具嗎？", "ke3 yi3 yi2 gong4 ba1 shi2 jiu3 yuan2 you3 zai4 ju4 ma5", "Yes. That's 89 dollars. Do you have an e-receipt barcode?"],
                ["B", "沒有。", "mei2 you3", "No, I don't."],
                ["A", "好，謝謝光臨！", "hao3 xie4 xie5 guang1 lin2", "OK, thanks for coming!"],
            ],
            "quiz": [
                {"q": "What does the customer buy?", "a": "A lunch box", "wrong": ["A drink", "An umbrella", "A rice ball"]},
                {"q": "Does the customer take a bag?", "a": "No", "wrong": ["Yes, one bag", "Yes, two bags", "The clerk doesn't ask"]},
                {"q": "How does the customer pay?", "a": "With an EasyCard", "wrong": ["In cash", "With a credit card", "With a phone app"]},
                {"q": "How much is it?", "a": "NT$89", "wrong": ["NT$98", "NT$69", "NT$125"]},
            ],
        },
        "write": ["出", "入", "口", "錢", "元", "卡", "推", "拉"],
        "culture": [
            ["More than a store", "At 7-Eleven (people call it 小七, Xiǎo Qī, \"Little Seven\") and FamilyMart (全家, Quánjiā) you can pay bills, print documents, buy train tickets, and pick up online orders."],
            ["Every receipt is a lottery ticket", "Taiwan's receipts (發票, fāpiào) have a lottery number. Prizes are drawn every two months, on the 25th of odd-numbered months. Keep your receipts!"],
            ["The e-receipt barcode", "A 載具 saves your receipts on your phone, so you don't lose the lottery numbers. You can set one up in the Ministry of Finance e-invoice app."],
            ["The EasyCard", "The 悠遊卡 (yōuyóukǎ) works on the MRT, buses, YouBike, and in most convenience stores. You can add money at the store counter."],
        ],
    },
    {
        "id": "food",
        "emoji": "🧋",
        "color": "#7a4fa3",
        "title": "Night Markets & Bubble Tea",
        "zh": "吃東西",
        "intro": "Order street food, say no to spicy or cilantro, and order bubble tea just the way you like it.",
        "phrases": [
            {"zh": "老闆，我要這個。", "py": "lao3 ban3 wo3 yao4 zhe4 ge5", "en": "Excuse me (boss), I'd like this one.",
             "note": "Call any food vendor 老闆 (\"boss\"). It is friendly and normal."},
            {"zh": "一份多少錢？", "py": "yi2 fen4 duo1 shao3 qian2", "en": "How much is one serving?"},
            {"zh": "內用還是外帶？", "py": "nei4 yong4 hai2 shi4 wai4 dai4", "en": "For here or to go?"},
            {"zh": "外帶，謝謝。", "py": "wai4 dai4 xie4 xie5", "en": "To go, thanks."},
            {"zh": "有菜單嗎？", "py": "you3 cai4 dan1 ma5", "en": "Do you have a menu?"},
            {"zh": "不要辣。", "py": "bu2 yao4 la4", "en": "Not spicy, please."},
            {"zh": "小辣就好。", "py": "xiao3 la4 jiu4 hao3", "en": "Just a little spicy."},
            {"zh": "不要香菜。", "py": "bu2 yao4 xiang1 cai4", "en": "No cilantro, please."},
            {"zh": "我吃素。", "py": "wo3 chi1 su4", "en": "I'm vegetarian."},
            {"zh": "我要一杯珍珠奶茶。", "py": "wo3 yao4 yi4 bei1 zhen1 zhu1 nai3 cha2", "en": "I'd like a bubble tea.",
             "hv": "珍珠 = trân châu and 茶 = trà, just like trà sữa trân châu."},
            {"zh": "甜度冰塊呢？", "py": "tian2 du4 bing1 kuai4 ne5", "en": "How sweet, and how much ice?"},
            {"zh": "半糖少冰。", "py": "ban4 tang2 shao3 bing1", "en": "Half sugar, less ice."},
            {"zh": "微糖去冰。", "py": "wei2 tang2 qu4 bing1", "en": "A little sugar, no ice.",
             "note": "In Taiwan 微 is read wéi (rising tone)."},
            {"zh": "好吃！", "py": "hao3 chi1", "en": "Delicious!"},
            {"zh": "可以結帳嗎？", "py": "ke3 yi3 jie2 zhang4 ma5", "en": "Can I pay now? / The check, please."},
        ],
        "signs": [
            {"zh": "營業中", "py": "ying2 ye4 zhong1", "en": "Open"},
            {"zh": "休息中", "py": "xiu1 xi2 zhong1", "en": "Closed (taking a break)"},
            {"zh": "只收現金", "py": "zhi3 shou1 xian4 jin1", "en": "Cash only"},
            {"zh": "排隊", "py": "pai2 dui4", "en": "Line up here"},
        ],
        "dialogue": {
            "title": "Ordering bubble tea",
            "cast": {"A": "店員 (the shop clerk)", "B": "客人 (a customer)"},
            "lines": [
                ["A", "你好，要喝什麼？", "ni3 hao3 yao4 he1 shen2 me5", "Hi, what would you like to drink?"],
                ["B", "我要一杯珍珠奶茶。", "wo3 yao4 yi4 bei1 zhen1 zhu1 nai3 cha2", "I'd like a bubble tea."],
                ["A", "大杯還是中杯？", "da4 bei1 hai2 shi4 zhong1 bei1", "Large or medium?"],
                ["B", "大杯。", "da4 bei1", "Large."],
                ["A", "甜度冰塊呢？", "tian2 du4 bing1 kuai4 ne5", "How sweet, and how much ice?"],
                ["B", "半糖少冰。", "ban4 tang2 shao3 bing1", "Half sugar, less ice."],
                ["A", "內用還是外帶？", "nei4 yong4 hai2 shi4 wai4 dai4", "For here or to go?"],
                ["B", "外帶，謝謝。", "wai4 dai4 xie4 xie5", "To go, thanks."],
                ["A", "好，六十五元。", "hao3 liu4 shi2 wu3 yuan2", "OK, that's 65 dollars."],
            ],
            "quiz": [
                {"q": "What size does the customer order?", "a": "Large", "wrong": ["Medium", "Small", "Two cups"]},
                {"q": "How sweet is the drink?", "a": "Half sugar", "wrong": ["No sugar", "Full sugar", "A little sugar"]},
                {"q": "How much ice?", "a": "Less ice", "wrong": ["No ice", "Regular ice", "Hot, no ice"]},
                {"q": "How much does it cost?", "a": "NT$65", "wrong": ["NT$56", "NT$75", "NT$60"]},
            ],
        },
        "write": ["吃", "喝", "茶", "冰", "糖", "辣", "菜", "素"],
        "culture": [
            ["Choose your sweetness", "Drink shops ask 甜度 (sweetness): 全糖 full, 少糖 less, 半糖 half, 微糖 a little, 無糖 none. And 冰塊 (ice): 正常冰 regular, 少冰 less, 微冰 a little, 去冰 none, 熱 hot."],
            ["Night markets", "At night market stalls you usually order and pay first, and many take cash only. Carry some NT$100 bills and coins."],
            ["Vegetarian food", "Vegetarian (素食, sùshí) restaurants are easy to find. Look for the character 素 on the sign."],
            ["A taste of home", "Look for 越南河粉 (Yuènán héfěn, Vietnamese pho). Many Taiwanese people love it, and Vietnamese restaurants are in many neighborhoods."],
            ["No tipping", "Tipping is not expected in Taiwan. Some sit-down restaurants add a 10% service charge to the bill."],
        ],
    },
]

# The other eight units are in content_more.py.
from content_more import MORE  # noqa: E402

UNITS += MORE
ORDER = ["hello", "numbers", "store", "food", "transit", "campus", "health", "home", "customs", "places", "classroom"]
UNITS.sort(key=lambda u: ORDER.index(u["id"]))

# Units planned for later, shown on the home screen as "coming soon".
COMING = []
