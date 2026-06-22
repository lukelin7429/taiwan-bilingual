/* ============================================================
   SHARED WORD DATA for the Play & games arcade
   Used by: quiz / flashcards / match
   Vocabulary: MOE 1200 (graded), with example sentences.
   Each word: { en, zh, pos, ex, tr, img | hex, fb(emoji) }
   - img  -> illustration at /resources/games/img/<img>.png
   - hex  -> render as a color swatch instead of an image
   TEACHERS: add a topic or word here and all three games update.
   ============================================================ */
(function(){
  var CATEGORIES = [
   {id:"animals",emoji:"🐻",en:"Animals",zh:"動物",words:[
    {en:"dog",img:"dog",fb:"🐶",zh:"狗",pos:"n.",ex:"The dog runs in the park.",tr:"狗在公園裡跑。"},
    {en:"cat",img:"cat",fb:"🐱",zh:"貓",pos:"n.",ex:"The cat sleeps on the sofa.",tr:"貓睡在沙發上。"},
    {en:"bird",img:"bird",fb:"🐦",zh:"鳥",pos:"n.",ex:"The bird sings in the tree.",tr:"鳥在樹上唱歌。"},
    {en:"fish",img:"fish",fb:"🐟",zh:"魚",pos:"n.",ex:"The fish swims in the water.",tr:"魚在水裡游。"},
    {en:"rabbit",img:"rabbit",fb:"🐰",zh:"兔子",pos:"n.",ex:"The rabbit has long ears.",tr:"兔子有長耳朵。"},
    {en:"bear",img:"bear",fb:"🐻",zh:"熊",pos:"n.",ex:"The bear sleeps all winter.",tr:"熊整個冬天都在睡覺。"},
    {en:"tiger",img:"tiger",fb:"🐯",zh:"老虎",pos:"n.",ex:"The tiger is big and strong.",tr:"老虎又大又壯。"},
    {en:"lion",img:"lion",fb:"🦁",zh:"獅子",pos:"n.",ex:"The lion is the king of animals.",tr:"獅子是萬獸之王。"},
    {en:"monkey",img:"monkey",fb:"🐵",zh:"猴子",pos:"n.",ex:"The monkey loves bananas.",tr:"猴子愛吃香蕉。"},
    {en:"elephant",img:"elephant",fb:"🐘",zh:"大象",pos:"n.",ex:"The elephant has a long nose.",tr:"大象有長長的鼻子。"},
    {en:"pig",img:"pig",fb:"🐷",zh:"豬",pos:"n.",ex:"The pig is pink and fat.",tr:"豬又粉又胖。"},
    {en:"duck",img:"duck",fb:"🦆",zh:"鴨子",pos:"n.",ex:"The duck swims in the pond.",tr:"鴨子在池塘裡游。"},
    {en:"bee",img:"bee",fb:"🐝",zh:"蜜蜂",pos:"n.",ex:"A bee is on the flower.",tr:"一隻蜜蜂在花上。"},
    {en:"ant",img:"ant",fb:"🐜",zh:"螞蟻",pos:"n.",ex:"An ant is very small.",tr:"螞蟻很小。"}]},
   {id:"food",emoji:"🍎",en:"Food",zh:"食物",words:[
    {en:"apple",img:"apple",fb:"🍎",zh:"蘋果",pos:"n.",ex:"I eat an apple every day.",tr:"我每天吃一顆蘋果。"},
    {en:"banana",img:"banana",fb:"🍌",zh:"香蕉",pos:"n.",ex:"Monkeys love bananas.",tr:"猴子愛吃香蕉。"},
    {en:"bread",img:"bread",fb:"🍞",zh:"麵包",pos:"n.",ex:"I have bread for breakfast.",tr:"我早餐吃麵包。"},
    {en:"rice",img:"rice",fb:"🍚",zh:"飯",pos:"n.",ex:"We eat rice for dinner.",tr:"我們晚餐吃飯。"},
    {en:"egg",img:"egg",fb:"🍳",zh:"蛋",pos:"n.",ex:"I like a fried egg.",tr:"我喜歡荷包蛋。"},
    {en:"cake",img:"cake",fb:"🍰",zh:"蛋糕",pos:"n.",ex:"The cake is sweet.",tr:"蛋糕很甜。"},
    {en:"milk",img:"milk",fb:"🥛",zh:"牛奶",pos:"n.",ex:"I drink milk in the morning.",tr:"我早上喝牛奶。"},
    {en:"noodles",img:"noodles",fb:"🍜",zh:"麵",pos:"n.",ex:"We eat beef noodles for lunch.",tr:"我們午餐吃牛肉麵。"},
    {en:"candy",img:"candy",fb:"🍬",zh:"糖果",pos:"n.",ex:"The candy is very sweet.",tr:"糖果很甜。"},
    {en:"cookie",img:"cookie",fb:"🍪",zh:"餅乾",pos:"n.",ex:"Can I have a cookie?",tr:"我可以吃一塊餅乾嗎？"},
    {en:"ice cream",img:"ice_cream",fb:"🍦",zh:"冰淇淋",pos:"n.",ex:"I love ice cream in summer.",tr:"我夏天愛吃冰淇淋。"},
    {en:"hamburger",img:"hamburger",fb:"🍔",zh:"漢堡",pos:"n.",ex:"He eats a big hamburger.",tr:"他吃一個大漢堡。"}]},
   {id:"school",emoji:"🎒",en:"School",zh:"學校",words:[
    {en:"book",img:"book",fb:"📖",zh:"書",pos:"n.",ex:"I read a book before bed.",tr:"我睡前看書。"},
    {en:"pen",img:"pen",fb:"🖊️",zh:"筆",pos:"n.",ex:"I write with a blue pen.",tr:"我用藍筆寫字。"},
    {en:"pencil",img:"pencil",fb:"✏️",zh:"鉛筆",pos:"n.",ex:"My pencil is yellow.",tr:"我的鉛筆是黃色的。"},
    {en:"bag",img:"bag",fb:"🎒",zh:"書包",pos:"n.",ex:"My books are in the bag.",tr:"我的書在書包裡。"},
    {en:"ruler",img:"ruler",fb:"📏",zh:"尺",pos:"n.",ex:"I draw a line with a ruler.",tr:"我用尺畫線。"},
    {en:"eraser",img:"eraser",fb:"🧽",zh:"橡皮擦",pos:"n.",ex:"Use an eraser to fix it.",tr:"用橡皮擦改正。"},
    {en:"desk",img:"desk",fb:"🪧",zh:"書桌",pos:"n.",ex:"I do my homework at my desk.",tr:"我在書桌上寫功課。"},
    {en:"chair",img:"chair",fb:"🪑",zh:"椅子",pos:"n.",ex:"Please sit on the chair.",tr:"請坐在椅子上。"},
    {en:"notebook",img:"notebook",fb:"📓",zh:"筆記本",pos:"n.",ex:"I write notes in my notebook.",tr:"我在筆記本上做筆記。"},
    {en:"clock",img:"clock",fb:"🕐",zh:"時鐘",pos:"n.",ex:"The clock is on the wall.",tr:"時鐘在牆上。"},
    {en:"scissors",img:"scissors",fb:"✂️",zh:"剪刀",pos:"n.",ex:"Cut the paper with scissors.",tr:"用剪刀剪紙。"}]},
   {id:"transport",emoji:"🚗",en:"Transport",zh:"交通工具",words:[
    {en:"car",img:"car",fb:"🚗",zh:"汽車",pos:"n.",ex:"My dad drives a red car.",tr:"我爸開一台紅色的車。"},
    {en:"bus",img:"bus",fb:"🚌",zh:"公車",pos:"n.",ex:"I take the bus to school.",tr:"我搭公車上學。"},
    {en:"train",img:"train",fb:"🚆",zh:"火車",pos:"n.",ex:"The train is very fast.",tr:"火車很快。"},
    {en:"airplane",img:"airplane",fb:"✈️",zh:"飛機",pos:"n.",ex:"The airplane is high in the sky.",tr:"飛機在高高的天空中。"},
    {en:"bike",img:"bike",fb:"🚲",zh:"腳踏車",pos:"n.",ex:"I ride my bike to school.",tr:"我騎腳踏車上學。"},
    {en:"boat",img:"boat",fb:"⛵",zh:"船",pos:"n.",ex:"The boat is on the lake.",tr:"船在湖上。"},
    {en:"ship",img:"ship",fb:"🚢",zh:"輪船",pos:"n.",ex:"The big ship sails on the sea.",tr:"大船在海上航行。"},
    {en:"truck",img:"truck",fb:"🚚",zh:"卡車",pos:"n.",ex:"The truck carries boxes.",tr:"卡車載著箱子。"},
    {en:"taxi",img:"taxi",fb:"🚕",zh:"計程車",pos:"n.",ex:"We take a taxi home.",tr:"我們搭計程車回家。"},
    {en:"motorcycle",img:"motorcycle",fb:"🛵",zh:"機車",pos:"n.",ex:"He rides a motorcycle.",tr:"他騎機車。"}]},
   {id:"colors",emoji:"🌈",en:"Colors",zh:"顏色",words:[
    {en:"red",hex:"#e63946",fb:"🔴",zh:"紅色",pos:"adj.",ex:"The apple is red.",tr:"蘋果是紅色的。"},
    {en:"blue",hex:"#1d6ff2",fb:"🔵",zh:"藍色",pos:"adj.",ex:"The sky is blue.",tr:"天空是藍色的。"},
    {en:"yellow",hex:"#ffd21f",fb:"🟡",zh:"黃色",pos:"adj.",ex:"The sun is yellow.",tr:"太陽是黃色的。"},
    {en:"green",hex:"#2ecc71",fb:"🟢",zh:"綠色",pos:"adj.",ex:"The grass is green.",tr:"草是綠色的。"},
    {en:"black",hex:"#2b2b2b",fb:"⚫",zh:"黑色",pos:"adj.",ex:"The cat is black.",tr:"貓是黑色的。"},
    {en:"white",hex:"#ffffff",fb:"⚪",zh:"白色",pos:"adj.",ex:"Snow is white.",tr:"雪是白色的。"},
    {en:"pink",hex:"#ff8fc8",fb:"🌸",zh:"粉紅色",pos:"adj.",ex:"The flower is pink.",tr:"花是粉紅色的。"},
    {en:"purple",hex:"#9b5de5",fb:"🟣",zh:"紫色",pos:"adj.",ex:"I like purple grapes.",tr:"我喜歡紫色的葡萄。"},
    {en:"orange",hex:"#ff8c1a",fb:"🟠",zh:"橘色",pos:"adj.",ex:"The orange is orange.",tr:"柳橙是橘色的。"},
    {en:"brown",hex:"#9c6b3f",fb:"🟤",zh:"棕色",pos:"adj.",ex:"The bear is brown.",tr:"熊是棕色的。"}]},
   {id:"clothes",emoji:"👕",en:"Clothes",zh:"衣物",words:[
    {en:"shirt",img:"shirt",fb:"👕",zh:"襯衫",pos:"n.",ex:"He wears a white shirt.",tr:"他穿白襯衫。"},
    {en:"pants",img:"pants",fb:"👖",zh:"褲子",pos:"n.",ex:"My pants are blue.",tr:"我的褲子是藍色的。"},
    {en:"dress",img:"dress",fb:"👗",zh:"洋裝",pos:"n.",ex:"She wears a pretty dress.",tr:"她穿漂亮的洋裝。"},
    {en:"hat",img:"hat",fb:"🧢",zh:"帽子",pos:"n.",ex:"I wear a hat in the sun.",tr:"太陽下我戴帽子。"},
    {en:"shoes",img:"shoes",fb:"👟",zh:"鞋子",pos:"n.",ex:"My shoes are new.",tr:"我的鞋子是新的。"},
    {en:"socks",img:"socks",fb:"🧦",zh:"襪子",pos:"n.",ex:"I wear warm socks.",tr:"我穿溫暖的襪子。"},
    {en:"coat",img:"coat",fb:"🧥",zh:"外套",pos:"n.",ex:"Put on your coat.",tr:"穿上你的外套。"},
    {en:"skirt",img:"skirt",fb:"👚",zh:"裙子",pos:"n.",ex:"Her skirt is red.",tr:"她的裙子是紅色的。"},
    {en:"gloves",img:"gloves",fb:"🧤",zh:"手套",pos:"n.",ex:"I wear gloves in winter.",tr:"冬天我戴手套。"},
    {en:"scarf",img:"scarf",fb:"🧣",zh:"圍巾",pos:"n.",ex:"She wears a long scarf.",tr:"她圍著長圍巾。"}]},
   {id:"sports",emoji:"⚽",en:"Sports",zh:"運動",words:[
    {en:"ball",img:"ball",fb:"⚽",zh:"球",pos:"n.",ex:"The boy kicks the ball.",tr:"男孩踢球。"},
    {en:"baseball",img:"baseball",fb:"⚾",zh:"棒球",pos:"n.",ex:"They watch a baseball game.",tr:"他們看棒球比賽。"},
    {en:"basketball",img:"basketball",fb:"🏀",zh:"籃球",pos:"n.",ex:"He is good at basketball.",tr:"他很會打籃球。"},
    {en:"soccer",img:"soccer",fb:"⚽",zh:"足球",pos:"n.",ex:"We play soccer after school.",tr:"我們放學後踢足球。"},
    {en:"tennis",img:"tennis",fb:"🎾",zh:"網球",pos:"n.",ex:"She plays tennis on Sunday.",tr:"她星期天打網球。"},
    {en:"badminton",img:"badminton",fb:"🏸",zh:"羽毛球",pos:"n.",ex:"We play badminton in the park.",tr:"我們在公園打羽毛球。"},
    {en:"volleyball",img:"volleyball",fb:"🏐",zh:"排球",pos:"n.",ex:"Volleyball is fun.",tr:"排球很好玩。"},
    {en:"table tennis",img:"pingpong",fb:"🏓",zh:"桌球",pos:"n.",ex:"I like table tennis.",tr:"我喜歡桌球。"}]},
   {id:"nature",emoji:"🌳",en:"Nature",zh:"大自然",words:[
    {en:"tree",img:"tree",fb:"🌳",zh:"樹",pos:"n.",ex:"The bird is in the tree.",tr:"鳥在樹上。"},
    {en:"flower",img:"flower",fb:"🌸",zh:"花",pos:"n.",ex:"The flower is beautiful.",tr:"花很美麗。"},
    {en:"sun",img:"sun",fb:"☀️",zh:"太陽",pos:"n.",ex:"The sun is bright.",tr:"太陽很亮。"},
    {en:"moon",img:"moon",fb:"🌙",zh:"月亮",pos:"n.",ex:"The moon is round tonight.",tr:"今晚的月亮很圓。"},
    {en:"star",img:"star",fb:"⭐",zh:"星星",pos:"n.",ex:"I see a star in the sky.",tr:"我看到天上的星星。"},
    {en:"cloud",img:"cloud",fb:"☁️",zh:"雲",pos:"n.",ex:"The cloud is white.",tr:"雲是白色的。"},
    {en:"rain",img:"rain",fb:"🌧️",zh:"雨",pos:"n.",ex:"The rain falls down.",tr:"雨落下來。"},
    {en:"mountain",img:"mountain",fb:"⛰️",zh:"山",pos:"n.",ex:"The mountain is very high.",tr:"山很高。"},
    {en:"river",img:"river",fb:"🏞️",zh:"河",pos:"n.",ex:"Fish swim in the river.",tr:"魚在河裡游。"},
    {en:"beach",img:"beach",fb:"🏖️",zh:"海灘",pos:"n.",ex:"We swim at the beach.",tr:"我們在海灘游泳。"}]}
  ];
  var ALL=[]; CATEGORIES.forEach(function(c){ c.words.forEach(function(w){ ALL.push(w); }); });
  window.GAME_DATA = { categories:CATEGORIES, all:ALL, IMG:"/resources/games/img/" };
})();
