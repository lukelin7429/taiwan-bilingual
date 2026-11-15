# -*- coding: utf-8 -*-
"""Story passages: one short first-person paragraph per unit, told by 小玉.

Added after Ngoc's feedback (November 2026): she learns best by memorizing a
whole connected paragraph rather than short dialogue lines. Each sentence is
[zh, py, en]; pinyin follows the same rules as content_src.py.
"""

STORIES = {
    "hello": {
        "title": "My first day", "zh": "我的第一天",
        "lines": [
            ["大家好，我叫小玉。", "da4 jia1 hao3 wo3 jiao4 xiao3 yu4", "Hello, everyone. My name is Xiao Yu."],
            ["我是越南人，也是大學生。", "wo3 shi4 yue4 nan2 ren2 ye3 shi4 da4 xue2 sheng1", "I'm Vietnamese, and I'm a college student."],
            ["我在銘傳大學讀書。", "wo3 zai4 ming2 chuan2 da4 xue2 du2 shu1", "I study at Ming Chuan University."],
            ["我會說一點中文，可是說得不快。", "wo3 hui4 shuo1 yi4 dian3 zhong1 wen2 ke3 shi4 shuo1 de5 bu2 kuai4", "I can speak a little Chinese, but not very fast."],
            ["所以我常常說：「請說慢一點。」", "suo3 yi3 wo3 chang2 chang2 shuo1 qing3 shuo1 man4 yi4 dian3", "So I often say, \"Please speak a little more slowly.\""],
            ["台灣人都很友善，也很有耐心。", "tai2 wan1 ren2 dou1 hen3 you3 shan4 ye3 hen3 you3 nai4 xin1", "People in Taiwan are friendly and very patient."],
            ["今天我認識了很多新同學。", "jin1 tian1 wo3 ren4 shi4 le5 hen3 duo1 xin1 tong2 xue2", "Today I met a lot of new classmates."],
            ["很高興認識你們！", "hen3 gao1 xing4 ren4 shi4 ni3 men5", "I'm so glad to meet you all!"],
        ],
    },
    "numbers": {
        "title": "My Friday", "zh": "我的星期五",
        "lines": [
            ["今天星期五，我早上八點起床。", "jin1 tian1 xing1 qi2 wu3 wo3 zao3 shang4 ba1 dian3 qi3 chuang2", "Today is Friday. I got up at eight in the morning."],
            ["九點半有中文課，十二點下課。", "jiu3 dian3 ban4 you3 zhong1 wen2 ke4 shi2 er4 dian3 xia4 ke4", "I had Chinese class at nine thirty, and class ended at twelve."],
            ["下午我跟朋友去看電影。", "xia4 wu3 wo3 gen1 peng2 you3 qu4 kan4 dian4 ying3", "In the afternoon I went to a movie with a friend."],
            ["電影票一張兩百八十元。", "dian4 ying3 piao4 yi4 zhang1 liang3 bai3 ba1 shi2 yuan2", "A movie ticket was 280 dollars."],
            ["看完電影，我們去買衣服。", "kan4 wan2 dian4 ying3 wo3 men5 qu4 mai3 yi1 fu2", "After the movie, we went shopping for clothes."],
            ["一件外套要一千兩百元，太貴了！", "yi2 jian4 wai4 tao4 yao4 yi4 qian1 liang3 bai3 yuan2 tai4 gui4 le5", "A jacket cost 1,200 dollars. Too expensive!"],
            ["我問老闆：「可以便宜一點嗎？」", "wo3 wen4 lao3 ban3 ke3 yi3 pian2 yi2 yi4 dian3 ma5", "I asked the owner, \"Can you make it a little cheaper?\""],
            ["老闆說：「好，算你一千元。」", "lao3 ban3 shuo1 hao3 suan4 ni3 yi4 qian1 yuan2", "The owner said, \"OK, a thousand for you.\""],
        ],
    },
    "store": {
        "title": "The store next door", "zh": "我家旁邊的便利商店",
        "lines": [
            ["我家旁邊有一家便利商店。", "wo3 jia1 pang2 bian1 you3 yi4 jia1 bian4 li4 shang1 dian4", "There's a convenience store next to my home."],
            ["我每天都去那裡買早餐。", "wo3 mei3 tian1 dou1 qu4 na4 li3 mai3 zao3 can1", "I go there every day to buy breakfast."],
            ["店員總是說：「歡迎光臨！」", "dian4 yuan2 zong3 shi4 shuo1 huan1 ying2 guang1 lin2", "The clerk always says, \"Welcome!\""],
            ["我買了一個便當，請他幫我加熱。", "wo3 mai3 le5 yi2 ge5 bian4 dang1 qing3 ta1 bang1 wo3 jia1 re4", "I bought a lunch box and asked him to heat it up."],
            ["他問我要不要袋子，我說：「不用，謝謝。」", "ta1 wen4 wo3 yao4 bu2 yao4 dai4 zi5 wo3 shuo1 bu2 yong4 xie4 xie5", "He asked if I wanted a bag. I said, \"No, thank you.\""],
            ["一共八十九元，我用悠遊卡付錢。", "yi2 gong4 ba1 shi2 jiu3 yuan2 wo3 yong4 you1 you2 ka3 fu4 qian2", "It was 89 dollars in all, and I paid with my EasyCard."],
            ["在台灣，便利商店也可以繳費、寄包裹。", "zai4 tai2 wan1 bian4 li4 shang1 dian4 ye3 ke3 yi3 jiao3 fei4 ji4 bao1 guo3", "In Taiwan, you can also pay bills and send packages at convenience stores."],
            ["真的很方便！", "zhen1 de5 hen3 fang1 bian4", "It's really convenient!"],
        ],
    },
    "food": {
        "title": "A night at the market", "zh": "逛夜市",
        "lines": [
            ["星期六晚上，我跟朋友去逛夜市。", "xing1 qi2 liu4 wan3 shang4 wo3 gen1 peng2 you3 qu4 guang4 ye4 shi4", "On Saturday night, I went to the night market with friends."],
            ["夜市人很多，也很熱鬧。", "ye4 shi4 ren2 hen3 duo1 ye3 hen3 re4 nao4", "The night market was crowded and lively."],
            ["我先買了一份臭豆腐。", "wo3 xian1 mai3 le5 yi2 fen4 chou4 dou4 fu5", "First I bought a plate of stinky tofu."],
            ["我跟老闆說：「不要辣，不要香菜。」", "wo3 gen1 lao3 ban3 shuo1 bu2 yao4 la4 bu2 yao4 xiang1 cai4", "I told the owner, \"Not spicy, and no cilantro.\""],
            ["然後我買了一杯珍珠奶茶。", "ran2 hou4 wo3 mai3 le5 yi4 bei1 zhen1 zhu1 nai3 cha2", "Then I bought a bubble tea."],
            ["我說：「半糖少冰，外帶，謝謝。」", "wo3 shuo1 ban4 tang2 shao3 bing1 wai4 dai4 xie4 xie5", "I said, \"Half sugar, less ice, to go, thanks.\""],
            ["台灣的小吃又便宜又好吃。", "tai2 wan1 de5 xiao3 chi1 you4 pian2 yi2 you4 hao3 chi1", "Taiwanese snacks are cheap and delicious."],
            ["我下個星期還要再來！", "wo3 xia4 ge5 xing1 qi2 hai2 yao4 zai4 lai2", "I'm coming back next week!"],
        ],
    },
    "transit": {
        "title": "Sunset in Tamsui", "zh": "去淡水看夕陽",
        "lines": [
            ["今天我要去淡水看夕陽。", "jin1 tian1 wo3 yao4 qu4 dan4 shui3 kan4 xi4 yang2", "Today I'm going to Tamsui to watch the sunset."],
            ["可是我不知道捷運站在哪裡。", "ke3 shi4 wo3 bu4 zhi1 dao4 jie2 yun4 zhan4 zai4 na3 li3", "But I didn't know where the MRT station was."],
            ["我問路人：「請問，捷運站在哪裡？」", "wo3 wen4 lu4 ren2 qing3 wen4 jie2 yun4 zhan4 zai4 na3 li3", "I asked someone, \"Excuse me, where is the MRT station?\""],
            ["她說：「往前直走，在紅綠燈右轉。」", "ta1 shuo1 wang3 qian2 zhi2 zou3 zai4 hong2 lv4 deng1 you4 zhuan3", "She said, \"Go straight ahead and turn right at the traffic light.\""],
            ["走路大概五分鐘就到了。", "zou3 lu4 da4 gai4 wu3 fen1 zhong1 jiu4 dao4 le5", "It was only about a five-minute walk."],
            ["我坐紅線，不用換車。", "wo3 zuo4 hong2 xian4 bu2 yong4 huan4 che1", "I took the Red Line and didn't need to change trains."],
            ["在捷運上不可以吃東西，也不可以喝水。", "zai4 jie2 yun4 shang4 bu4 ke3 yi3 chi1 dong1 xi1 ye3 bu4 ke3 yi3 he1 shui3", "On the MRT you can't eat, and you can't drink water either."],
            ["淡水的夕陽好漂亮！", "dan4 shui3 de5 xi4 yang2 hao3 piao4 liang4", "The sunset in Tamsui is so beautiful!"],
        ],
    },
    "campus": {
        "title": "My college life", "zh": "我的大學生活",
        "lines": [
            ["我每天早上都有中文課。", "wo3 mei3 tian1 zao3 shang4 dou1 you3 zhong1 wen2 ke4", "I have Chinese class every morning."],
            ["老師說話很快，有時候我聽不懂。", "lao3 shi1 shuo1 hua4 hen3 kuai4 you3 shi2 hou4 wo3 ting1 bu4 dong3", "The teacher speaks fast, and sometimes I don't understand."],
            ["我就舉手問：「可以再說一次嗎？」", "wo3 jiu4 ju3 shou3 wen4 ke3 yi3 zai4 shuo1 yi2 ci4 ma5", "Then I raise my hand and ask, \"Could you say that again?\""],
            ["下課以後，我跟同學一起吃午餐。", "xia4 ke4 yi3 hou4 wo3 gen1 tong2 xue2 yi4 qi3 chi1 wu3 can1", "After class, I have lunch with my classmates."],
            ["學生餐廳的菜很便宜。", "xue2 sheng1 can1 ting1 de5 cai4 hen3 pian2 yi2", "The food in the student cafeteria is cheap."],
            ["下午我們去圖書館寫作業。", "xia4 wu3 wo3 men5 qu4 tu2 shu1 guan3 xie3 zuo4 ye4", "In the afternoon we go to the library to do homework."],
            ["下禮拜要考試，大家都很認真。", "xia4 li3 bai4 yao4 kao3 shi4 da4 jia1 dou1 hen3 ren4 zhen1", "We have a test next week, so everyone is working hard."],
            ["我們互相說：「加油！」", "wo3 men5 hu4 xiang1 shuo1 jia1 you2", "We tell each other, \"You can do it!\""],
        ],
    },
    "health": {
        "title": "I got sick", "zh": "我生病了",
        "lines": [
            ["昨天晚上我發燒了，喉嚨也很痛。", "zuo2 tian1 wan3 shang4 wo3 fa1 shao1 le5 hou2 long2 ye3 hen3 tong4", "Last night I had a fever, and my throat hurt a lot."],
            ["今天早上，我去附近的診所看醫生。", "jin1 tian1 zao3 shang4 wo3 qu4 fu4 jin4 de5 zhen3 suo3 kan4 yi1 sheng1", "This morning I went to a clinic nearby to see a doctor."],
            ["我跟護士說：「我要掛號。這是我的健保卡。」", "wo3 gen1 hu4 shi4 shuo1 wo3 yao4 gua4 hao4 zhe4 shi4 wo3 de5 jian4 bao3 ka3", "I told the nurse, \"I'd like to register. Here is my health insurance card.\""],
            ["醫生問我對什麼藥過敏，我說沒有。", "yi1 sheng1 wen4 wo3 dui4 shen2 me5 yao4 guo4 min3 wo3 shuo1 mei2 you3", "The doctor asked if I was allergic to any medicine. I said no."],
            ["他說我感冒了，要多喝水，多休息。", "ta1 shuo1 wo3 gan3 mao4 le5 yao4 duo1 he1 shui3 duo1 xiu1 xi2", "He said I had a cold and should drink plenty of water and rest."],
            ["這個藥一天吃三次，飯後吃。", "zhe4 ge5 yao4 yi4 tian1 chi1 san1 ci4 fan4 hou4 chi1", "This medicine is taken three times a day, after meals."],
            ["有健保，看醫生不會很貴。", "you3 jian4 bao3 kan4 yi1 sheng1 bu2 hui4 hen3 gui4", "With health insurance, seeing a doctor isn't expensive."],
            ["休息兩天以後，我就好了。", "xiu1 xi2 liang3 tian1 yi3 hou4 wo3 jiu4 hao3 le5", "After two days of rest, I was well again."],
        ],
    },
    "home": {
        "title": "My new home", "zh": "我的新家",
        "lines": [
            ["我在學校附近租了一個小房間。", "wo3 zai4 xue2 xiao4 fu4 jin4 zu1 le5 yi2 ge5 xiao3 fang2 jian1", "I rented a small room near school."],
            ["房租每個月五號付。", "fang2 zu1 mei3 ge5 yue4 wu3 hao4 fu4", "The rent is due on the fifth of every month."],
            ["在台灣，垃圾不可以放在路邊。", "zai4 tai2 wan1 le4 se4 bu4 ke3 yi3 fang4 zai4 lu4 bian1", "In Taiwan, you can't leave trash on the street."],
            ["每天晚上七點半，垃圾車會來。", "mei3 tian1 wan3 shang4 qi1 dian3 ban4 le4 se4 che1 hui4 lai2", "Every evening at seven thirty, the garbage truck comes."],
            ["聽到音樂，我就拿垃圾出去倒。", "ting1 dao4 yin1 yue4 wo3 jiu4 na2 le4 se4 chu1 qu4 dao4", "When I hear the music, I take the trash out."],
            ["紙、瓶子、廚餘都要分開。", "zhi3 ping2 zi5 chu2 yu2 dou1 yao4 fen1 kai1", "Paper, bottles, and food scraps all have to be sorted."],
            ["上個星期熱水器壞了，我打電話給房東。", "shang4 ge5 xing1 qi2 re4 shui3 qi4 huai4 le5 wo3 da3 dian4 hua4 gei3 fang2 dong1", "Last week the water heater broke, so I called my landlord."],
            ["他第二天就找人來修，真好！", "ta1 di4 er4 tian1 jiu4 zhao3 ren2 lai2 xiu1 zhen1 hao3", "He had someone fix it the very next day. How nice!"],
        ],
    },
    "customs": {
        "title": "New Year in Taiwan", "zh": "在台灣過年",
        "lines": [
            ["今年我第一次在台灣過年。", "jin1 nian2 wo3 di4 yi1 ci4 zai4 tai2 wan1 guo4 nian2", "This year I celebrated Lunar New Year in Taiwan for the first time."],
            ["同學請我去她家吃年夜飯。", "tong2 xue2 qing3 wo3 qu4 ta1 jia1 chi1 nian2 ye4 fan4", "A classmate invited me to her home for New Year's Eve dinner."],
            ["我帶了一盒鳳梨酥，說：「這是一點小心意。」", "wo3 dai4 le5 yi4 he2 feng4 li2 su1 shuo1 zhe4 shi4 yi4 dian3 xiao3 xin1 yi4", "I brought a box of pineapple cakes and said, \"This is a little something for you.\""],
            ["她媽媽說：「你太客氣了！」", "ta1 ma1 ma5 shuo1 ni3 tai4 ke4 qi4 le5", "Her mother said, \"You're too kind!\""],
            ["進門以前，我先脫鞋。", "jin4 men2 yi3 qian2 wo3 xian1 tuo1 xie2", "Before going in, I took off my shoes."],
            ["吃飯的時候，大家一起說：「新年快樂！」", "chi1 fan4 de5 shi2 hou4 da4 jia1 yi4 qi3 shuo1 xin1 nian2 kuai4 le4", "At dinner, everyone said together, \"Happy New Year!\""],
            ["越南也過農曆新年，也發紅包。", "yue4 nan2 ye3 guo4 nong2 li4 xin1 nian2 ye3 fa1 hong2 bao1", "Vietnam celebrates Lunar New Year too, and we also give red envelopes."],
            ["所以在台灣過年，我覺得很像在家裡。", "suo3 yi3 zai4 tai2 wan1 guo4 nian2 wo3 jue2 de5 hen3 xiang4 zai4 jia1 li3", "So New Year in Taiwan felt a lot like being at home."],
        ],
    },
    "places": {
        "title": "A trip to Jiufen", "zh": "去九份玩",
        "lines": [
            ["上個週末，我跟朋友去九份玩。", "shang4 ge5 zhou1 mo4 wo3 gen1 peng2 you3 qu4 jiu3 fen4 wan2", "Last weekend, I went to Jiufen with friends."],
            ["我們先坐火車到瑞芳，再坐公車上山。", "wo3 men5 xian1 zuo4 huo3 che1 dao4 rui4 fang1 zai4 zuo4 gong1 che1 shang4 shan1", "We took the train to Ruifang, then a bus up the mountain."],
            ["週末人很多，所以我們早一點出發。", "zhou1 mo4 ren2 hen3 duo1 suo3 yi3 wo3 men5 zao3 yi4 dian3 chu1 fa1", "It's crowded on weekends, so we left a little early."],
            ["九份的老街很窄，有很多小吃店。", "jiu3 fen4 de5 lao3 jie1 hen3 zhai3 you3 hen3 duo1 xiao3 chi1 dian4", "Jiufen's old street is narrow and full of snack shops."],
            ["我們吃了有名的芋圓，又甜又好吃。", "wo3 men5 chi1 le5 you3 ming2 de5 yu4 yuan2 you4 tian2 you4 hao3 chi1", "We ate the famous taro balls. They were sweet and delicious."],
            ["晚上的風景好漂亮，我們拍了很多照片。", "wan3 shang4 de5 feng1 jing3 hao3 piao4 liang4 wo3 men5 pai1 le5 hen3 duo1 zhao4 pian4", "The view at night was beautiful, and we took lots of photos."],
            ["回家以前，我問：「最後一班車幾點？」", "hui2 jia1 yi3 qian2 wo3 wen4 zui4 hou4 yi4 ban1 che1 ji3 dian3", "Before going home, I asked, \"When is the last bus?\""],
            ["九份真好玩，下次再來！", "jiu3 fen4 zhen1 hao3 wan2 xia4 ci4 zai4 lai2", "Jiufen was so much fun. I'll come again next time!"],
        ],
    },
    "classroom": {
        "title": "Teaching at a school", "zh": "到國小介紹越南",
        "lines": [
            ["今天我去一所國小介紹越南文化。", "jin1 tian1 wo3 qu4 yi4 suo3 guo2 xiao3 jie4 shao4 yue4 nan2 wen2 hua4", "Today I went to an elementary school to share Vietnamese culture."],
            ["主任帶我到三年級的教室。", "zhu3 ren4 dai4 wo3 dao4 san1 nian2 ji2 de5 jiao4 shi4", "The director took me to a third-grade classroom."],
            ["我說：「小朋友好！我叫小玉，我從越南來。」", "wo3 shuo1 xiao3 peng2 you3 hao3 wo3 jiao4 xiao3 yu4 wo3 cong2 yue4 nan2 lai2", "I said, \"Hello, kids! My name is Xiao Yu, and I'm from Vietnam.\""],
            ["有幾個小朋友的媽媽也是越南人。", "you3 ji3 ge5 xiao3 peng2 you3 de5 ma1 ma5 ye3 shi4 yue4 nan2 ren2", "Some of the children's mothers are Vietnamese too."],
            ["我教他們用越南話說「你好」。", "wo3 jiao1 ta1 men5 yong4 yue4 nan2 hua4 shuo1 ni3 hao3", "I taught them how to say \"hello\" in Vietnamese."],
            ["我說：「跟我念！」大家都念得很大聲。", "wo3 shuo1 gen1 wo3 nian4 da4 jia1 dou1 nian4 de5 hen3 da4 sheng1", "I said, \"Repeat after me!\" and everyone said it out loud."],
            ["最後我們分成四組玩遊戲。", "zui4 hou4 wo3 men5 fen1 cheng2 si4 zu3 wan2 you2 xi4", "At the end, we split into four groups and played a game."],
            ["下課了，小朋友說：「明天再來！」", "xia4 ke4 le5 xiao3 peng2 you3 shuo1 ming2 tian1 zai4 lai2", "When class was over, the children said, \"Come again tomorrow!\""],
        ],
    },
}
