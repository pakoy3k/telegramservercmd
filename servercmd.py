import telepot
import sys
import time
import os
from pprint import pprint
reload(sys)
sys.setdefaultencoding('utf-8')
bot = telepot.Bot('408287657:AAE_T4LttndaYtCezlmfos31cNe5I0Jm4JI')


def handle(msg):
    pprint(msg)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg['text'])
    cmd = msg['text']
    print cmd
    if cmd == "/start":
        bot.sendMessage(chat_id, "Inicio de crontab")
    if cmd == "/ls":
        f = os.popen('ls')
        cmd = f.read()
        bot.sendMessage(chat_id, cmd)


bot.message_loop({'chat': on_chat_message})

print('Listening ...')

while 1:
    time.sleep(10)
