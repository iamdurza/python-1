"""This is a module """

import colors as c
from utils import ask

intro = c.clear + c.magenta + '''
Welcome to the baws quiz quiz.
'''

def q1():
    answer = ask("Who is jackssepticeye?") 
    if answer == "A famous youtuber":
        print("And what a boss he is.")
        return True
    print("That is incorrect.")
    return False

def q2():
    answer = ask("What game dous he play most?")
    if answer.startswith("Happy Wheels"):
        print("But isn't that physically impossible?  Oh well.")
        return True
    print("Nope.")
    return False


def q3():
    answer = ask("What famous youtuber made a shoutout to him")
    if answer.startswith("pewdipie"):
         print(":)")
         return True
    print(":<")
    return False

questions = [q1,q2,q3]








