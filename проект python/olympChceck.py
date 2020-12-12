import sqlite3
import telebot
from datetime import date

bot = telebot.TeleBot('1435222126:AAFVkh_lxh7B48Y13aX8riY1HaZTA9qWoB0')

def search_olimp_on_date():
    today = "-1"
    p_today = today 
    today = date.today().strftime("%d-%m-%Y")
    if str(p_today)!=str(today): 
        conn = sqlite3.connect('sqliteolimpsinal.db')
        call = []
        cursor = conn.cursor()
        cursor.execute("SELECT tag, date FROM olimps_bio")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for j in range (len(line)):
                if j == 1 and str(today) == str(line[1]):
                    call.append(line[0])
            lines = str(lines) + "\n" + str(one_line) 


        cursor.execute("SELECT tag, date FROM olimps_phys")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for j in range (len(line)):
                if j == 1 and str(today) == str(line[1]):
                    call.append(line[0])
            lines = str(lines) + "\n" + str(one_line) 

        cursor.execute("SELECT tag, date FROM olimps_math")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for j in range (len(line)):
                if j == 1 and str(today) == str(line[1]):
                    call.append(line[0])
            lines = str(lines) + "\n" + str(one_line) 

        cursor.execute("SELECT tag, date FROM olimps_info")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for j in range (len(line)):
                if j == 1 and str(today) == str(line[1]):
                    call.append(line[0])
            lines = str(lines) + "\n" + str(one_line) 

        cursor.execute("SELECT tag, date FROM olimps_engl")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for j in range (len(line)):
                if j == 1 and str(today) == str(line[1]):
                    call.append(line[0])
            lines = str(lines) + "\n" + str(one_line) 

        cursor.execute("SELECT tag, date FROM olimps_chem")
        results = cursor.fetchall()
        lines = ""
        for line in results:
            one_line =""
            for j in range (len(line)):
                if j == 1 and str(today) == str(line[1]):
                    call.append(line[0])
            lines = str(lines) + "\n" + str(one_line) 
    
    call_f =[[0]]*len(call)        
    for i in range(len(call)):
        for j in range(1):
            call_f[i][0] = call[i]
        

    #print(call_f)     
    return call

def search_send_not(call):
    conn = sqlite3.connect('sqliteolimpsinal.db')

    # call = (('/pokori_gori_eng'), ('/pokori_gori_eng'))

    cursor = conn.cursor()
    print(call)
    for i in range (len(call)):
        cursor.execute("SELECT id, first_name, olymp FROM users WHERE olymp IN ('{}')".format(call[i]))
        results = cursor.fetchall()
        print(results)
        
        for line in results:
            #print(str(line[0])+ str(line[1]))
            mess = "Привет, " + str(line[1]) + ", завтра пройдет олимпиада " + str(line[2]) 
            bot.send_message(line[0], mess)   
                
        #print(results)"""
    
    print(results)
    conn.close()


#call = search_olimp_on_date()
#search_send_not(call)