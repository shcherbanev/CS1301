def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars = str(dollars).strip().replace('$','')
    dollars = float(dollars)
    return dollars



def percent_to_float(percent):
    percent = str(percent).strip().replace('%','')
    percent = float(percent)/100
    return percent


main()
