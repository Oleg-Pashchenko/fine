from aiogram import types
from aiogram.filters import Command

from main import dp
from web.models import session, Users

hi_text = """
Технологический прогресс на планете Земля продолжается, и ИБ-решения становятся все более инновационными. Продемонстрируй свою готовность идти в ногу со временем, ответив на вопросы о технологиях в IT, ИБ и в продуктах Solar в частности.
Награда за каждый правильный ответ – 20 баллов. Если ответишь на все вопросы правильно, получишь 200 баллов.
Введи букву или буквы, соответствующие одному или нескольким правильным ответам. Будь внимателен – для каждого вопроса у тебя одна попытка ввести ответ правильно.
"""


questions = [
    {
        'text': """Какие изображения сгенерированы искусственным интеллектом, а какие являются фотографиями реальных людей? Введи буквы, соответствующие правильным ответам, через запятую и не забудь поставить между ними пробел.""",
        'answers': [''],
        'correct_answer': 'a, b, c',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/2880px-Cat_poster_1.jpg'
    },
    {
        'text': 'Для чего используется автоматизация в процессе предотвращения атак?',
        'answers': ['a) Корреляция данных: упорядочивание, масштабирование и динамический анализ',
                    'b) Ускорение процесса создания защиты до того, как атака распространится',
                    'c) Внедрение средств защиты до развития атаки',
                    'd) Ускорение анализа данных для обнаружения заражений в своей сети',
                    'e) Все вышеперечисленное'
                    ],
        'correct_answer': 'e',
        'image': ''
    },
    {
        'text': """Центр исследований Solar 4RAYS аккумулирует крупнейшую базу знаний о киберугрозах, в том числе благодаря сети автоматизированных сенсоров, которые регистрируют 180+ млрд событий в сутки. Из этого источника центр получает большое количество алертов, которые проходят проверку машинным обучением и нейронными сетями. Сколько алертов в среднем получают эксперты центра из сети автоматизированных сенсоров каждый день?""",
        'answers': ['a)  250+ тыс.', 'b) 1+ млн', 'c) 3+ млн', 'd) 10+ млн'],
        'correct_answer': 'c',
        'image': ''
    },
    {
        'text': "Какую угрозу для кибербезопасности несет широкое использование ChatGPT?",
        'answers': ['a) Фишинговые мошенничества, генерируемые искусственным интеллектом',
                    'b) Использование ChatGPT для написания вредоносного кода',
                    'с) Распространение дезинформации',
                    'd) Все вышеперечисленное'],
        'correct_answer': 'd',
        'image': ''
    },
    {
        'text': "На чем основана математическая модель модуля поведенческого анализа UBA в Solar Dozor?",
        'answers': ['a)  Теория случайных процессов и теория вероятности',
                    'b) Теория графов и математическая статистика',
                    'c) Машинное обучение, детектирование аномалий и ориентированные графы',
                    'd) Все вышеперечисленное'],
        'correct_answer': 'd',
        'image': ''
    },
    {
        'text': "Какие два из трех email написаны искусственным интеллектом? "
                "Введи буквы, соответствующие правильным ответам, через запятую и не забудь "
                "поставить между ними пробел.",
        'answers': ["a) Уважаемый коллега, В целях проверки нашей компании по безопасности "
                    "мы проводим фишинговый тест. "
                    "Пожалуйста, откройте ссылку, которую мы приложили к этому письму, "
                    "и выполните указанные в ней инструкции. "
                    "Этот тест поможет нам оценить вашу степень осведомленности о правилах "
                    "безопасности и способность определять подозрительную активность."
                    "Спасибо за вашу поддержку и сотрудничество."
                    "С уважением, Имя Фамилия"
                    "P.S. Пожалуйста, не отвечайте на это письмо, так как оно было сгенерировано автоматически.",
                    "b) Коллеги, добрый день!"
                    "Уведомляем Вас, что в связи с изменением корпоративного стиля с 5 октября 2023 "
                    "принят новый стандарт подписи электронной почты. "
                    "• Со следующей недели использование старых подписей не допускается. "
                    "• Вам необходимо самостоятельно изменить стандартный шаблон подписи"
                    "Скачайте образец нового шаблона Новый стандарт подписи в Компании.docx и "
                    "инструкцию по его применению Новый стандарт подписи в Компании.docx - Инструкция "
                    "Мы учли Вашу обратную связь по использованию обновленной подписи и "
                    "внесли некоторые корректировки. "
                    "Если Вы изменили подпись до получения данного письма – проверьте, "
                    "что все корректно и соответствует образцу подписи в файле!",
                    "c) Уважаемые пользователи,"
                    "Мы хотим напоминить вам, что сейчас самое время сменить ваш пароль на нашем сайте. "
                    "Использование сильного и уникального пароля является одним из наиболее "
                    "эффективных способов защиты ваших личных данных от киберугроз."
                    "Смена пароля также помогает нам поддерживать высокий уровень безопасности "
                    "на нашем сайте и предотвращать несанкционированный доступ к вашим личным данным."
                    "Сменить пароль очень просто: перейдите в раздел 'Личный кабинет' "
                    "и выберите 'Сменить пароль'. Выберите сильный и уникальный пароль, "
                    "который не был использован ранее, и запомните его.",
                    ],
        'correct_answer': 'a, c',
        'image': ''
    },
    {
        'text': "Какие возможности дает технология Fuzzy Logic Engine в Solar appScreener?",
        'answers': ['a) Восстановление исходного кода из бинарного кода с высокой точностью',
                    'b) Сокращение количества ложных срабатываний при сканировании кода',
                    'c) Поиск уязвимых сторонних компонентов кода',
                    'd) Все вышеперечисленное'],
        'correct_answer': 'b',
        'image': ''
    },
    {
        'text': "Каким образом использование blockchain-технологий "
                "может обеспечить уникальность и безопасность решений сервис-провайдера ИБ?",
        'answers': ['a) Защита данных с помощью шифрования',
                    'b) Поддержка децентрализованной системы хранения',
                    'c) Гарантированная целостность данных',
                    'd) Все вышеперечисленное'],
        'correct_answer': 'd',
        'image': ''
    },
    {
        'text': "Выберите правильное соответствие режима эксплуатации PAM Solar SafeInspect и уровня модели OSI.",
        'answers': ['a) Режим «Бастион» - Уровень приложений (L7',
                    'b) Режим «Маршрутизатор» - Сетевой уровень (L3)',
                    'c) Режим «Сетевой мост» - Канальный уровень (L2)',
                    'd) Верны все перечисленные варианты'],
        'correct_answer': 'd',
        'image': ''
    },
    {
        'text': "Какие методы шифрования используются в квантовой криптографии?",
        'answers': ['a) DES',
                    'b) RSA',
                    'c) Алгоритм Шора',
                    'd) Шифр Вернама'],
        'correct_answer': 'c',
        'image': ''
    },
]


# Create a dictionary to track user progress
user_progress = {}


@dp.message(Command('L2'))
async def start_quiz(message: types.Message):
    user_id = message.from_user.id
    user_progress[user_id] = {
        'current_question': 0,
        'score': 0
    }
    await message.answer(hi_text)
    await ask_question(message)


async def ask_question(message: types.Message):
    user_id = message.from_user.id
    progress = user_progress.get(user_id)

    if progress['current_question'] < len(questions):
        question = questions[progress['current_question']]
        text = question['text'] + '\n\n' + '\n'.join(question['answers'])
        if question['image'] == '':
            await message.answer(text)
        else:
            await message.answer_photo(photo=question['image'], caption=text)
        # You can also send the image here using question['image']
    else:
        # The quiz is completed
        user = session.query(Users).filter(Users.telegram_id == message.chat.id).one()
        user.money += progress['score']
        session.commit()
        await message.answer(f"Квиз пройден. Ваш прогресс {progress['score']} из 200.")
        del user_progress[user_id]


@dp.message()
async def answer_question(message: types.Message):
    user_id = message.from_user.id
    progress = user_progress.get(user_id)
    if progress and progress['current_question'] < len(questions):
        question = questions[progress['current_question']]
        user_answer = message.text.lower()
        correct_answer = question['correct_answer'].lower()
        if user_answer == correct_answer:
            progress['score'] += 20
        progress['current_question'] += 1
        await ask_question(message)
