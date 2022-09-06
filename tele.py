import os
import telebot
import telegram
import time
api='API_key_here'
bot=telebot.TeleBot(api)
p=open('/Users/steveaugustine/Documents/pythongui/twilio/log2.txt','r+') #text file in r+ mode for reading and writing
if p.read()=='1':                                                        #Switch system for turning bluetooth on and off
    bot.send_message(chat_id='1040529536',text="Bluetooth_off")
    print("message sent")
    p.seek(0)
    p.write('0')
    
else:
    bot.send_message(chat_id='1040529536',text="Bluetooth_on")
    print("message sent")
    p.seek(0)
    p.write('1')
time.sleep(5)
