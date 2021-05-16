import json
import os

def osOpen():
    if os.name=="posix":
        return "open -a 'Google Chrome' \"{}\""
    elif os.name=="nt":
        return "start chrome \"{}\""

def commands(pdDict):
    day = input("Is today a 1-5 or 6-10 day? Type 1 or 6: ")
    if int(day) in (1,6):
        if int(day)==6:
            period=6
        else:
            period=1

        for _ in range(5):
            check1=pdDict[str(period)]['name']
            if check1 != 'free': # check if free
                # print('checkpoint')
                print("Opening class links for period {}: {}".format(period,pdDict[str(period)]["name"]))
                for link in pdDict[str(period)]["additional"]:
                    os.system(osOpen().format(link))
                os.system(osOpen().format(pdDict[str(period)]['zoom']))

            period+=1
    else:
        print("You did not type 1 or 6.")
        commands(pdDict)

with open("data.json") as json_file:
    data=json.load(json_file)
    commands(data)
