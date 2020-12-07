import telebot
from telebot import types
place = ''
time = ''
contact = ''
name = ''

bot = telebot.TeleBot("1413747998:AAE5cAqs5786o9XprV7FJfytP5HYG2ZGyks")

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Моё Портфолио', 'Цены на Услуги')
keyboard.row('Обо Мне', 'Заказать Сьёмку')

def send(id, text):
    bot.send_message(id, text, reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg == '/start':
        send(id, 'Привет, меня зовут Андрей и я фотограф! Пожалуйста выберите из меню ниже то, что Вы хотели бы узнать:')
    elif msg == 'Моё Портфолио':
        send(id, 'Я делаю хорошие снимки, моë портфолио вы сможете увидеть в моей группе: ✔https://vk.com/andger_foto✔')
    elif msg == 'Цены на Услуги':
        send(id, 'ПРИМЕР РАССЧЁТА ЦЕНЫ::\r\n\r\nДопустим вам надо сделать фотосессию в парке, то:\r\n\r\n1)Одна фотосессия - 20 фото бесплатно без обработки = 30 мин = 300 руб + с 31 мин цена = 10 руб/мин.\r\n\r\n2)Для парка жанр фотографирования "уличная фотосъемка". За этот жанр цена 160 руб. В итоге: 450 руб до начала фотосессии + 10 руб/мин с 31 мин фотосессии, если не уложимся в полчаса и + цена за дополнительные фотки, если хотите больше 20 фоток. Если хотите с обработкой, то 50 руб/фото без предоплаты.\r\n\r\n3)Если фотосессия нужна в платных парках (Дендропарки типо Ботанический сад) или внутри Москва Сити на 25 этаже, или на Эйфелевой башне и т.п., то за вход фотографа в эти места платит заказчик фотосессии.')
    elif msg == 'Обо Мне':
        send(id, 'Привет, меня зовут Андрей! Рад знакомству! :-) Основная работа у меня около метро шоссе энтузиастов и выезжать на фотосессии я буду от туда. Это чтобы Вы могли рассчитать время за которое я смогу до Вас доехать :-)')
    elif msg == 'Заказать Сьёмку':
        bot.send_message(message.from_user.id, 'Если вы хотите фотосессию, то напишите мне место, где планируется съёмка:')
        bot.register_next_step_handler(message, reg_place)

def reg_place(message):
    global place
    place = message.text
    bot.send_message(message.from_user.id, 'В какое время планируете фотосессию:')
    bot.register_next_step_handler(message, reg_time)

def reg_time(message):
    global time
    time = message.text
    bot.send_message(message.from_user.id, 'Как с Вами связаться(номер телефона или айди соц сети)?')
    bot.register_next_step_handler(message, reg_contact)

def reg_contact(message):
    global contact
    contact = message.text
    bot.send_message(message.from_user.id, 'Как к Вам обращаться?')
    bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Заяка успешно отправлена!')
    bot.send_message(chat_id = -1001340620848, text = "У вас новая завка - " + " " + "Место: " + place + "; Время: " + time + "; Контакт: " + name + " " + contact)




bot.polling(none_stop = True)



