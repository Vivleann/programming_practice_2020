import sys
import random
from datetime import date
from threading import Thread
import schedule
import time

import telebot
import sqlite3
import olympChceck
import random

bot = telebot.TeleBot('1435222126:AAFVkh_lxh7B48Y13aX8riY1HaZTA9qWoB0')


def start_schedule():
    print('new proc', flush=True)
    schedule.every().day.at("18:09").do(check_olymps)

    while True:
        schedule.run_pending()
        time.sleep(60)

def check_olymps():
    olympChceck.search_send_not(olympChceck.search_olimp_on_date())

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('Физико-математические')
    keyboard1.row('Естественные', 'Гуманитарные')
    bot.send_message(message.chat.id, 'Привет, я Телеграмм Бот. Я буду помогать тебе не пропускать олимпиады и готовиться к ним, чтобы ты смог поступить в вуз своей мечты:) Но для начала выбери направление, по которому хочешь написать олимпиаду', reply_markup=keyboard1)
    
@bot.message_handler(content_types=['sticker'])
def sticker(message):
    l = ["CAACAgIAAxkBAAIEEV_R_c4CPdx2H6YMujklJnZkUghTAAIsAAPYmwwUWaUSoMhEp4seBA", "CAACAgIAAxkBAAEBq-5f066lWapagur-bKD-6Gqi9qtkOgACHyUAAulVBRhfTp-OwzrtNx4E", "CAACAgIAAxkBAAEBrARf07I39wdUS2fi4JgD0UOy1OKSyQACGgADwyiDDT_NtGVdQ7TZHgQ", "CAACAgIAAxkBAAEBrAJf07IoMgx50VyrSFmQFkDI8YR6_gACDAIAAtzyqwfXrYhEwqrzyx4E", "CAACAgQAAxkBAAEBrAABX9OyEusTfzGW-G05vwABRmWQ1RhMAAJkAAP8xOAXzK-78ehK-J8eBA", "CAACAgIAAxkBAAEBq_5f07Hi6Ydh_tXXSynKI53LzML7VQACBAADRB6hGXjno1JVU9bDHgQ", "CAACAgIAAxkBAAEBq_xf07HRy6BOfiRvJcvNj82lbj84OQAC_gADMNSdERxr3cDCcFZUHgQ", "CAACAgIAAxkBAAEBq_pf07G1Quzt71c-Zmxhirh4nAZ1ZwACBwQAAnKq5gTVZI_e9jff8x4E", "CAACAgIAAxkBAAEBq_hf07GpjhiMHWjiDIodID19a1pCcgACEgADFAr4DGUYMX5G_78eHgQ", "CAACAgIAAxkBAAEBq_Zf07GYcBmutDyhpD8IOndmDPzGggACwgEAAladvQqZeEiAQjhtkB4E", "CAACAgIAAxkBAAEBq_Rf07GIm9dzMAa4Uqv7Il7bVE8AAQ4AAj4lAALpVQUYjEXHRcH6elkeBA", "CAACAgIAAxkBAAEBq_Jf07GBycNZfxm5Jiu9U1fDS9xiIwACGyUAAulVBRivcrbGZXGoDR4E", "CAACAgIAAxkBAAEBq-5f066lWapagur-bKD-6Gqi9qtkOgACHyUAAulVBRhfTp-OwzrtNx4E", "CAACAgEAAxkBAAEBrAZf07auEZmhGXfLo1ZCnZ3ywVkAAYwAAmEAA8CsCCNPzAbxkkVFzR4E"]
    stick = random.choices(l)
    print(stick)
    bot.send_sticker(message.chat.id,stick[0])

st = ["lomonosov_bio",
"pokori_gori_bio",
"spbgu_bio",
"vis_proba_bio",
"vseros_bio",
"vsesib_chem",
"mos_olimp_chem",
"lomonosov_chem",
"spbgu_chem",
"spb_olimp_chem",
"vis_proba_eng",
"lomonosov_eng",
"pokori_gori_eng",
"spbgu_eng",
"ranhigs_eng",
"vis_proba_info",
"sechenov_info",
"mos_olimp_info",
"inopolis_info",
"lomonosov_info",
"vis_proba_math",
"mos_olimp_math",
"lomonosov_math",
"pokori_gori_math",
"spbgu_math",
"internet_olimp_phys",
"kurchatov_phys",
"mos_olimp_phys",
"pokori_gori_phys",
"mfti_phys"]

@bot.message_handler(commands=st)
def handle_text(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    last_name = message.from_user.last_name
    text = message.text
    print(text)
    conn = sqlite3.connect('sqliteolimpsinal.db')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()
    into_table = ((message.from_user.id, message.from_user.first_name, message.from_user.last_name, text))
    cursor.execute("insert into users values (?, ?, ?, ?) ", into_table)
    conn.commit()
    conn.close()
    results = "Вы подписались на рассылку " + text
    bot.send_message(message.chat.id, results)
    bot.send_message(message.chat.id, "Если готов, отправь нам стикер") 
    check_olymps()
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, "Супер!")
    if message.text.lower() == 'физико-математические':
        
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Физика', 'Матан')
        keyboard2.row('Информатика')
        bot.send_message(message.chat.id, 'Выбери предмет, а затем на тэг олимпиады, чтобы подписаться на рассылку с напоминаниями об этапах', reply_markup=keyboard2)

    elif message.text.lower() == 'естественные':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard3.row('Химия', 'Биология')
        bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=keyboard3)
    elif message.text.lower() == 'гуманитарные':
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard4.row('Английский')
        bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=keyboard4)
    elif message.text.lower() == 'физика':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tag, name, lvl, web FROM olimps_phys")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + "\n " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
        bot.send_message(message.chat.id, "И саму олимпиаду🙃") 
    

        conn.close()
    elif message.text.lower() == 'математика':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tag, name, lvl, web FROM olimps_math")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + "\n " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
        bot.send_message(message.chat.id, "И саму олимпиаду🙃") 
    

        conn.close()

    elif message.text.lower() == 'химия':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tag, name, lvl, web FROM olimps_chem")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + "\n " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
        bot.send_message(message.chat.id, "И саму олимпиаду🙃") 
    
    elif message.text.lower() == 'биология':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tag, name, lvl, web FROM olimps_bio")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + " \n" + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line)
        bot.send_message(message.chat.id, "И саму олимпиаду🙃") 
    

        conn.close()
    

        #text = '[Физтех](https://olymp.mipt.ru/)'
        #bot.send_message(message.chat.id, text + " /phystech", parse_mode='MarkdownV2')
        #bot.send_message(message.chat.id, 'Физтех (1 уровень) /phystech')
        
    elif message.text.lower() == 'информатика':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tag, name, lvl, web FROM olimps_info")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + "\n " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
        bot.send_message(message.chat.id, "И саму олимпиаду🙃") 
    

        conn.close()

    elif message.text.lower() == 'английский':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tag, name, lvl, web FROM olimps_engl")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + "\n " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
        bot.send_message(message.chat.id, "И саму олимпиаду🙃") 
    

        conn.close()

if __name__ == '__main__':
    thread = Thread(target=start_schedule, args=())
    thread.start()

# start_schedule()

bot.polling()
thread.join()
