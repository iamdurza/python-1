"""This is a module """

import colors as c
from utils import ask

intro = c.clear + c.magenta + '''
Welcome to the pink fluffy unicors quiz.
'''

def q1():
    answer = ask("What color are the unicors?") 
    if answer == "pink":
        print("And what a lovely color it is.")
        return True
    print("That is incorrect.")
    return False

def q2():
    answer = ask("What are the unicors dancing on?")
    if answer.startswith("rainbow"):
        print("But isn't that physically impossible?  Oh well.")
        return True
    print("Nope.")
    return False


def q3():
    answer = ask("Use one word to describe the texture  of the unicors magic fur?")
    if answer.startswith("smile"):
         print(":)")
         return True
    print(":<")
    return False

questions = [q1,q2,q3]








