#!/bin/env python

import sys

menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = int()
while True:
     try:
          choice = input("Item: ").lower().strip()
          if choice == "":
               break
     except (EOFError, KeyError):
          break
     else:

          try:
               total = total + menu[choice]
          except KeyError:
               continue
          else:

               formatted = format(total, '.2f')
               #rounded = round(total, 2)
               print(f"Total: ",'$',formatted, sep="")


