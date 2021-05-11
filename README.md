## Stuy virtual learning scheduler for Windows
---
#### Setting up for dummies
- Create a folder, and navigate to it with a terminal. To get the files locally, run
```
git clone https://github.com/Keychainn/virtuallearningscheduler.git
```
- Refer to Instructions and Info steps 1 and 2 to run the file.
---
#### What is it?
- I always get a a jolting sense of dread when I'm a minute late to class. Maybe I forgot about the time. However, this shall plague Stuy students no more. With this program, your zoom/google meets link will automatically launch, along with any links to attendance questions or student.desmos.com, jupitered.com, etc. Please excuse the uncommented code; I have been making this for 2 hours on on end.
---
#### Requirements:
- Must be running Windows. I have not built in functionality for macOS/linux yet.
- Launches Chrome, so you should have that installed.
---
#### Instructions and Info:
- If using Thonny, go into Tools > open system shell and type `python scheduler.py` to run. Make sure you are in the right directory if there is an error.
- If not using Thonny, and you already have [Python](https://www.python.org/downloads/) installed, simply run `python scheduler.py` or `python3 scheduler.py` in a terminal. I might make an executable later on to save the hassle of downloading python.
- If you are just starting out, you will see some introductory messages. After you press enter, you will be shown input areas for the name of the class, zoom/meets link, and any other additional links you may need that are specific to the class, such as your Google Classroom stream, jupitered attendance questions, etc.
- Once you finish the process, "data.json" will be created in the same directory. If you ever wish to remake your class data, you can either edit directly inside of the JSON file or delete it; upon running scheduler.py again after deleting it, you can go through the data creation process again.
- After you are satisfied with your data file, run the program again. It will open class links 2 minutes before class starts.
- If the program quits immediately, you are likely running it after the last period has started.
---
#### Limitations:
- Most obviously, this is only for Windows. I might make a MacOS version soon.
- This doesn't account for double periods or gym and AB days yet. For doubles, you will have to put both gym and zoom link at the gym time slot, and the zoom link (for science, usually) on its regular slot. If it gets annoying by launching links in the middle of your double, you can do ctrl+C in the terminal to quit the process. The program will continue where it left off whenever you relaunch it. THIS DOES NOT CARRY OVER TO THE NEXT DAY.
- Like I said in caps, this does not carry over to the next day. I think I will implement that in the next version. For now, running at the beginning of the day (or anytime in the middle of the school day) will work.
- Some text says command/control, but this is only for Windows currently, so disregard "command" as it doesn't apply to Windows machines. Foreshadowing? maybe.
- (dev note) I am not sure if sleep is the best way to do the waiting. Perhaps await or something similar may work?
---
#### How to steal my code:
- On line 69, it has `periods=((9,8),(10,13),(11,18),(12,23),(13,28))`. If you want to adapt this code for personal use or for other schedules, add/remove/edit the tuples in `(militaryhour,minute)` format in chronological order.