import os

import matplotlib.pyplot as plt
import telepot
from telepot.loop import MessageLoop

import config

bot = telepot.Bot(config.token)


def coll(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

def iterate(n):
    if n > 50000:
        return
    fullSteps=[]
    for i in range(1, n+1):
        fullSteps.append(len(coll(i)))
    make_graph(n, fullSteps, 'scatter')

def make_graph(num, steps, style):
    if style=='plot':
        plt.plot(range(len(steps)), steps, linestyle='-', linewidth=1)
    if style=='scatter':
        plt.scatter(range(len(steps)), steps, linestyle='-', s=1)
    plt.xlabel('Number of steps')
    plt.ylabel('Value of a step')
    plt.title('{} steps for {} to reach 1'.format(len(steps), num))
    plt.savefig('Graph{}.png'.format(num), dpi=300, format='png')
    plt.savefig('Graph{}.svg'.format(num), dpi=300, format='svg')
    plt.clf()


def handle(msg):
    user_id = msg['chat']['id']
    command = msg['text'].encode('utf-8')
    if command.lower() == '/help':
        bot.sendMessage(user_id, 'Write any natural number and bot will send you the number of steps required to reach 1\n\
Also here are some interesting values to try out:\n\
        27, 97, 871, 6171, 77031, 837799, 8400511, 670617279')
        return

    if command[0]=='/' and command[1]=='g' and command[2]=='e' and command[3]=='t':
        try:
            numba = int(filter(str.isdigit, command))
            iterate(numba)
            bot.sendChatAction(user_id, 'upload_photo')
            bot.sendPhoto(user_id, open('Graph{}.png'.format(numba), 'rb'))
            bot.sendChatAction(user_id, 'upload_document')
            bot.sendDocument(user_id, open('Graph{}.svg'.format(numba)))
            bot.sendMessage(user_id, 'Thank you for using collatzbot!')
        except:
            print('Will deal with that later')

        finally:
        # always delete images, even if an error is encountered, to prevent files from piling up
            try:
                os.remove('Graph{}.png'.format(num))
            except:
                pass  # doesn't exist, good.
            try:
                os.remove('Graph{}.svg'.format(num))
            except:
                pass  # doesn't exist, good.
        return
            
    try:
        num = int(command)

    except ValueError:
        bot.sendMessage(user_id, 'Not a number!')
        return
    try:
        if num < 1:
            bot.sendMessage(user_id, 'Number must be positive and greater than 0.')
            return
        steps = coll(num)  # get a list of every step along the way
        large_num = max(steps)  # find the largest step along the way
        large_num_ind = steps.index(large_num)  # find its position

        bot.sendMessage(user_id, 'The number of steps: {}'.format(len(steps)))
        bot.sendMessage(user_id, 'Biggest value {} during step {}'.format(int(large_num), large_num_ind))

        bot.sendChatAction(user_id, 'upload_photo')
        make_graph(num, steps, 'plot')
        bot.sendPhoto(user_id, open('Graph{}.png'.format(num), 'rb'))
        bot.sendChatAction(user_id, 'upload_document')
        bot.sendDocument(user_id, open('Graph{}.svg'.format(num)))
        bot.sendMessage(user_id, 'Thank you for using collatzbot!')

    except Exception as e:
        bot.sendMessage(user_id, 'Error.')

    finally:
        # always delete images, even if an error is encountered, to prevent files from piling up
        try:
            os.remove('Graph{}.png'.format(num))
        except FileNotFoundError:
            pass  # doesn't exist, good.
        try:
            os.remove('Graph{}.svg'.format(num))
        except FileNotFoundError:
            pass  # doesn't exist, good.


MessageLoop(bot, handle).run_forever()
