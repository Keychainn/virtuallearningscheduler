## Stuy virtual learning scheduler for Chrome
---
#### Setting up for dummies
1. If you don't have git, you can download the scheduler.zip file, and [unzip](https://www.sweetwater.com/sweetcare/articles/how-to-zip-and-unzip-files/) it to a location of your choosing.
2. Create a folder and navigate to it with a terminal. To get the files locally, run
```
git clone https://github.com/Keychainn/virtuallearningscheduler.git
```
Refer to Instructions and Info steps 1 and 2 to run the file.
---
#### What is it?
- Never be late again!
- I always get a a jolting sense of dread when I'm a minute late to class. Maybe I forgot about the time. However, this shall plague Stuy students no more. With this program, your zoom/google meets link will automatically launch, along with any links to attendance questions or student.desmos.com, jupitered.com, etc.
---
#### Requirements:
- Must be running Windows or Mac. Linux is untested.
- Must have either Google Chrome, Firefox, Safari, or Microsoft Edge.
- Must have [Python 3](https://www.python.org/downloads/) installed (this includes a Thonny installation).
---
#### Instructions and Info:
- If you are just starting out, you will see some introductory messages. After you press enter, you will be shown input areas for the name of the class, zoom/meets link, and any other additional links you may need that are specific to the class, such as your Google Classroom stream, jupitered attendance questions, reference table, etc. If you are having trouble pasting a link in, try right clicking on the terminal.
- **Thonny only:** if you wish to run this program while being able to use Thonny normally, go into Tools > open system shell and type `python scheduler.py` to run. Make sure you are in the right directory if there is an error.
- Once you finish the process, "data.json" will be created in the same directory. If you ever wish to remake your class data, you can either edit directly inside of the JSON file or delete/rename/move it; upon running scheduler.py again after deleting/renaming/moving it, you can go through the data creation process again.
- After you are satisfied with your data file, run the program again. It will open class links 2 minutes before class starts.
- If the program quits immediately, you are likely running it after the last period has started.
- If you want to test if the program will work without waiting for the start of every period, you can do so by running `python tester.py`.
- **Old versions:** If you are using an old version of data.json, you will see a message saying something about a deprecated version. If you are averse to completely remaking your data.json file, you can add `"browser": "chrome",` (or `"browser": "Google Chrome",` for MacOS) after the first `{` in your data.json file.
---
#### Limitations:
- This doesn't account for double periods or gym and AB days yet. For doubles, you will have to put both gym and zoom link at the gym time slot, and the zoom link (for science, usually) on its regular slot. If it gets annoying by launching links in the middle of your double, you can do ctrl/command+C in the terminal to quit the process (or stop button in Thonny/IDE). The program will continue whenever you relaunch it.
- You should run this program every morning, as this does not carry over to the next day. This is because this program will effectively freeze if you put your computer to sleep, which is something that many computers do overnight.
- I haven't figured out a GUI (not to be confused with a [DUI :D](https://en.wikipedia.org/wiki/Driving_under_the_influence))  yet, so everything is done in the command line for now.
---
#### How to steal my code:
- On line 103, it has `periods=((9,8),(10,13),(11,18),(12,23),(13,28))`. If you want to adapt this code for personal use or for other schedules, add/remove/edit the tuples in `(militaryhour,minute)` format in chronological order.