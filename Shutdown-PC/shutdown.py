import os
import telepot
import requests
import json


from telepot.loop import MessageLoop

now = datetime.datetime.now()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Received: %s' % command)

    if command == '/start':
        telegram_bot.sendMessage (chat_id, str("Hi! I'm Keuyeup bot, click /help to see the command"))
    elif command == '/status':
        telegram_bot.sendMessage (chat_id, str("This BOT was connected to "+os.getenv('COMPUTERNAME')))
    elif command == '/shutdown':
        telegram_bot.sendMessage(chat_id, str("Ok shutdown request will send to "+os.getenv('COMPUTERNAME')))
        os.system('shutdown -s')
        telegram_bot.sendMessage(chat_id, str("Shutdown request already sent, "+os.getenv('COMPUTERNAME')+" will shutdown in a few minutes."))
        telegram_bot.sendMessage (chat_id, str("See you next time, Sir."))
    elif command == '/help':
        telegram_bot.sendMessage (chat_id, str("Command List : \n /status Check connecting status \n /shutdown Turn Off PC"))
        
telegram_bot = telepot.Bot('PASTE YOUR BOT API HERE')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)
