import json
from multiprocessing.connection import wait
import time
def main():
    opendata = open('data/savegame.json')
    read = json.load(opendata)
    def save():
        data ={
        'coins': coins
        }
        with open('data/savegame.json', "w") as outfile:
            json.dump(data, outfile)
    if read == {}:
        null = {
            'coins': 0
        }
        with open('data/savegame.json', "w") as outfile:
            json.dump(null, outfile)
    else:
        coins = read["coins"]
        version = "0.0.1"
        def jobmenu():
            print("hello")
            input()
        print("LOADING.....")
        time.sleep(10)
        print()
        print("simplejobsimulator v" + version)
        print()
        print()
        print("Coins: " + str(coins))
        print()
        print("1. Job Menu")
        mainInput = input()
        if mainInput == "1":
            jobmenu()
while True:
    main()