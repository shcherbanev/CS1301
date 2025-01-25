import sys
def main():
    entered_message = str(input("Enter your message: ")).strip()
    print(shorten(entered_message))

def shorten(user_message):
    mess = str(user_message)
    for i in mess:
        if i.isdigit():
            continue

    for i in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        mess = mess.replace(i, "")
    return mess


if __name__ == "__main__":
    main()