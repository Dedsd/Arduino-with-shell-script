## Arduino with shell script
#### Executing shell script that automate workspaces with python and arduino when pressed a push button

---

### Components

- Arduino UNO R3(or compatible)
- Push button 2x
- Led rgb 2x
- Resistors 220 ohms 6x
- Resistors 10k 2x
- Jumpers
- Breadboard

---

### Packages

- [os(python)](https://docs.python.org/3/library/os.html)
- [time(python)](https://docs.python.org/3/library/time.html)
- [nanpy(python)](https://github.com/nanpy/nanpy)
- [xdotool(linux)](https://github.com/jordansissel/xdotool)

---

### How it works

#### With the lib nanpy we can connect with arduino serial and execute commands outside arduino ide using python. Recognizing when the button is being pushed or not we trigger the led and run the shell script that opens applications, automates the application windows and creates an organized workspace. The shell script must be with permission for the python script execute. The `co` variable must be changed with the current usb that arduino is connected with.
