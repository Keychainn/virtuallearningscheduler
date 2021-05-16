from time import sleep
import json
import os
from datetime import datetime

#helper functions:
def checkIfElementsIn(userTuple,userInput): # check if any elements in given tuple are in a list
    conditional=False
    for x in userTuple:
        if x == userInput.lower(): # account for random capitalization
            conditional=True
    return conditional

def osOpen(): # different strings depending on OS
    if os.name=="posix":
        return "open -a 'Google Chrome' \"{}\""
    elif os.name=="nt":
        return "start chrome \"{}\""

def makeDatetimeObj(hrmin): # makes a datetime obj
    return datetime(datetime.now().year, datetime.now().month, datetime.now().day, hrmin[0],hrmin[1])



def createData(): # creates data.json file, requires user input
    print("\nRemember that days alternate between pds 1-5 and 6-10!")
    print("Press command/control+c to exit at any time.")
    sleep(1)

    pdDict={}

    for classNum in range(10): # 10 periods
        subDict={} # inside for loop to flush temporary dict when frees are in the middle of day
        print("\nWhat class do you have for period {}? Type \"N/A\" or \"free\" if you have a free or lunch during this period. Do not repeat subject names.".format(classNum+1))
        selectedClass = input("> ")
        

        freePeriod = checkIfElementsIn(("free","na","n/a"),selectedClass)

        if not freePeriod:
            invalid=True
            while invalid: # standard "repeat until proper input"
                print("    Paste zoom/google meets link. If your class doesn't have a recurring link, paste your Google Classroom stream:")
                zoom = input("    > ")
                if "https" in zoom and ("zoom" in zoom or "meet" in zoom or "classroom" in zoom):
                    invalid=False
                else:
                    print("That doesn't seem to work. Please try again with the full zoom/meets link.")
                    sleep(1)
        
            moreLinks=True
            extra=[] # init extra links list
            while moreLinks: # standard "repeat until proper input"
                print("    Paste any links you regularly visit i.e. attendance questions. Leave blank (and press enter) if none:")
                extraLink = input("    > ")

                if extraLink.replace(" ",""):
                    extra.append(extraLink)
                else:
                    moreLinks=False
                    
            subDict.update({"name":selectedClass,"zoom":zoom,"additional":extra})

        else:
            subDict.update({"name":"free"})
        # subDict.update({"free":freePeriod})
        pdDict[classNum+1] = subDict # int?
    
    with open("./data.json","w+") as writefile:
        json.dump(pdDict,writefile)

def commands(pdDict):
    periods=((9,8),(10,13),(11,18),(12,23),(13,28)) # in military time
    day = input("Is today a 1-5 or 6-10 day? Type 1 or 6: ")
    if int(day) in (1,6):
        if int(day)==6:
            period=6
        else:
            period=1

        for time in periods:
            time_delta=(makeDatetimeObj(time)-datetime.now()).total_seconds()
            if time_delta < 0:
                print("Period {} has already passed.".format(period))
                period+=1
                continue
            print("Waiting until the start of period {}...".format(period))
            sleep(time_delta)

            if pdDict[str(period)]['name'] != 'free': # check if free
                print("Opening class links for period {}: {}".format(period,pdDict[str(period)]["name"]))
                for link in pdDict[str(period)]["additional"]:
                    os.system(osOpen().format(link))
                os.system(osOpen().format(pdDict[str(period)]['zoom']))

            period+=1
    else:
        print("You did not type 1 or 6.")
        commands(pdDict)


if __name__=="__main__":
    print("Run \"git pull\" every once in a while to stay up to date.")
    sleep(1.5)
    try:
        with open("data.json") as json_file:
            exist=True
    except:
        exist=False
        print("\nIt looks like a data file doesn't exist (yet). Please contact qsun30@stuy.edu if this problem persists. If this is your first time using this program, this is expected!")
        # input("Press ENTER to start inputting classes, or command/control+C to exit.")
        createData()
    if exist:
        with open("data.json") as json_file: # moved out of try block so errors point to their problem instead of except block
            data=json.load(json_file)
            commands(data)
