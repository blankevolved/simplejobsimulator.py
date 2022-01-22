import json
import time
print("LOADING.....")
time.sleep(10)
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
        version = "simplejobsimulator.py v0.0.1"
        def jobmenu():
            print()
            print(version)
            print()
            print("Coins: " + str(coins))
            print()
            print("hello")
            Input = input()
        def upgrademenu():
            print()
            print(version)
            print()
            print("Coins: " + str(coins))
            print()
            print("Upgrades:")
            print()
            print("1. Upgrade 1")
            print( "[Test Upgrade]")
            Input = input()
        print()
        print(version)
        print()
        print()
        print("Coins: " + str(coins))
        print()
        print("1. Job Menu")
        print("2. Upgrade Menu")
        Input = input()
        if Input == "1":
            jobmenu()
        if Input == "2":
            upgrademenu()
        else:
            main()
while True:
    main()