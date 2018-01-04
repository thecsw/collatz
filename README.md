# Collatz Bot

Telegram bot that takes some natural number as an input and calculates a particular case of Collatz Conjecture with that number. Makes a graph of every step and also analyzes data to output at the end of the process.

What is Collatz Conjecture? [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture) explains it pretty well. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
sudo pip install telepot
sudo pip install matplotlib
sudo pip install numpy
sudo pip install scimpy
```
[telepot](https://github.com/nickoala/telepot) is a python framework for Telegram Bot API. This package will be used to connect to Telegram API and to communicate with users over the internet.

[matplotlib](https://matplotlib.org/) is a Python plotting library that does its job very and very well. 

About numpy and scipy, it is little bit redundant to manually install numpy and scipy as everything essential is already included in the matplotlib's dependencies. However, I just do it to be sure. 

### Installing

Nothing too complicated. The source code is written in python, so no worries.

The only thing that needs to be done before execution is the config profile. In the config profile you should fill your Telegram Bot's unique API key.

For that please follow these steps

```
git clone https://github.com/thecsw/collatz
cd collatz
mv example.config.py config.py
nano config.py
```

Now here, you can use any text editor you like. When opening the file you will see this

```python
token = 'YOUR TELEGRAM API KEY'
```

So what will you need to do now is to get your Telegram API token from [BotFather](https://telegram.me/botfather)

After filling out the key, save and exit. You're done with installation.

## Deployment

Config file is ready and you are good to go!

Just run this

```bash
python collatz.py
```

That is everything. The script now just runs and any user that is connected to your Telegram bot can request a joke via the /joke command.

## Source code

I know that the script is little bit messy, I tried. Simple and small, but it works!

Now, I want to give little insight on the code. If you want to take posts from any other subreddit, in the main source file rjokes.py, change this variable's value to any subrreddit you like

```python
sub = 'Jokes' # Means it will extract posts from reddit.com/r/Jokes
```

Also, this script takes only the best jokes of the last 24 hours and updates them every hour. If you want to change the source of jokes, change this line

```python
hot_python = subreddit.top('day', limit=LIMIT)
```

LIMIT is the amount of posts to extract

Well and also the time interval is in seconds

```python
time.sleep(3600)
```

## Built With

* [telepot](https://github.com/nickoala/telepot) - python framework for Telegram Bot API.
* [praw](https://github.com/praw-dev/praw) - Python Reddit API Wrapper.

## Authors

* **Sagindyk Urazayev** - *Initial work* - [thecsw](https://github.com/thecsw)

## License

This project is licensed under the The GNU General Public License - see the [LICENSE.md](https://github.com/thecsw/rjokes/blob/master/LICENSE) file for details