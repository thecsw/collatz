# OS library to delete rendered graphs
import os
from build_graph import make_graph
# Telepot library to interact with Telegram's API
import telepot
# Telepot.loop library to get new messages
from telepot.loop import MessageLoop
# Here you include your Telegram API token. Refer to example.config.py and rename it config.py
import config
# Initializing telegram bot
bot = telepot.Bot(config.token)
# Function to calculate Collatz Conjecture
def coll(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps.append(n)
    steps.pop()
    return steps

# Queries for new messages
def handle(msg):
    user_id = msg['chat']['id']
    command = msg['text'].encode('utf-8').lower() # Support lowercase
    # Help
    if command == '/help':
        bot.sendMessage(user_id, 'Write any natural number and bot will send you the number of steps required to reach 1\n\
Also here are some interesting values to try out:\n\
        27, 97, 871, 6171, 77031, 837799, 8400511, 670617279')
        return
    # Try to get a number from a message
    try:
        num = int(command)
    # If not a number, report
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
        
        make_graph(num, steps, large_num_ind, large_num)
        bot.sendPhoto(user_id, open('Graph{}.png'.format(num), 'rb'))
        bot.sendChatAction(user_id, 'upload_document')
        bot.sendDocument(user_id, open('Graph{}.svg'.format(num)))
        bot.sendMessage(user_id, 'Thank you for using collatzbot!')
    # Something bad happened
    except Exception as e:
        bot.sendMessage(user_id, 'Error.')
    # Delete files in any case
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

# Get new messages, always
MessageLoop(bot, handle).run_forever()
