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
        return "open -a '{}' \"{}\""
    elif os.name=="nt":
        return "start {} \"{}\""

def osOpenDeprecated(): # backwards compatability TODO remove
    if os.name=="posix":
        return "open -a 'Google Chrome' \"{}\""
    elif os.name=="nt":
        return "start chrome \"{}\""

def makeDatetimeObj(hrmin): # makes a datetime obj
    return datetime(datetime.now().year, datetime.now().month, datetime.now().day, hrmin[0],hrmin[1])

def determineBrowser(browser):
    if browser == 1:
        b = ("Google Chrome", "chrome")
    elif browser == 2:
        b = ("Firefox", "firefox")
    elif browser == 3:
        b = ("Safari", "msedge")
    else:
        b = ('none')
    if os.name=="posix":
        return b[0]
    elif os.name=="nt":
        return b[1]
    else:
        return "os"

def createData(): # creates data.json file, requires user input
    print("\nRemember that days alternate between pds 1-5 and 6-10!")
    print("Press command/control+c to exit at any time.")
    sleep(1)

    pdDict={}
    browser=determineBrowser(int(input("\nWhat browser do you use? (1) Google Chrome; (2) Firefox; (3) Microsoft Edge/Safari: ")))
    if browser=="none":
        print("That didn't seem to work. Did you input a number from 1-3?")
        sleep(1)
        createData()
    elif browser=="os":
        print("That didn't seem to work. Are you using an unsupported OS?")
        sleep(2)
        createData()
    pdDict["browser"]=browser    

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
                    try: # backwards compatability for people with old data.json files TODO remove
                        os.system(osOpen().format(pdDict["browser"],link))
                    except:
                        print("Opened using deprecated version. This will continue to work, but consider going through the data creation process again to stay up to date.")
                        os.system(osOpenDeprecated().format(link))

                try: # backwards compatability TODO remove
                    os.system(osOpen().format(pdDict["browser"],pdDict[str(period)]['zoom']))
                except:
                    print("Opened using deprecated version. This will continue to work, but consider going through the data creation process again to stay up to date.")
                    os.system(osOpenDeprecated().format(pdDict[str(period)]['zoom']))

            period+=1
    else:
        print("You did not type 1 or 6.")
        commands(pdDict)


if __name__=="__main__":
    print("Run \"git pull\" every once in a while to stay up to date. (If you didn't download via zip file)")
    sleep(1)
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
