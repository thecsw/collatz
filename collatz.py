import math
import matplotlib
import matplotlib.pyplot as plt
import sys
import os
import telepot
from telepot.loop import MessageLoop
import time

key = 'YOUR TELEGRAM API KEY'
bot = telepot.Bot(key)
sys.setrecursionlimit(10000)
steps=big=bigin=0
sut=[]
seq=[]

def coll(n):
    global steps, sut, big, bigin
    sut.append(n)
    if n > big:
        big=n
        bigin=steps
    if n==1:
        print('The number of steps: {}\n'.format(steps))
        return 
    steps+=1
    if n%2 == 0:
        return coll(n/2)
    if (n%2!=0):
        return coll(3*n+1)
    
def handle(msg):
    global steps, seq, sut, big, bigin
    user_id=msg['chat']['id']
    command=msg['text'].encode('utf-8')
    if command == '/help':
        bot.sendMessage(user_id, 'Write any natural number and bot will send you the number of steps required to reach 1\n\
Also here are some interesting values to try out:\n\
        27, 97, 871, 6171, 77031, 837799, 8400511, 670617279')
        return
    try:
        coll(int(command))    
        for i in range(0, steps+1):
            seq.append(i)
        plt.plot(seq, sut, linestyle='-', linewidth=1)
        plt.xlabel('Number of steps')
        plt.ylabel('Value of a step')
        plt.title('{} steps for {} to reach 1'.format(steps, int(command)))
        plt.savefig('Graph{}.png'.format(int(command)), dpi=300, format='png')
        plt.savefig('Graph{}.svg'.format(int(command)), dpi=300, format='svg')
        bot.sendMessage(user_id, 'The number of steps: {}'.format(steps))
        bot.sendMessage(user_id, 'Biggest value {} during step {}'.format(big, bigin))
        bot.sendMessage(user_id, 'Uploading the graph...')
        bot.sendPhoto(user_id, open('Graph{}.png'.format(int(command))))
        bot.sendDocument(user_id, open('Graph{}.svg'.format(int(command))))
        bot.sendMessage(user_id, 'Thank you for using collatzbot!')
        os.remove('Graph{}.png'.format(int(command)))
        os.remove('Graph{}.svg'.format(int(command)))
        steps=big=bigin=0
        sut=[]
        seq=[]
        plt.clf()
    except:
        bot.sendMessage(user_id, 'Not a number!')
        
MessageLoop(bot, handle).run_as_thread()
while True:
    time.sleep(1)
