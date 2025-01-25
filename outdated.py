#!/bin/env python

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    user_input = str(input("Date: ").strip())

    alpha = bool
    digit = bool

# DETERMINE WHAT HAS BEEN ENTERED

    for i in user_input:
        if i.isalpha():
            #print("Entered words")
            alpha = True
            break
        elif i.isdigit():
            #print("Entered digit")
            digit = True
            break
        else:
            print("Input unknown")

# MAIN APPLICATION BODY

    if alpha == True:
        try:
            month, day, year = user_input.split(" ")
        except ValueError:
            continue
        else:
            try:
                day = int(day)
            except ValueError:
                day = day.strip(",")
                day = int(day)
                year = int(year)
                if month in month_list and day <= 31 and year < 9999:
                    day = f'{day:02}'
                    month_index = month_list.index(month)+1
                    month_index_modified = f'{month_index:02}'
                    print(year, month_index_modified, day, sep="-")
                    break
                else:
                    continue

    elif digit == True:
        try:
            month, day, year = user_input.split("/")
        except ValueError:
            continue
        else:
            month = int(month)
            day = int(day)
            year= int(year)
            if day <= 31 and month <= 12:
                day = f'{day:02}'
                month = f'{month:02}'
                print(year,month,day, sep="-")
            #print("Looks like you've entered digits")
                break
            else:
                continue
    else:
        print("Looks like you've entered something else")

