from time import sleep
import json
from os import system
from datetime import datetime

def checkIfElementsIn(userTuple,userInput): # helper fx to check if any elements in given tuple are in a list
    conditional=False
    for x in userTuple:
        if x == userInput.lower():
            conditional=True
    return conditional

def createData(): # creates data.json file, requires user input
    print("\nRemember that days alternate between pds 1-5 and 6-10!")
    print("Press command/control+c to exit at any time. does not work on thonny or other Python IDE; use the stop button instead.")
    sleep(1)

    pdDict={}

    for classNum in range(10): # 10 periods
        subDict={} # inside to flush when frees are in middle of day
        print("\nWhat class do you have for period {}? Type \"N/A\" or \"free\" if you have a free or lunch during this period. Do not repeat subject names.".format(classNum+1))
        selectedClass = input("> ")
        

        freePeriod = checkIfElementsIn(("free","na","n/a"),selectedClass)

        if not freePeriod:
            invalid=True
            while invalid:
                print("    Paste zoom/google meets link: (try: right clicking, command+shift+v, control+shift+v, control/command+v)")
                zoom = input("    > ")
                if "https" in zoom and ("zoom" in zoom or "meet" in zoom):
                    invalid=False
                else:
                    print("That doesn't seem to work. Please try again with the full zoom link.")
                    sleep(1)
        
            moreLinks=True
            extra=[]
            linkNum=1
            while moreLinks:
                print("    Any other links you regularly visit? (i.e. attendance questions) CHOOSE y/n :")
                
                yn = input("    > ")
                if checkIfElementsIn(("n","no"),yn):
                    moreLinks=False
                elif checkIfElementsIn(("y","yes"),yn):
                    print("        Paste link #{} here: (Be sure to paste links that are regularly accessible! i.e. rocket chat stream, Google Classroom stream)".format(linkNum))
                    extra.append(input("        > "))
                else:
                    print("        \nGive a yes or no answer\n")
                    linkNum-=1
                linkNum+=1
            subDict.update({"name":selectedClass,"zoom":zoom,"additional":extra})
        else:
            subDict.update({"name":"free"})
        subDict.update({"free":freePeriod})

        pdDict[classNum+1] = subDict # see if i can write as int
    
    with open("./data.json","w+") as writefile:
        json.dump(pdDict,writefile)

def makeDatetimeObj(hrmin):
    return datetime(datetime.now().year,datetime.now().month,datetime.now().day,hrmin[0],hrmin[1])

def commands(pdDict):
    periods=((9,8),(10,13),(11,18),(12,23),(13,28)) # in military time
    periods=((20,59),(21,0),(21,1),(21,2),(21,3))
    day = input("Is today a 1-5 or 6-10 day? Type 1 or 6: ")
    if int(day) in (1,6):
        if int(day)==6:
            addon=5
        else:
            addon=0

        period=1
        for time in periods:
            time_delta=(makeDatetimeObj(time)-datetime.now()).total_seconds()
            if time_delta < 0:
                period+=1
                continue
            print("Waiting until the start of the next period...")
            sleep(time_delta)

            if not pdDict[str(period+addon)]['free']: # check if free
                print("Opening class links for period {}: {}".format(period+addon,pdDict[str(period+addon)]["name"]))
                for link in pdDict[str(period+addon)]["additional"]:
                    if link:
                        system(f"start chrome {link}")
                system("start chrome {}".format(pdDict[str(period+addon)]['zoom']))

            period+=1
    else:
        print("You did not type 1 or 6.")
        commands(pdDict)


if __name__=="__main__":
    try:
        with open("data.json") as json_file:
            pass
    except:
        print("It looks like a data file doesn't exist (yet). Please contact qsun30@stuy.edu if this problem persists. If this is your first time using this program, this is expected!")
        input("Press enter to start inputting classes, or command/control+C to exit. This program works best if run in Windows Powershell or Windows Command Prompt.")
        createData()
    with open("data.json") as json_file:
        data=json.load(json_file)
        commands(data)
