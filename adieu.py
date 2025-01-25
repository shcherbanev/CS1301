#!/bin/env python

import sys
import inflect
p = inflect.engine()

def exit():
    sys.exit()

list = []

while True:
    try:
        name = str(input("Name: "))
        list.append(name)
    except EOFError:
        mylist = p.join(list)
        print("Adieu, adieu, to", mylist)
        exit()
    else:
        pass
