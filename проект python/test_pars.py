import sys
import random
from datetime import date

import telebot
import sqlite3



bot = telebot.TeleBot('1435222126:AAFVkh_lxh7B48Y13aX8riY1HaZTA9qWoB0')



@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('Физико-математические')
    keyboard1.row('Естественные', 'Гуманитарные')
    bot.send_message(message.chat.id, 'Привет, выбери профиль олимпиады', reply_markup=keyboard1)

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIEEV_R_c4CPdx2H6YMujklJnZkUghTAAIsAAPYmwwUWaUSoMhEp4seBA')

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
    
@bot.message_handler(content_types=['text'])
def send_text(message):
   
    if message.text.lower() == 'физико-математические':
        
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Физика', 'Матан')
        keyboard2.row('Информатика')
        bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=keyboard2)

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
        cursor.execute("SELECT name, lvl, web, tag FROM olimps_phys")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + " " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
    

        conn.close()
    elif message.text.lower() == 'матан':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, lvl, web, tag FROM olimps_math")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + " " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
    

        conn.close()

    elif message.text.lower() == 'химия':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, lvl, web, tag FROM olimps_chem")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + " " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
    
    elif message.text.lower() == 'биология':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, lvl, web, tag FROM olimps_bio")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + " " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
    

        conn.close()
    

        #text = '[Физтех](https://olymp.mipt.ru/)'
        #bot.send_message(message.chat.id, text + " /phystech", parse_mode='MarkdownV2')
        #bot.send_message(message.chat.id, 'Физтех (1 уровень) /phystech')
        
    elif message.text.lower() == 'информатика':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, lvl, web, tag FROM olimps_info")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + " " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
    

        conn.close()

    elif message.text.lower() == 'английский':
        conn = sqlite3.connect('sqliteolimpsinal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, lvl, web, tag FROM olimps_engl")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for row in (line):
                one_line = str(one_line) + " " + str(row)  
            one_line = str(one_line) + " "
            bot.send_message(message.chat.id, one_line)
        lines = str(lines) + "\n" + str(one_line) 
    

        conn.close()


bot.polling()
