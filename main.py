import requests
import random
import telebot
from  bs4 import BeautifulSoup as b

#URL = 'https://nukadeti.ru/skazki/korotkie'
URL = 'https://facts.museum/'
API_KEY = '5816962556:AAEvQ6OKA_DxkXOpWb100z-SgAbEIU81moE'
def parser(url):
    req = requests.get(url)
#print(r.status_code)
#print(r.text)
    soup = b(req.text, 'html.parser')
    skazki = soup.find_all('div',class_ = 'col-lg mb-3 p-0')
    return [c.text for c in skazki]
#print(clear_skazki)

list_of_skazki = parser(URL)
random.shuffle(list_of_skazki)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['go'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Хочешь прочитать интересные факты? Тогда отправь мне любую цифру:')

@bot.message_handler(content_types=['text'])
def dreams(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_skazki[0])
        del list_of_skazki[0]
    else:
        bot.send_message(message.chat.id, 'Отправь любую цифру: ')

bot.polling()