#!/bin/env python

import sys
import random
from pyfiglet import Figlet

def invalid_usage():
    sys.exit("Invalid usage")

def exit():
    sys.exit()



if len(sys.argv) == 1:
    figlet = Figlet()
    fonts = figlet.getFonts()
    random.shuffle(fonts)
    font = fonts[5]
    figlet.setFont(font=font)
    input = input("Input: ").strip().lower()
    print("Output:")
    print(figlet.renderText(input))
    exit()
elif len(sys.argv) == 3:
    figlet = Figlet()
    fonts = figlet.getFonts()
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
        font = sys.argv[2]
        input = input("Input: ").strip()
        figlet.setFont(font=font)
        print("Output:")
        print(figlet.renderText(input))
    else:
        invalid_usage()
elif len(sys.argv) == 2:
    invalid_usage()

    exit()
else:
    exit()
