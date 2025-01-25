#!/bin/env python

import sys
import requests



def main():

    def user_bitcoins():
            try:
                num_bitcoins = float(sys.argv[1])
            except IndexError:
                    sys.exit("Missing command-line argument")
            except ValueError:
                    sys.exit("Command-line argument is not a number")
            else:
                amount = bitcoin_rate(num_bitcoins)
                print(f"${amount:,.4f}")
                sys.exit()

    print("User entered: ", + user_bitcoins())

def bitcoin_rate(num_bitcoins):
    try:
        responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
         sys.exit()
    else:
        o = responce.json()
        rate = o["bpi"]
        usd = rate["USD"]
        usd_rate = usd["rate_float"]
        return usd_rate * num_bitcoins




if __name__ == "__main__":
    main()
