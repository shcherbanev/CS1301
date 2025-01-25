#!/bin/env python

from fractions import Fraction

while True:

    try:
        num = Fraction(input("Fraction?: "))
        result = round(num, 2) * 100
        #print(result)
    except (ZeroDivisionError, ValueError):
        pass
    else:
        if result >= 0 and result <= 1:
            #print(result)
            print("E")
            break
        elif result >= 99 and result <= 100:
            #print(result)
            print("F")
            break
        elif result > 100:
            #print(result)
            continue
        else:
            print(result, '%', sep="")
            break


