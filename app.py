import random

execuse = ("You wouldnt believe this but,", "OMG,", "Sweet baby jesus,")
who = ("The dog", "The nanny", "My Grandma")
action = ("ate", "ran over", "punched")
what = ("the homework", "the laptop", "the gardner")
when = ("yesterday", "today", "on friday")


def getrandomnumber():
    return random.randint(0,2)

temporary = getrandomnumber()

print(execuse[getrandomnumber()]+" "+who[temporary]+" "+action[temporary] +
      " "+what[temporary]+" "+when[temporary])
