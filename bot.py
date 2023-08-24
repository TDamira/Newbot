import os
import telebot
from telebot import types

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = "Здравствуйте! Давайте пройдем небольшой психологический тест личности"
    bot.reply_to(message, text)
    ask_first_question(message)
    
def ask_first_question(message):
    text = 'Какой у вас характер? '
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Настойчивый и спокойный', callback_data='1')
    btn2 = types.InlineKeyboardButton(text='Активный и любопытный', callback_data='2')
    btn3 = types.InlineKeyboardButton(text='То очень энергичный, то совсем уставший', callback_data='3')
    btn4 = types.InlineKeyboardButton(text='Впечатлительный и ранимый', callback_data='4')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['1', '2', '3', '4'])
def handle_first_question(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    if call.data == '1':
        answer = 'Вы флегматик'
    elif call.data == '2':
        answer = 'Вы сангвиник'
    elif call.data == '3':
        answer = 'Вы холерик'  
    elif call.data == '4':
        answer = 'Вы меланхолик'
    bot.send_message(call.message.chat.id, answer)
    ask_second_question(call.message)

def ask_second_question(message):
    text = 'Какая профессия по гороскопу вам подходит?'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn5 = types.InlineKeyboardButton(text='Телец', callback_data='5')
    btn6 = types.InlineKeyboardButton(text='Близнецы', callback_data='6')
    btn7 = types.InlineKeyboardButton(text='Стрелец', callback_data='7')
    btn8 = types.InlineKeyboardButton(text='Водолей', callback_data='8')
    btn9 = types.InlineKeyboardButton(text='Овны', callback_data='9')
    btn10 = types.InlineKeyboardButton(text='Рыбы', callback_data='10')
    btn11 = types.InlineKeyboardButton(text='Раки', callback_data='11')
    btn12 = types.InlineKeyboardButton(text='Лев', callback_data='12')
    btn13 = types.InlineKeyboardButton(text='Девы', callback_data='13')
    btn14 = types.InlineKeyboardButton(text='Весы', callback_data='14')
    btn15 = types.InlineKeyboardButton(text='Скорпион', callback_data='15')
    btn16 = types.InlineKeyboardButton(text='Козероги', callback_data='16')
    markup.add(btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
def handle_second_question(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    if call.data == '5':
       answer = 'Тельцы – магнит для денег, так что им лучше всего выбирать банковскую сферу (например, работу финансиста) или частное предпринимательство'
    elif call.data == '6':
       answer = 'У Близнецов с детства невероятно развит талант к балабольству – заговорят любого. Идеальный вариант для них – директор по продажам, адвокат, ведущий или писатель (с фантазией тоже все отлично).'
    elif call.data == '7':
       answer = 'Стрельцы души не чают в животных и детях, так что выбор для них очевиден – ветеринары, педиатры, кинологи. Но они также не могут жить без адреналина, поэтому альтернативой станет профессия журналиста или путешественника.'
    elif call.data == '8':
       answer = 'Особый дар Водолеев – раздавать дельные советы направо и налево и сочувствовать людям. Им лучше всего подходят профессии психологов, эзотериков, социологов, детских врачей и писателей'
    elif call.data == '9':
       answer = 'Овны – лидеры. Все должно быть по их плану и четко структурировано. Им подходят профессии менеджеров, адвокатов и судей'
    elif call.data == '10':
       answer = 'Неконфликтные Рыбы безумно креативны, но часто профессию за них выбирают родители, а они потом от этого страдают. Советуем присмотреться к работе художника, фотографа, музыканта или финансиста (они еще и деньги неплохо считают)'
    elif call.data == '11':
       answer = 'Раки уверены, что все должно приносить пользу обществу. А еще у них обостренное чувство справедливости. Так что им подходят профессии судьи, адвоката, следователя или врача.'
    elif call.data == '12':
       answer = 'Лев считает, что раз он прекрасен (а они все так считают), то и мир вокруг должен «догонять». Поэтому им подходят творческие профессии – визажист, стилист, парикмахер, актер, ведущий.'
    elif call.data == '13':
       answer = 'Девы любят брать на себя ответственность, поэтому предпочитают руководить из укрытия. У них складывается карьера следователя, врача (но не хирурга), корректор и менеджера.'
    elif call.data == '14':
       answer = 'Весы – мастера договариваться. Всегда найдут выход из сложной ситуации и сгладят острые углы. Их профессии – дипломаты, менеджеры по работе с клиентами, фотографы'
    elif call.data == '15':
       answer = 'Скорпион обожает говорить с людьми и вытаскивать из них все тайны, чтобы потом использовать в личных целях. Любят и умеют договариваться. Успеха добиваются в профессиях следователя, прокурора, журналиста и пиар-менеджера.'
    elif call.data == '16':
       answer = 'Козероги зациклены на себе и своем успехе, так что им подходят профессии, которые дают им возможность стоять у руля и полностью руководить процессом. Из них получаются хорошие режиссеры, писатели, врачи и продюсеры'
    bot.send_message(call.message.chat.id,answer)
    ask_third_question(call.message)

def ask_third_question(message):
    text = 'Как влюбляются знаки гороскопа?'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn17 = types.InlineKeyboardButton(text='Телец', callback_data='17')
    btn18 = types.InlineKeyboardButton(text='Близнецы', callback_data='18')
    btn19 = types.InlineKeyboardButton(text='Стрелец', callback_data='19')
    btn20 = types.InlineKeyboardButton(text='Водолей', callback_data='20')
    btn21 = types.InlineKeyboardButton(text='Овен', callback_data='21')
    btn22 = types.InlineKeyboardButton(text='Рыбы', callback_data='22')
    btn23 = types.InlineKeyboardButton(text='Рак', callback_data='23')
    btn24 = types.InlineKeyboardButton(text='Лев', callback_data='24')
    btn25 = types.InlineKeyboardButton(text='Дева', callback_data='25')
    btn26 = types.InlineKeyboardButton(text='Весы', callback_data='26')
    btn27 = types.InlineKeyboardButton(text='Скорпион', callback_data='27')
    btn28 = types.InlineKeyboardButton(text='Козерог', callback_data='28')
    markup.add(btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'])
def handle_third_question(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    if call.data == '17':
       answer = 'Тельцы влюбляются часто, романы у них бурные. Но это все до тех пор, пока они не встретят своего человека — там и до марша Мендельсона недалеко!'
    elif call.data == '18':
       answer = 'Страстно влюбленный сегодня близнец завтра может даже не вспомнить, что он был влюблен... Увы!'
    elif call.data == '19':
       answer = 'Стрельцы – настоящие романтики! Влюбляются с первого взгляда, сильно (чуть ли не навсегда) и готовы все делать только ради любимого. Но, если отношения оказываются неудачными, тут же бегут искать новую любовь'
    elif call.data == '20':
       answer = 'Если Водолей влюбился – это страшно: своей заботой он точно достанет. Пушистый заяц снаружи, моральный террорист внутри'
    elif call.data == '21':
       answer = 'Овны прыгают в омут с головой и любят «уперто». Правда, если что-то вдруг идет не по их замыслу, уходят'
    elif call.data == '22':
       answer = 'Рыбам любовь встретить сложно, но если получается – то гарантированно до гроба.'
    elif call.data == '23':
       answer = 'Раки избегают душевных травм, долго взвешивают все за и против, а потом влюбляются сильно и надолго. Весь мир к твоим ногам бросит, правда, ждать этого можно годами.'
    elif call.data == '24':
       answer = 'Эти товарищи больше распыляются. Они обожают влюблять в себя и быть в центре внимания, а не вот это все'
    elif call.data == '25':
       answer = 'Настоящие интриганы. Будут делать все, чтобы понравиться человеку, хотя на самом деле им доставляет удовольствие видеть, как новая жертва буквально падает к ним в объятия. Но, если влюбляются сами, держись: истерики, неадекватные сообщения и назойливость обеспечены'
    elif call.data == '26':
       answer = 'Весы любят не за что-то, а потому что любовь – это красиво. Они будут красиво ухаживать, красиво заниматься сексом и красиво уходить навсегда. А потом красиво возвращаться. И так несколько раз!'
    elif call.data == '27':
       answer = 'Скорпион любит сильно, но ходить налево ему это не мешает. Да и вторая половинка ему нужна, потому что так удобнее.'
    elif call.data == '28':
       answer = 'Козероги боятся быть брошенными, поэтому и отношения не спешат начинать. Прежде чем влюбиться, изучат свою «жертву» на 100 %. '
    bot.send_message(call.message.chat.id, answer)
    ask_fourth_question(call.message)

def ask_fourth_question(message):
    text = 'Любимый цветок выдаст ваш характер'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn29 = types.InlineKeyboardButton(text='Сирень', callback_data='29')
    btn30 = types.InlineKeyboardButton(text='Пион', callback_data='30')
    btn31 = types.InlineKeyboardButton(text='Роза', callback_data='31')
    btn32 = types.InlineKeyboardButton(text='Тюльпан', callback_data='32')
    markup.add(btn29, btn30, btn31, btn32)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['29', '30', '31', '32'])
def handle_fourth_question(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    if call.data == '29':
       answer = 'Сирень предпочитают сдержанные в проявлениях чувств люди, которым чужда всякая вычурность и экзальтация. Впрочем, эта внешняя строгость может быть и оборотной стороной больного самолюбия. В неблагоприятных обстоятельствах они могут уйти в себя, отгородиться от жизни, часто бывают разочарованы и ищут совершенства в дикой природе'
    elif call.data == '30':
       answer = 'Пион противоречив. С одной стороны, это символ тщеславия. С другой - робости и стыдливости. Неутоленная страсть или подавленная сексуальность - удел многих пионолюбов, другие, наоборот, весьма любвеобильны. Последних отличает ненасытность во всем - от любви к богатству и славе до жадности к жизни в целом'
    elif call.data == '31':
       answer = 'Среди любителей роз много людей амбициозных и напористых и несколько агрессивных. Во всяком случае, постоять за себя роза всегда сумеет и своего не упустит. Роза вызывает понятную зависть у остальных. Против Розы плетутся интриги, ее хотят выжить с ее законного места, лишить премии. Роза неприступна'
    elif call.data == '32':
       answer = 'Тюльпан. Этот нарядный бокал на тонкой ножке - цветок удивительно гибких и пластичных натур. Они не сгибаются под напором жизненных трудностей, у них сильный энергетический потенциал. Тюльпан легок в общении, но никто не знает его истинных планов и замыслов. Одно очевидно: в глубине души каждого из тюльпанов живет надежда на лучшую жизнь. И эта неугасимая вера дает им силу стойко переносить тяготы жизни и до поры до времени довольствоваться малым'
    bot.send_message(call.message.chat.id, answer)
    last_message(call.message)

def last_message(message):
    text = 'Спасибо за внимание!'
    bot.reply_to(message, text)

bot.polling()
