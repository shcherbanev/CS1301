import random


def main():
    level = get_level()
    i = 0
    counter = 0
    score = 0
    while i != 10:
        try:
            if counter == 0:
                x = generate_integer(level)
                y = generate_integer(level)
            ans = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            counter += 1
        else:
            if ans == x + y:
                score += 1
                counter = 0
                i += 1
            else:
                print("EEE")
                counter += 1
        if counter == 3:
            i += 1
            print(f"{x} + {y} = {x+y}")
            counter = 0

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                continue


def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
    elif level == 3:
        a = random.randint(100, 999)
    else:
        pass

    return a


if __name__ == "__main__":
    main()