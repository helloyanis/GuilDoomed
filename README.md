# Initial Setup
**Easy setup for Windows**
- Download [easysetup.ps1](https://raw.githubusercontent.com/helloyanis/GuilDoomed/main/easysetup.ps1) (Right-click > Save as)
- Right-click file and click "Run with PowerShell"
The file will install the script, Python, Python modules and guide you through the setup!

**Manual setup**
- Download the [GuilDOOMed.py](https://raw.githubusercontent.com/helloyanis/GuilDoomed/main/GuilDOOMed.py) file (Right-click > Save as)
- Download and install DOOM on your PC
- Download and install [Python](https://www.python.org/downloads/)
- Open cmd and type `pip install guilded pyautogui aiohttp`
- Create a Guilded bot on your server, and copy your bot token
- Edit the Python file (Right click > Open with > Pick a code editor, or notepad if you don't have one), on the first two lines replace `your-bot-token` with the token you copied on the previous step, as well as the channel name of where you want the commands to come in!
- Save the Pyhton file. **You're all set!**


# Start the bot
- Start DOOM, and stream it to your Guilded server (bots can't stream)
- Double click on your `GuilDOOMed.py` file to run it
- It should say `Ready!`, so focus on the game window and wait for commands to come!
**!Be careful! The bot controls your keypresses! Only stay focused on the DOOM window while the bot is running!**
- To stop the bot, close the terminal window

# Troubleshooting
If the window opens then closes, that means an error occured. To see what happened,
- Open IDLE (Search it in Windows search)
- Click File > Open (or press CTRL+O) and open GuilDOOMed.py
- On the new window, click Run > Run module (or press F5) and read the error

`No module named xxx` : Open cmd and type `pip install` and the name of the module that's in the error, for example `pip install guilded`
`builtins.type size changed, may indicate binary incompatibility. Expected 904 from C header, got 888 from PyObject` : Incompatible Python version (Working on a fix)
