"""This my awesome utility kitchen sink. Don't judge me."""

import colors as c 



def ask(question,color=c.red):
    print(color + question + c.reset)
    answer = input("> " + c.base3).lower().strip()
    print(c.reset)
    return answer



if __name__ == '__main__':
    print(c.clear)
    name = ask("what is your name?")
    color = ask("What is your favorite color?",c.random_color())








