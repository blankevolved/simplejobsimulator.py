import json
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
        def jobmenu():
            print("hello")
            input()
        print(
"""Simple Job Simulator""",
"""

Coins:""", coins,
"""

1. Jobs
line 3"""
            )
        mainInput = input()
        if mainInput == "1":
            jobmenu()
while True:
    main()
    ## loop