import json

# A1 Level - 启蒙入门
a1_subtitles = {
    'a1-1': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "Hello, my name is Tom.", "chinese": "你好，我叫汤姆。", "keyWords": ["name"], "vocab": [{"word": "name", "phonetic": "/neɪm/", "meaning": "名字", "example": "My name is Tom."}]},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "How are you today?", "chinese": "你今天好吗？", "keyWords": ["today"], "vocab": [{"word": "today", "phonetic": "/təˈdeɪ/", "meaning": "今天", "example": "I am happy today."}]},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "I am fine, thank you.", "chinese": "我很好，谢谢。", "keyWords": ["fine", "thank"], "vocab": [{"word": "fine", "phonetic": "/faɪn/", "meaning": "好的", "example": "I'm fine, thanks."}, {"word": "thank", "phonetic": "/θæŋk/", "meaning": "感谢", "example": "Thank you very much."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "Nice to meet you.", "chinese": "很高兴见到你。", "keyWords": ["meet"], "vocab": [{"word": "meet", "phonetic": "/miːt/", "meaning": "遇见", "example": "Nice to meet you."}]},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "I am from China.", "chinese": "我来自中国。", "keyWords": ["from"], "vocab": [{"word": "from", "phonetic": "/frʌm/", "meaning": "来自", "example": "I am from China."}]},
        {"id": 6, "startTime": 11, "endTime": 13, "english": "I love learning English.", "chinese": "我喜欢学英语。", "keyWords": ["love", "learning"], "vocab": [{"word": "love", "phonetic": "/lʌv/", "meaning": "喜爱", "example": "I love English."}, {"word": "learn", "phonetic": "/lɜːrn/", "meaning": "学习", "example": "I learn every day."}]}
    ],
    'a1-2': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "One, two, three, four, five.", "chinese": "一、二、三、四、五。", "keyWords": [], "vocab": []},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "Red, blue, green, yellow.", "chinese": "红色、蓝色、绿色、黄色。", "keyWords": ["red", "blue"], "vocab": [{"word": "red", "phonetic": "/red/", "meaning": "红色", "example": "The apple is red."}, {"word": "blue", "phonetic": "/bluː/", "meaning": "蓝色", "example": "The sky is blue."}]},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "I have five apples.", "chinese": "我有五个苹果。", "keyWords": ["have", "apples"], "vocab": [{"word": "have", "phonetic": "/hæv/", "meaning": "有", "example": "I have a book."}, {"word": "apple", "phonetic": "/ˈæpl/", "meaning": "苹果", "example": "I like apples."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "The apple is red.", "chinese": "这个苹果是红色的。", "keyWords": ["apple", "red"], "vocab": []},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "My favorite color is blue.", "chinese": "我最喜欢的颜色是蓝色。", "keyWords": ["favorite", "color"], "vocab": [{"word": "favorite", "phonetic": "/ˈfeɪvərɪt/", "meaning": "最喜欢的", "example": "My favorite color is blue."}, {"word": "color", "phonetic": "/ˈkʌlər/", "meaning": "颜色", "example": "What color do you like?"}]}
    ],
    'a1-3': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "This is my family.", "chinese": "这是我的家庭。", "keyWords": ["family"], "vocab": [{"word": "family", "phonetic": "/ˈfæməli/", "meaning": "家庭", "example": "My family is big."}]},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "I have a father and a mother.", "chinese": "我有爸爸和妈妈。", "keyWords": ["father", "mother"], "vocab": [{"word": "father", "phonetic": "/ˈfɑːðər/", "meaning": "父亲", "example": "My father is a doctor."}, {"word": "mother", "phonetic": "/ˈmʌðər/", "meaning": "母亲", "example": "My mother is a teacher."}]},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "I have a brother, too.", "chinese": "我还有一个哥哥。", "keyWords": ["brother"], "vocab": [{"word": "brother", "phonetic": "/ˈbrʌðər/", "meaning": "兄弟", "example": "I have an older brother."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "We are a happy family.", "chinese": "我们是一个幸福的家庭。", "keyWords": ["happy"], "vocab": [{"word": "happy", "phonetic": "/ˈhæpi/", "meaning": "快乐的", "example": "I am very happy."}]},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "I love my family very much.", "chinese": "我非常爱我的家人。", "keyWords": ["love", "much"], "vocab": [{"word": "much", "phonetic": "/mʌtʃ/", "meaning": "非常", "example": "I love it very much."}]}
    ],
    'a1-4': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "What do you like?", "chinese": "你喜欢什么？", "keyWords": ["like"], "vocab": [{"word": "like", "phonetic": "/laɪk/", "meaning": "喜欢", "example": "I like music."}]},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "I like music and dancing.", "chinese": "我喜欢音乐和跳舞。", "keyWords": ["music", "dancing"], "vocab": [{"word": "music", "phonetic": "/ˈmjuːzɪk/", "meaning": "音乐", "example": "I love music."}, {"word": "dance", "phonetic": "/dæns/", "meaning": "跳舞", "example": "She likes to dance."}]},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "Do you like reading books?", "chinese": "你喜欢读书吗？", "keyWords": ["reading", "books"], "vocab": [{"word": "read", "phonetic": "/riːd/", "meaning": "阅读", "example": "I read books every day."}, {"word": "book", "phonetic": "/bʊk/", "meaning": "书", "example": "This is a good book."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "Yes, I love reading.", "chinese": "是的，我喜欢阅读。", "keyWords": ["love", "reading"], "vocab": []},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "What about you?", "chinese": "你呢？", "keyWords": [], "vocab": []},
        {"id": 6, "startTime": 11, "endTime": 13, "english": "I like playing football.", "chinese": "我喜欢踢足球。", "keyWords": ["playing", "football"], "vocab": [{"word": "play", "phonetic": "/pleɪ/", "meaning": "玩", "example": "Let's play together."}, {"word": "football", "phonetic": "/ˈfʊtbɔːl/", "meaning": "足球", "example": "I play football every Sunday."}]}
    ]
}

# A2 Level - 日常基础
a2_subtitles = {
    'a2-1': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "Yesterday I went shopping.", "chinese": "昨天我去购物了。", "keyWords": ["went", "shopping"], "vocab": [{"word": "go", "phonetic": "/ɡoʊ/", "meaning": "去", "example": "I go to school every day."}, {"word": "shopping", "phonetic": "/ˈʃɑːpɪŋ/", "meaning": "购物", "example": "Let's go shopping."}]},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "I bought some new clothes.", "chinese": "我买了一些新衣服。", "keyWords": ["bought", "clothes"], "vocab": [{"word": "buy", "phonetic": "/baɪ/", "meaning": "买", "example": "I buy a book."}, {"word": "clothes", "phonetic": "/kloʊðz/", "meaning": "衣服", "example": "I need new clothes."}]},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "The store was very busy.", "chinese": "商店里非常拥挤。", "keyWords": ["store", "busy"], "vocab": [{"word": "store", "phonetic": "/stɔːr/", "meaning": "商店", "example": "The store is open."}, {"word": "busy", "phonetic": "/ˈbɪzi/", "meaning": "忙碌的", "example": "I am very busy today."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "I spent a lot of money.", "chinese": "我花了很多钱。", "keyWords": ["spent", "money"], "vocab": [{"word": "spend", "phonetic": "/spend/", "meaning": "花费", "example": "I spend time with my family."}, {"word": "money", "phonetic": "/ˈmʌni/", "meaning": "钱", "example": "I don't have much money."}]},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "But I got a great deal!", "chinese": "但我买到了超值的东西！", "keyWords": ["great", "deal"], "vocab": [{"word": "great", "phonetic": "/ɡreɪt/", "meaning": "很棒的", "example": "That's a great idea."}, {"word": "deal", "phonetic": "/diːl/", "meaning": "交易", "example": "It's a good deal."}]}
    ],
    'a2-2': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "What will you do tomorrow?", "chinese": "你明天要做什么？", "keyWords": ["tomorrow"], "vocab": [{"word": "tomorrow", "phonetic": "/təˈmɒroʊ/", "meaning": "明天", "example": "See you tomorrow."}]},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "I will visit my grandmother.", "chinese": "我要去看望我的奶奶。", "keyWords": ["visit", "grandmother"], "vocab": [{"word": "visit", "phonetic": "/ˈvɪzɪt/", "meaning": "拜访", "example": "I visit my grandma every week."}, {"word": "grandmother", "phonetic": "/ˈɡrænmʌðər/", "meaning": "祖母", "example": "My grandmother is kind."}]},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "We will have lunch together.", "chinese": "我们会一起吃午饭。", "keyWords": ["lunch", "together"], "vocab": [{"word": "lunch", "phonetic": "/lʌntʃ/", "meaning": "午餐", "example": "Let's have lunch."}, {"word": "together", "phonetic": "/təˈɡeðər/", "meaning": "一起", "example": "Let's do it together."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "Then I will go to the gym.", "chinese": "然后我会去健身房。", "keyWords": ["gym"], "vocab": [{"word": "gym", "phonetic": "/dʒɪm/", "meaning": "健身房", "example": "I go to the gym."}]},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "It will be a busy day!", "chinese": "这会是忙碌的一天！", "keyWords": ["busy"], "vocab": []}
    ],
    'a2-3': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "The weather is beautiful today.", "chinese": "今天天气真好。", "keyWords": ["weather", "beautiful"], "vocab": [{"word": "weather", "phonetic": "/ˈweðər/", "meaning": "天气", "example": "The weather is nice."}, {"word": "beautiful", "phonetic": "/ˈbjuːtɪfl/", "meaning": "美丽的", "example": "What a beautiful day!"}]},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "The sun is shining.", "chinese": "阳光明媚。", "keyWords": ["sun", "shining"], "vocab": [{"word": "sun", "phonetic": "/sʌn/", "meaning": "太阳", "example": "The sun is hot."}, {"word": "shine", "phonetic": "/ʃaɪn/", "meaning": "照耀", "example": "The stars shine at night."}]},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "It's about 25 degrees.", "chinese": "温度大约25度。", "keyWords": ["degrees"], "vocab": [{"word": "degree", "phonetic": "/dɪˈɡriː/", "meaning": "度", "example": "It's 30 degrees today."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "I want to go to the park.", "chinese": "我想去公园。", "keyWords": ["park"], "vocab": [{"word": "park", "phonetic": "/pɑːrk/", "meaning": "公园", "example": "Let's go to the park."}]},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "Let's go for a walk!", "chinese": "我们去散步吧！", "keyWords": ["walk"], "vocab": [{"word": "walk", "phonetic": "/wɔːk/", "meaning": "散步", "example": "I walk every morning."}]}
    ],
    'a2-4': [
        {"id": 1, "startTime": 1, "endTime": 3, "english": "How was your weekend?", "chinese": "你的周末过得怎么样？", "keyWords": ["weekend"], "vocab": [{"word": "weekend", "phonetic": "/ˈwiːkend/", "meaning": "周末", "example": "I relax on weekends."}]},
        {"id": 2, "startTime": 3, "endTime": 5, "english": "It was great, thanks.", "chinese": "很棒，谢谢。", "keyWords": [], "vocab": []},
        {"id": 3, "startTime": 5, "endTime": 7, "english": "I went to the movies.", "chinese": "我去看电影了。", "keyWords": ["movies"], "vocab": [{"word": "movie", "phonetic": "/ˈmuːvi/", "meaning": "电影", "example": "Let's watch a movie."}]},
        {"id": 4, "startTime": 7, "endTime": 9, "english": "The film was amazing.", "chinese": "电影非常精彩。", "keyWords": ["film", "amazing"], "vocab": [{"word": "film", "phonetic": "/fɪlm/", "meaning": "电影", "example": "This is a good film."}, {"word": "amazing", "phonetic": "/əˈmeɪzɪŋ/", "meaning": "惊人的", "example": "That's an amazing view."}]},
        {"id": 5, "startTime": 9, "endTime": 11, "english": "I highly recommend it!", "chinese": "我强烈推荐！", "keyWords": ["recommend"], "vocab": [{"word": "recommend", "phonetic": "/ˌrekəˈmend/", "meaning": "推荐", "example": "I recommend this book."}]}
    ]
}

# B1 Level - 突破进阶
b1_subtitles = {
    'b1-1': [
        {"id": 1, "startTime": 1, "endTime": 4, "english": "The city has been completely rebuilt.", "chinese": "这座城市已经被完全重建。", "keyWords": ["completely", "rebuilt"], "vocab": [{"word": "completely", "phonetic": "/kəmˈpliːtli/", "meaning": "完全地", "example": "I completely agree."}, {"word": "rebuild", "phonetic": "/ˌriːˈbɪld/", "meaning": "重建", "example": "They will rebuild the house."}]},
        {"id": 2, "startTime": 4, "endTime": 7, "english": "Many new buildings have been constructed.", "chinese": "许多新的建筑物已经建成。", "keyWords": ["buildings", "constructed"], "vocab": [{"word": "building", "phonetic": "/ˈbɪldɪŋ/", "meaning": "建筑物", "example": "This is a tall building."}, {"word": "construct", "phonetic": "/kənˈstrʌkt/", "meaning": "建造", "example": "They construct bridges."}]},
        {"id": 3, "startTime": 7, "endTime": 10, "english": "The project was funded by the government.", "chinese": "该项目由政府资助。", "keyWords": ["project", "funded", "government"], "vocab": [{"word": "project", "phonetic": "/ˈprɒdʒekt/", "meaning": "项目", "example": "This is an important project."}, {"word": "fund", "phonetic": "/fʌnd/", "meaning": "资助", "example": "The project is funded."}, {"word": "government", "phonetic": "/ˈɡʌvərnmənt/", "meaning": "政府", "example": "The government helps people."}]},
        {"id": 4, "startTime": 10, "endTime": 13, "english": "Local residents have benefited from it.", "chinese": "当地居民从中受益。", "keyWords": ["residents", "benefited"], "vocab": [{"word": "resident", "phonetic": "/ˈrezɪdənt/", "meaning": "居民", "example": "The residents are happy."}, {"word": "benefit", "phonetic": "/ˈbenɪfɪt/", "meaning": "受益", "example": "She benefits from the course."}]},
        {"id": 5, "startTime": 13, "endTime": 16, "english": "The transformation is truly remarkable.", "chinese": "这一转型确实令人瞩目。", "keyWords": ["transformation", "remarkable"], "vocab": [{"word": "transformation", "phonetic": "/ˌtrænsfərˈmeɪʃn/", "meaning": "转变", "example": "A transformation has occurred."}, {"word": "remarkable", "phonetic": "/rɪˈmɑːrkəbl/", "meaning": "卓越的", "example": "That's a remarkable achievement."}]}
    ],
    'b1-2': [
        {"id": 1, "startTime": 1, "endTime": 4, "english": "If I had more time, I would travel more.", "chinese": "如果我有更多时间，我会多去旅行。", "keyWords": ["travel"], "vocab": [{"word": "travel", "phonetic": "/ˈtrævl/", "meaning": "旅行", "example": "I love to travel."}]},
        {"id": 2, "startTime": 4, "endTime": 7, "english": "I would visit countries like Japan and France.", "chinese": "我想去日本和法国这样的国家。", "keyWords": ["visit", "countries"], "vocab": [{"word": "country", "phonetic": "/ˈkʌntri/", "meaning": "国家", "example": "France is a beautiful country."}]},
        {"id": 3, "startTime": 7, "endTime": 10, "english": "There are so many places I want to see.", "chinese": "有太多地方我想去看。", "keyWords": ["places"], "vocab": [{"word": "place", "phonetic": "/pleɪs/", "meaning": "地方", "example": "This is a nice place."}]},
        {"id": 4, "startTime": 10, "endTime": 13, "english": "Unfortunately, I have to work.", "chinese": "不幸的是，我必须工作。", "keyWords": ["unfortunately"], "vocab": [{"word": "unfortunately", "phonetic": "/ʌnˈfɔːrtʃənətli/", "meaning": "不幸地", "example": "Unfortunately, I can't come."}]},
        {"id": 5, "startTime": 13, "endTime": 16, "english": "Maybe next year, things will be different.", "chinese": "也许明年情况会有所不同。", "keyWords": ["different"], "vocab": [{"word": "different", "phonetic": "/ˈdɪfrənt/", "meaning": "不同的", "example": "We are different."}]}
    ],
    'b1-3': [
        {"id": 1, "startTime": 1, "endTime": 4, "english": "A typical day for a student starts early.", "chinese": "学生典型的一天很早就开始了。", "keyWords": ["typical", "student"], "vocab": [{"word": "typical", "phonetic": "/ˈtɪpɪkl/", "meaning": "典型的", "example": "That's a typical day."}, {"word": "student", "phonetic": "/ˈstuːdnt/", "meaning": "学生", "example": "She is a good student."}]},
        {"id": 2, "startTime": 4, "endTime": 7, "english": "We usually have breakfast at seven.", "chinese": "我们通常七点吃早餐。", "keyWords": ["breakfast"], "vocab": [{"word": "breakfast", "phonetic": "/ˈbrekfəst/", "meaning": "早餐", "example": "I have breakfast at 7."}]},
        {"id": 3, "startTime": 7, "endTime": 10, "english": "Then we head to school for class.", "chinese": "然后我们去学校上课。", "keyWords": ["head", "class"], "vocab": [{"word": "class", "phonetic": "/klæs/", "meaning": "班级", "example": "My class is big."}]},
        {"id": 4, "startTime": 10, "endTime": 13, "english": "Lunch break is from twelve to one.", "chinese": "午休时间是十二点到一点。", "keyWords": ["break"], "vocab": [{"word": "break", "phonetic": "/breɪk/", "meaning": "休息", "example": "Let's take a break."}]},
        {"id": 5, "startTime": 13, "endTime": 16, "english": "After school, I usually do my homework.", "chinese": "放学后，我通常做作业。", "keyWords": ["homework"], "vocab": [{"word": "homework", "phonetic": "/ˈhoʊmwɜːrk/", "meaning": "作业", "example": "I have too much homework."}]},
        {"id": 6, "startTime": 16, "endTime": 19, "english": "Then I hang out with friends.", "chinese": "然后我和朋友们出去玩。", "keyWords": ["hang", "friends"], "vocab": [{"word": "friend", "phonetic": "/frend/", "meaning": "朋友", "example": "She is my best friend."}]}
    ],
    'b1-4': [
        {"id": 1, "startTime": 1, "endTime": 4, "english": "The environment is facing serious challenges.", "chinese": "环境正面临严峻挑战。", "keyWords": ["environment", "challenges"], "vocab": [{"word": "environment", "phonetic": "/ɪnˈvaɪrənmənt/", "meaning": "环境", "example": "We must protect the environment."}, {"word": "challenge", "phonetic": "/ˈtʃælɪndʒ/", "meaning": "挑战", "example": "This is a big challenge."}]},
        {"id": 2, "startTime": 4, "endTime": 7, "english": "Climate change is affecting our planet.", "chinese": "气候变化正在影响我们的星球。", "keyWords": ["climate", "planet"], "vocab": [{"word": "climate", "phonetic": "/ˈklaɪmət/", "meaning": "气候", "example": "The climate is changing."}, {"word": "planet", "phonetic": "/ˈplænɪt/", "meaning": "行星", "example": "Earth is our planet."}]},
        {"id": 3, "startTime": 7, "endTime": 10, "english": "We need to take action now.", "chinese": "我们现在就需要采取行动。", "keyWords": ["action"], "vocab": [{"word": "action", "phonetic": "/ˈækʃn/", "meaning": "行动", "example": "Take action now."}]},
        {"id": 4, "startTime": 10, "endTime": 13, "english": "Renewable energy is the future.", "chinese": "可再生能源是未来的发展方向。", "keyWords": ["renewable", "energy"], "vocab": [{"word": "renewable", "phonetic": "/rɪˈnuːəbl/", "meaning": "可再生的", "example": "Solar power is renewable."}, {"word": "energy", "phonetic": "/ˈenərdʒi/", "meaning": "能源", "example": "We need more energy."}]},
        {"id": 5, "startTime": 13, "endTime": 16, "english": "Together, we can make a difference.", "chinese": "我们一起可以有所作为。", "keyWords": ["together", "difference"], "vocab": [{"word": "difference", "phonetic": "/ˈdɪfrəns/", "meaning": "不同", "example": "You can make a difference."}]}
    ]
}

# B2 Level - 流利应用
b2_subtitles = {
    'b2-1': [
        {"id": 1, "startTime": 1, "endTime": 5, "english": "Despite the numerous challenges we faced, we ultimately succeeded.", "chinese": "尽管我们面临无数挑战，最终还是成功了。", "keyWords": ["numerous", "ultimately"], "vocab": [{"word": "numerous", "phonetic": "/ˈnuːmərəs/", "meaning": "众多的", "example": "There are numerous problems."}, {"word": "ultimately", "phonetic": "/ˈʌltɪmətli/", "meaning": "最终", "example": "Ultimately, he was right."}]},
        {"id": 2, "startTime": 5, "endTime": 9, "english": "The project required extensive planning and collaboration.", "chinese": "该项目需要广泛的规划和协作。", "keyWords": ["extensive", "collaboration"], "vocab": [{"word": "extensive", "phonetic": "/ɪkˈstensɪv/", "meaning": "广泛的", "example": "He has extensive experience."}, {"word": "collaboration", "phonetic": "/kəˌlæbəˈreɪʃn/", "meaning": "合作", "example": "Our collaboration was successful."}]},
        {"id": 3, "startTime": 9, "endTime": 13, "english": "Each team member played a crucial role in the outcome.", "chinese": "每个团队成员都在结果中发挥了关键作用。", "keyWords": ["crucial", "outcome"], "vocab": [{"word": "crucial", "phonetic": "/ˈkruːʃl/", "meaning": "至关重要的", "example": "This is a crucial moment."}, {"word": "outcome", "phonetic": "/ˈaʊtkʌm/", "meaning": "结果", "example": "The outcome was positive."}]},
        {"id": 4, "startTime": 13, "endTime": 17, "english": "Therefore, I would like to express my sincere gratitude.", "chinese": "因此，我想表达我真诚的感谢。", "keyWords": ["therefore", "sincere", "gratitude"], "vocab": [{"word": "therefore", "phonetic": "/ˈðerfɔːr/", "meaning": "因此", "example": "It's raining; therefore, stay home."}, {"word": "sincere", "phonetic": "/sɪnˈsɪr/", "meaning": "真诚的", "example": "My apologies are sincere."}, {"word": "gratitude", "phonetic": "/ˈɡrætɪtuːd/", "meaning": "感激", "example": "I feel deep gratitude."}]},
        {"id": 5, "startTime": 17, "endTime": 21, "english": "Without their dedication, this achievement would have been impossible.", "chinese": "没有他们的奉献，这个成就是不可能的。", "keyWords": ["dedication", "achievement"], "vocab": [{"word": "dedication", "phonetic": "/ˌdedɪˈkeɪʃn/", "meaning": "奉献", "example": "Her dedication is admirable."}, {"word": "achievement", "phonetic": "/əˈtʃiːvmənt/", "meaning": "成就", "example": "This is a great achievement."}]}
    ],
    'b2-2': [
        {"id": 1, "startTime": 1, "endTime": 5, "english": "If I were you, I would accept the offer without hesitation.", "chinese": "如果我是你，我会毫不犹豫地接受这个提议。", "keyWords": ["hesitation"], "vocab": [{"word": "hesitation", "phonetic": "/ˌhezɪˈteɪʃn/", "meaning": "犹豫", "example": "Without hesitation, he agreed."}]},
        {"id": 2, "startTime": 5, "endTime": 9, "english": "The benefits far outweigh the potential risks.", "chinese": "好处远远超过潜在的风险。", "keyWords": ["benefits", "outweigh", "risks"], "vocab": [{"word": "benefit", "phonetic": "/ˈbenɪfɪt/", "meaning": "好处", "example": "Exercise has many benefits."}, {"word": "outweigh", "phonetic": "/ˌaʊtˈweɪ/", "meaning": "超过", "example": "The good outweighs the bad."}, {"word": "risk", "phonetic": "/rɪsk/", "meaning": "风险", "example": "There's a risk of failure."}]},
        {"id": 3, "startTime": 9, "endTime": 13, "english": "Moreover, the company offers excellent prospects.", "chinese": "此外，公司提供卓越的发展前景。", "keyWords": ["moreover", "prospects"], "vocab": [{"word": "moreover", "phonetic": "/mɔːrˈoʊvər/", "meaning": "此外", "example": "It's cheap; moreover, it's good."}, {"word": "prospect", "phonetic": "/ˈprɒspekt/", "meaning": "前景", "example": "The prospects are bright."}]},
        {"id": 4, "startTime": 13, "endTime": 17, "english": "You would be wise to seize this opportunity.", "chinese": "你应该明智地抓住这个机会。", "keyWords": ["wise", "seize", "opportunity"], "vocab": [{"word": "wise", "phonetic": "/waɪz/", "meaning": "明智的", "example": "She is a wise woman."}, {"word": "seize", "phonetic": "/siːz/", "meaning": "抓住", "example": "Seize the moment!"}, {"word": "opportunity", "phonetic": "/ˌɒpərˈtuːnəti/", "meaning": "机会", "example": "A great opportunity awaits."}]}
    ],
    'b2-3': [
        {"id": 1, "startTime": 1, "endTime": 5, "english": "Technology has profoundly transformed modern society.", "chinese": "科技深刻地改变了现代社会。", "keyWords": ["profoundly", "transformed", "society"], "vocab": [{"word": "profoundly", "phonetic": "/prəˈfaʊndli/", "meaning": "深刻地", "example": "She was profoundly moved."}, {"word": "transform", "phonetic": "/trænsˈfɔːrm/", "meaning": "改变", "example": "Technology transforms lives."}, {"word": "society", "phonetic": "/səˈsaɪəti/", "meaning": "社会", "example": "Society is changing."}]},
        {"id": 2, "startTime": 5, "endTime": 9, "english": "From education to healthcare, its impact is undeniable.", "chinese": "从教育到医疗，它的影响是不可否认的。", "keyWords": ["impact", "undeniable"], "vocab": [{"word": "impact", "phonetic": "/ˈɪmpækt/", "meaning": "影响", "example": "The impact was huge."}, {"word": "undeniable", "phonetic": "/ˌʌndɪˈnaɪəbl/", "meaning": "不可否认的", "example": "The evidence is undeniable."}]},
        {"id": 3, "startTime": 9, "endTime": 13, "english": "However, we must also consider its unintended consequences.", "chinese": "然而，我们也必须考虑其意想不到的后果。", "keyWords": ["consider", "unintended", "consequences"], "vocab": [{"word": "consider", "phonetic": "/kənˈsɪdər/", "meaning": "考虑", "example": "Consider your options."}, {"word": "unintended", "phonetic": "/ˌʌnɪnˈtendɪd/", "meaning": "意外的", "example": "There were unintended effects."}, {"word": "consequence", "phonetic": "/ˈkɒnsɪkwens/", "meaning": "后果", "example": "Consider the consequences."}]},
        {"id": 4, "startTime": 13, "endTime": 17, "english": "Striking a balance between innovation and caution is crucial.", "chinese": "在创新与谨慎之间取得平衡至关重要。", "keyWords": ["striking", "balance", "innovation", "crucial"], "vocab": [{"word": "strike", "phonetic": "/straɪk/", "meaning": "达到", "example": "Strike while the iron is hot."}, {"word": "balance", "phonetic": "/ˈbæləns/", "meaning": "平衡", "example": "Find the right balance."}, {"word": "innovation", "phonetic": "/ˌɪnəˈveɪʃn/", "meaning": "创新", "example": "Innovation drives growth."}]}
    ],
    'b2-4': [
        {"id": 1, "startTime": 1, "endTime": 5, "english": "Not only did we win the championship, but we also broke the record.", "chinese": "我们不仅赢得了冠军，还打破了记录。", "keyWords": ["championship", "record"], "vocab": [{"word": "championship", "phonetic": "/ˈtʃæmpiənʃɪp/", "meaning": "冠军", "example": "We won the championship."}, {"word": "record", "phonetic": "/ˈrekɔːrd/", "meaning": "记录", "example": "She set a new record."}]},
        {"id": 2, "startTime": 5, "endTime": 9, "english": "Never before has our team performed so exceptionally.", "chinese": "我们的团队从未有过如此出色的表现。", "keyWords": ["performed", "exceptionally"], "vocab": [{"word": "perform", "phonetic": "/pərˈfɔːrm/", "meaning": "表演", "example": "The band performed well."}, {"word": "exceptionally", "phonetic": "/ɪkˈsepʃənli/", "meaning": "特别地", "example": "She is exceptionally talented."}]},
        {"id": 3, "startTime": 9, "endTime": 13, "english": "It is through dedication and teamwork that we achieved this.", "chinese": "正是通过奉献和团队合作，我们才实现了这一点。", "keyWords": ["dedication", "teamwork"], "vocab": [{"word": "teamwork", "phonetic": "/ˈtiːmwɜːrk/", "meaning": "团队合作", "example": "Teamwork is key."}]},
        {"id": 4, "startTime": 13, "endTime": 17, "english": "What makes this victory even more special is the journey itself.", "chinese": "让这次胜利更特别的是这段旅程本身。", "keyWords": ["victory", "journey"], "vocab": [{"word": "victory", "phonetic": "/ˈvɪktəri/", "meaning": "胜利", "example": "This is our greatest victory."}, {"word": "journey", "phonetic": "/ˈdʒɜːrni/", "meaning": "旅程", "example": "Life is a journey."}]}
    ]
}

# C1 Level - 精通母语级
c1_subtitles = {
    'c1-1': [
        {"id": 1, "startTime": 1, "endTime": 6, "english": "The paradox of choice is a fascinating concept that challenges our assumptions about freedom.", "chinese": "选择悖论是一个引人入胜的概念，它挑战了我们对自由的假设。", "keyWords": ["paradox", "fascinating", "concept", "assumptions"], "vocab": [{"word": "paradox", "phonetic": "/ˈpærədɒks/", "meaning": "悖论", "example": "This is a fascinating paradox."}, {"word": "fascinating", "phonetic": "/ˈfæsɪneɪtɪŋ/", "meaning": "迷人的", "example": "What a fascinating story!"}, {"word": "concept", "phonetic": "/ˈkɒnsept/", "meaning": "概念", "example": "Explain the concept."}, {"word": "assumption", "phonetic": "/əˈsʌmpʃn/", "meaning": "假设", "example": "That's a false assumption."}]},
        {"id": 2, "startTime": 6, "endTime": 11, "english": "We often assume that more choices lead to greater satisfaction, but research suggests otherwise.", "chinese": "我们常常认为更多的选择会带来更大的满足感，但研究表明并非如此。", "keyWords": ["satisfaction", "research", "suggests"], "vocab": [{"word": "satisfaction", "phonetic": "/ˌsætɪsˈfækʃn/", "meaning": "满足", "example": "Job satisfaction is important."}, {"word": "research", "phonetic": "/ˈriːsɜːrtʃ/", "meaning": "研究", "example": "New research shows that..."}]},
        {"id": 3, "startTime": 11, "endTime": 16, "english": "When confronted with an overwhelming array of options, people tend to experience anxiety.", "chinese": "当面对过多的选择时，人们往往会感到焦虑。", "keyWords": ["confronted", "overwhelming", "array", "anxiety"], "vocab": [{"word": "confront", "phonetic": "/kənˈfrʌnt/", "meaning": "面对", "example": "Face the truth."}, {"word": "overwhelming", "phonetic": "/ˌoʊvərˈwelmɪŋ/", "meaning": "压倒性的", "example": "The task is overwhelming."}, {"word": "anxiety", "phonetic": "/æŋˈzaɪəti/", "meaning": "焦虑", "example": "She suffers from anxiety."}]},
        {"id": 4, "startTime": 16, "endTime": 21, "english": "This phenomenon has significant implications for decision-making in various domains.", "chinese": "这一现象对各个领域的决策都有重要影响。", "keyWords": ["phenomenon", "significant", "implications", "domains"], "vocab": [{"word": "phenomenon", "phonetic": "/fəˈnɒmɪnən/", "meaning": "现象", "example": "This is a rare phenomenon."}, {"word": "significant", "phonetic": "/sɪɡˈnɪfɪkənt/", "meaning": "重要的", "example": "This is significant news."}, {"word": "implication", "phonetic": "/ˌɪmplɪˈkeɪʃn/", "meaning": "含义", "example": "Consider the implications."}]},
        {"id": 5, "startTime": 21, "endTime": 26, "english": "Understanding this dynamic can help individuals make more informed choices.", "chinese": "理解这一动态可以帮助个人做出更明智的选择。", "keyWords": ["dynamic", "informed", "choices"], "vocab": [{"word": "dynamic", "phonetic": "/daɪˈnæmɪk/", "meaning": "动态", "example": "It's a dynamic process."}, {"word": "informed", "phonetic": "/ɪnˈfɔːrmd/", "meaning": "知情的", "example": "Make an informed decision."}]}
    ],
    'c1-2': [
        {"id": 1, "startTime": 1, "endTime": 6, "english": "A critical analysis of modernism requires an understanding of its historical context.", "chinese": "对现代主义的批判性分析需要理解其历史背景。", "keyWords": ["critical", "analysis", "modernism", "historical", "context"], "vocab": [{"word": "critical", "phonetic": "/ˈkrɪtɪkl/", "meaning": "批判的", "example": "This is a critical issue."}, {"word": "analysis", "phonetic": "/əˈnælɪsɪs/", "meaning": "分析", "example": "Let's do a careful analysis."}, {"word": "modernism", "phonetic": "/ˈmɒdərnɪzəm/", "meaning": "现代主义", "example": "Modernism changed art."}, {"word": "context", "phonetic": "/ˈkɒntekst/", "meaning": "背景", "example": "Consider the context."}]},
        {"id": 2, "startTime": 6, "endTime": 11, "english": "Emerging in the early twentieth century, it was a response to profound societal changes.", "chinese": "它出现在二十世纪初，是对深刻社会变革的回应。", "keyWords": ["emerging", "profound", "societal"], "vocab": [{"word": "emerge", "phonetic": "/ɪˈmɜːrdʒ/", "meaning": "出现", "example": "New evidence emerged."}, {"word": "profound", "phonetic": "/prəˈfaʊnd/", "meaning": "深刻的", "example": "This is a profound insight."}, {"word": "societal", "phonetic": "/səˈsaɪətl/", "meaning": "社会的", "example": "Societal norms are changing."}]},
        {"id": 3, "startTime": 11, "endTime": 16, "english": "Artists and writers sought to break away from traditional forms and conventions.", "chinese": "艺术家和作家寻求摆脱传统形式和惯例。", "keyWords": ["sought", "traditional", "conventions"], "vocab": [{"word": "seek", "phonetic": "/siːk/", "meaning": "寻求", "example": "Seek the truth."}, {"word": "traditional", "phonetic": "/trəˈdɪʃənl/", "meaning": "传统的", "example": "Traditional values are important."}, {"word": "convention", "phonetic": "/kənˈvenʃn/", "meaning": "惯例", "example": "Break with convention."}]},
        {"id": 4, "startTime": 16, "endTime": 21, "english": "Their revolutionary works challenged established norms and pushed creative boundaries.", "chinese": "他们的革命性作品挑战了既定的规范，推动了创造性的边界。", "keyWords": ["revolutionary", "established", "boundaries"], "vocab": [{"word": "revolutionary", "phonetic": "/ˌrevəˈluːʃəneri/", "meaning": "革命性的", "example": "This is revolutionary technology."}, {"word": "established", "phonetic": "/ɪˈstæblɪʃt/", "meaning": "确立的", "example": "The company is well established."}, {"word": "boundary", "phonetic": "/ˈbaʊndri/", "meaning": "边界", "example": "Push the boundaries."}]}
    ],
    'c1-3': [
        {"id": 1, "startTime": 1, "endTime": 6, "english": "The art of rhetoric in public speaking is a skill that can be mastered through deliberate practice.", "chinese": "公共演讲中的修辞艺术是一种可以通过刻意练习掌握的技能。", "keyWords": ["rhetoric", "public", "mastered", "deliberate"], "vocab": [{"word": "rhetoric", "phonetic": "/ˈretərɪk/", "meaning": "修辞", "example": "Political rhetoric."}, {"word": "deliberate", "phonetic": "/dɪˈlɪbərət/", "meaning": "刻意的", "example": "Make a deliberate choice."}]},
        {"id": 2, "startTime": 6, "endTime": 11, "english": "Great speakers employ various techniques to captivate and persuade their audience.", "chinese": "优秀的演讲者运用各种技巧来吸引和说服他们的听众。", "keyWords": ["employ", "techniques", "captivate", "persuade"], "vocab": [{"word": "employ", "phonetic": "/ɪmˈplɔɪ/", "meaning": "运用", "example": "Employ different methods."}, {"word": "technique", "phonetic": "/tekˈniːk/", "meaning": "技巧", "example": "Use this technique."}, {"word": "captivate", "phonetic": "/ˈkæptɪveɪt/", "meaning": "吸引", "example": "The story captivated her."}, {"word": "persuade", "phonetic": "/pərˈsweɪd/", "meaning": "说服", "example": "I couldn't persuade him."}]},
        {"id": 3, "startTime": 11, "endTime": 16, "english": "From metaphors and anecdotes to rhetorical questions, each element serves a specific purpose.", "chinese": "从比喻和轶事到反问句，每个元素都有其特定用途。", "keyWords": ["metaphors", "anecdotes", "rhetorical", "element"], "vocab": [{"word": "metaphor", "phonetic": "/ˈmetəfɔːr/", "meaning": "比喻", "example": "A powerful metaphor."}, {"word": "anecdote", "phonetic": "/ˈænɪkdoʊt/", "meaning": "轶事", "example": "Tell an anecdote."}, {"word": "element", "phonetic": "/ˈelɪmənt/", "meaning": "元素", "example": "A key element of success."}]},
        {"id": 4, "startTime": 16, "endTime": 21, "english": "By understanding and applying these tools, anyone can become a more effective communicator.", "chinese": "通过理解和运用这些工具，任何人都可以成为更有效的沟通者。", "keyWords": ["applying", "effective", "communicator"], "vocab": [{"word": "effective", "phonetic": "/ɪˈfektɪv/", "meaning": "有效的", "example": "An effective strategy."}, {"word": "communicator", "phonetic": "/kəˈmjuːnɪkeɪtər/", "meaning": "沟通者", "example": "She's a great communicator."}]}
    ],
    'c1-4': [
        {"id": 1, "startTime": 1, "endTime": 6, "english": "Interpreting complex texts requires more than just linguistic proficiency.", "chinese": "解读复杂文本需要的不仅仅是语言能力。", "keyWords": ["interpreting", "complex", "texts", "linguistic", "proficiency"], "vocab": [{"word": "interpret", "phonetic": "/ɪnˈtɜːrprət/", "meaning": "解读", "example": "Interpret the poem."}, {"word": "complex", "phonetic": "/kəmˈpleks/", "meaning": "复杂的", "example": "A complex issue."}, {"word": "text", "phonetic": "/tekst/", "meaning": "文本", "example": "Read the text carefully."}, {"word": "linguistic", "phonetic": "/lɪŋˈɡwɪstɪk/", "meaning": "语言的", "example": "Linguistic analysis."}, {"word": "proficiency", "phonetic": "/prəˈfɪʃnsi/", "meaning": "熟练", "example": "Language proficiency."}]},
        {"id": 2, "startTime": 6, "endTime": 11, "english": "It demands critical thinking, cultural awareness, and literary sensitivity.", "chinese": "它需要批判性思维、文化意识和文学敏感性。", "keyWords": ["demands", "critical", "awareness", "sensitivity"], "vocab": [{"word": "demand", "phonetic": "/dɪˈmænd/", "meaning": "要求", "example": "The job demands patience."}, {"word": "sensitivity", "phonetic": "/ˌsensɪˈtɪvəti/", "meaning": "敏感", "example": "Cultural sensitivity is important."}]},
        {"id": 3, "startTime": 11, "endTime": 16, "english": "Literary devices such as symbolism, irony, and allegory often require deeper analysis.", "chinese": "象征、讽刺和寓言等文学手法往往需要更深入的分析。", "keyWords": ["literary", "devices", "symbolism", "irony", "allegory"], "vocab": [{"word": "symbolism", "phonetic": "/ˈsɪmbəlɪzəm/", "meaning": "象征", "example": "The use of symbolism."}, {"word": "irony", "phonetic": "/ˈaɪrəni/", "meaning": "讽刺", "example": "What irony!"}, {"word": "allegory", "phonetic": "/ˈælɪɡɔːri/", "meaning": "寓言", "example": "A classic allegory."}]},
        {"id": 4, "startTime": 16, "endTime": 21, "english": "By examining these layers of meaning, readers can develop a richer understanding of the work.", "chinese": "通过审视这些意义层次，读者可以对作品有更丰富的理解。", "keyWords": ["examining", "layers", "richer", "understanding"], "vocab": [{"word": "examine", "phonetic": "/ɪɡˈzæmɪn/", "meaning": "检验", "example": "Examine the evidence."}, {"word": "layer", "phonetic": "/ˈleɪər/", "meaning": "层次", "example": "Layers of meaning."}]}
    ]
}

# Build the complete levels data
levels_data = [
    {
        "id": "a1",
        "name": "启蒙入门",
        "level": "A1",
        "difficulty": 1,
        "color": "#10b981",
        "gradient": "linear-gradient(135deg, #10b981 0%, #059669 100%)",
        "icon": "fa-seedling",
        "vocabulary": {
            "count": "200-500",
            "unit": "词",
            "topics": ["数字", "颜色", "家庭", "身体", "食物", "时间", "常见物品"]
        },
        "goal": "掌握字母和音标，能理解并使用最基础的日常用语，进行简单的自我介绍与问答",
        "content": {
            "phonetics": "26个字母的读与写，国际音标（48个音素），自然拼读基本规则",
            "vocabulary": "200-500个最核心词汇，涵盖数字、颜色、家庭、身体、食物、时间、常见物品等",
            "grammar": "人称代词、be动词、名词单复数、基本的there be句型、一般现在时（含第三人称单数）、can/can't表示能力",
            "skills": "能听懂极其缓慢、清晰的短句，说出或写出自己的名字、年龄、来自哪里等简单信息"
        },
        "method": {
            "description": "以听读模仿为主，不求死记硬背语法规则，通过大量图片、声音建立直接关联",
            "steps": [
                "每天跟读字母和单词发音，使用APP练习发音打分",
                "用闪卡（实物图+单词）反复记忆基础名词、动词",
                "观看简单英文儿童动画（如《小猪佩奇》英文版），配合画面理解",
                "做\"单句模仿\"练习，听一句复述一句"
            ],
            "resources": ["多邻国", "Memrise", "BBC Learning English Lower Intermediate", "《新概念英语》第一册前半部分"]
        },
        "sampleVideos": [
            {"id": "a1-1", "title": "Hello, How Are You?", "duration": "03:15", "difficulty": "简单", "tags": ["问候", "自我介绍"], "subtitles": a1_subtitles['a1-1']},
            {"id": "a1-2", "title": "Numbers and Colors", "duration": "02:45", "difficulty": "简单", "tags": ["数字", "颜色"], "subtitles": a1_subtitles['a1-2']},
            {"id": "a1-3", "title": "My Family Members", "duration": "04:00", "difficulty": "简单", "tags": ["家庭", "介绍"], "subtitles": a1_subtitles['a1-3']},
            {"id": "a1-4", "title": "What Do You Like?", "duration": "03:30", "difficulty": "简单", "tags": ["爱好", "喜好"], "subtitles": a1_subtitles['a1-4']}
        ]
    },
    {
        "id": "a2",
        "name": "日常基础",
        "level": "A2",
        "difficulty": 2,
        "color": "#3b82f6",
        "gradient": "linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)",
        "icon": "fa-book",
        "vocabulary": {
            "count": "1000-1500",
            "unit": "词",
            "topics": ["旅行", "职业", "日常活动", "情感", "商店", "购物", "天气"]
        },
        "goal": "能就个人和家庭信息、购物、天气、爱好等常见话题进行简单交流，写出简短的便条或描述",
        "content": {
            "phonetics": "巩固音标，学习连读、弱读等基本语音现象",
            "vocabulary": "扩展至1000-1500词，增加旅行、职业、日常活动、情感、商店与购物等主题词汇",
            "grammar": "一般过去时、一般将来时（will/going to）、现在进行时、形容词比较级和最高级、情态动词（must, should）、基础副词、常见介词短语",
            "skills": "能听懂语速较慢、发音清晰的日常对话；能描述昨天做了什么、明天打算做什么；能读懂简短的通知、邮件、菜单，能写简单的日记"
        },
        "method": {
            "description": "开始构建\"句子框架\"，将孤立单词应用到实用场景中，大量进行对话模仿和简单阅读",
            "steps": [
                "用\"影子跟读法\"练习短对话，模仿语音语调",
                "用英语记三句话日记，强制使用新学的时态",
                "开始阅读分级读物，从小学高年级水平开始，不查过多词",
                "找一个语伴或用AI对话，围绕固定话题（如周末安排）反复练习"
            ],
            "resources": ["ESLPod.com 播客", "《新概念英语》第一册后半及第二册前24课", "英语流利说", "Raz-Kids分级阅读", "Oxford Bookworms Starter"]
        },
        "sampleVideos": [
            {"id": "a2-1", "title": "Yesterday I Went Shopping", "duration": "04:20", "difficulty": "中等", "tags": ["过去时", "购物"], "subtitles": a2_subtitles['a2-1']},
            {"id": "a2-2", "title": "What Will You Do Tomorrow?", "duration": "03:50", "difficulty": "中等", "tags": ["将来时", "计划"], "subtitles": a2_subtitles['a2-2']},
            {"id": "a2-3", "title": "The Weather Is Beautiful Today", "duration": "03:10", "difficulty": "中等", "tags": ["天气", "日常"], "subtitles": a2_subtitles['a2-3']},
            {"id": "a2-4", "title": "How Was Your Weekend?", "duration": "04:30", "difficulty": "中等", "tags": ["对话", "过去时"], "subtitles": a2_subtitles['a2-4']}
        ]
    },
    {
        "id": "b1",
        "name": "突破进阶",
        "level": "B1",
        "difficulty": 3,
        "color": "#8b5cf6",
        "gradient": "linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)",
        "icon": "fa-rocket",
        "vocabulary": {
            "count": "3000",
            "unit": "词",
            "topics": ["抽象名词", "情感描述", "工作术语", "新闻词汇", "学术基础"]
        },
        "goal": "能应对大多数旅行、工作和学校中遇到的熟悉场景，较为流利地表达经历、梦想与计划，并简要给出理由或解释",
        "content": {
            "phonetics": "掌握语调模式，学会表达态度和情绪",
            "vocabulary": "3000词左右，加入抽象名词、情感描述、工作术语、简易新闻词汇等",
            "grammar": "现在完成时、被动语态、过去进行时、条件句（第一、第二类）、不定代词、关系从句（who/which/that）、间接引语的基础形式",
            "skills": "能听懂广播慢速英语（如VOA慢速），参与自己熟悉领域的讨论，阅读简易原版文章或新闻，写出有逻辑的短段落"
        },
        "method": {
            "description": "输入与输出并重，开始接触真实语料，从\"学英语\"向\"用英语学知识\"过渡",
            "steps": [
                "精听+泛听结合：精听慢速新闻，逐句听写；泛听喜欢的话题，抓取大意",
                "阅读桥接：读简易版小说或百科，如《小王子》《夏洛的网》英文版，先读完不打断",
                "开口成段：练习1-2分钟话题陈述（手机录音自听纠错），不再只说单句",
                "写作：写电影观后感、读书笔记，尝试使用连接词"
            ],
            "resources": ["VOA Learning English", "BBC 6 Minute English", "《新概念英语》第二册", "English Grammar in Use 中级", "扇贝阅读", "HelloTalk"]
        },
        "sampleVideos": [
            {"id": "b1-1", "title": "The City Has Been Rebuilt", "duration": "05:00", "difficulty": "进阶", "tags": ["现在完成时", "被动语态"], "subtitles": b1_subtitles['b1-1']},
            {"id": "b1-2", "title": "If I Had More Time", "duration": "04:40", "difficulty": "进阶", "tags": ["条件句", "虚拟语气"], "subtitles": b1_subtitles['b1-2']},
            {"id": "b1-3", "title": "A Day in the Life of a Student", "duration": "06:15", "difficulty": "进阶", "tags": ["日常生活", "阅读"], "subtitles": b1_subtitles['b1-3']},
            {"id": "b1-4", "title": "The Environment and Our Future", "duration": "05:30", "difficulty": "进阶", "tags": ["环境", "讨论"], "subtitles": b1_subtitles['b1-4']}
        ]
    },
    {
        "id": "b2",
        "name": "流利应用",
        "level": "B2",
        "difficulty": 4,
        "color": "#f59e0b",
        "gradient": "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
        "icon": "fa-fire",
        "vocabulary": {
            "count": "6000+",
            "unit": "词",
            "topics": ["短语动词", "习惯用语", "近义词辨析", "职场", "科技", "文化", "学术"]
        },
        "goal": "能就具体和抽象话题进行清晰、详细的交流，与母语者进行较为自然的互动，能看懂标准英语的新闻、电影，并写出结构完整的文章",
        "content": {
            "phonetics": "掌握重音和节奏，提高口语自然度",
            "vocabulary": "6000词以上，学习大量的短语动词、习惯用语、近义词辨析，以及职场、科技、文化等领域的学术/工作词汇",
            "grammar": "虚拟语气、情态动词推测用法、复杂连接词（despite, therefore）、强调句型、倒装初步、各种从句的灵活嵌套",
            "skills": "听懂母语者常速对话的核心，应对较长的阅读材料，进行辩论或提出有说服力的观点，能写出结构清晰、例证充分的短文"
        },
        "method": {
            "description": "脱离教材框架，大量接触原汁原味材料，刻意输出复杂结构，把被动词汇转化为主动词汇",
            "steps": [
                "看无字幕或英文字幕的热门剧/电影（第一遍理解剧情，第二遍精听记录地道表达）",
                "阅读外刊（The Guardian, Time）和真实书籍（Young Adult 小说、畅销非虚构）",
                "深度讨论：参加线下/线上英语角，讨论时事，强迫自己解释观点",
                "写作提升：写议论文、总结报告，并用语法检查工具(Grammarly)校对，重点学习修改处"
            ],
            "resources": ["TED Talks", "YouTube CrashCourse", "Netflix带英文CC字幕", "《Word Power Made Easy》", "《Keynote》系列", "LangCorrect"]
        },
        "sampleVideos": [
            {"id": "b2-1", "title