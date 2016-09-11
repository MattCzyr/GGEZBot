import praw
import traceback
import random
from collections import deque
from praw.helpers import comment_stream

USERNAME = "gg_ez_bot"
PASSWORD = "***" # No password for you :(
USERAGENT = "GG EZ v1.0.0 (by /u/ChaosTheDude)"

FOOTER = "\n\n---\n^I ^am ^a ^bot ^made ^by ^/u/ChaosTheDude. ^Beep ^boop. ^| ^[GitHub](https://github.com/ChaosTheDude/GG-EZ-Bot)"

r = praw.Reddit(USERAGENT)
r.login(USERNAME, PASSWORD)

cache = deque(maxlen=200)

responses = ['Well played. I salute you all.',
             'For glory and honor! Huzzah comrades!',
             'I\'m wrestling with some insecurity issues in my life but thank you all for playing with me.',
             'It\'s past my bedtime. Please don\'t tell my mommy.',
             'Gee whiz! That was fun. Good playing!',
             'I feel very, very small... please hold me...',
             'Ah shucks... you guys are the best!',
             'Good game! Best of luck to you all!',
             'I\'m trying to be a nicer person. It\'s hard, but I am trying, guys.',
             'Mommy says people my age shouldn\'t suck their thumbs.',
             'Well played. I salute you all.',
             'C\'mon, Mom! One more game before you tuck me in. Oops mistell.',
             'Great game, everyone!',
             'It was an honor to play with you all. Thank you.']


def process_comment(c):
    text = c.body.lower()
    if "gg ez" in text:
        print(comment.body)
        response = random.choice(responses)
        print("\n" + response + "\n---\n")
        c.reply(response + FOOTER)


running = True
while running:
    for comment in comment_stream(r, 'overwatch'):
        if comment.id in cache:
            break

        cache.append(comment.id)
        replied = False

        try:
            process_comment(comment)
        except KeyboardInterrupt:
            running = False
        except:
            traceback.print_exc()