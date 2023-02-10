token = "your token here"  # Your bot token between the quotes
commands_channel_name = "Commands" # The name of the channel where you want to use the bot (can only be a text channel)


############################################
import time
import pyautogui
import guilded

client = guilded.Client()


@client.event
async def on_ready():
    print('Ready')


@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != commands_channel_name:
        return
    match (message.content.lower()):

        case "help":
            await message.channel.send("Check the project on Github! https://github.com/helloyanis/GuilDoomed")

# Move up

        case "u":
            pyautogui.keyDown('up')
            time.sleep(1)
            pyautogui.keyUp('up')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬆️ for 1s")
            await message.delete()

        case "up":
            pyautogui.keyDown('up')
            time.sleep(1)
            pyautogui.keyUp('up')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬆️ for 1s")
            await message.delete()

        case "lu":
            pyautogui.keyDown('up')
            time.sleep(.3)
            pyautogui.keyUp('up')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬆️ for 0.3s")
            await message.delete()

        case "lup":
            pyautogui.keyDown('up')
            time.sleep(.3)
            pyautogui.keyUp('up')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬆️ for 0.3s")
            await message.delete()

        case "hu":
            pyautogui.keyDown('up')
            time.sleep(3)
            pyautogui.keyUp('up')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬆️ for 3s")
            await message.delete()

        case "hup":
            pyautogui.keyDown('up')
            time.sleep(3)
            pyautogui.keyUp('up')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬆️ for 3s")
            await message.delete()

# Move down

        case "d":
            pyautogui.keyDown('down')
            time.sleep(1)
            pyautogui.keyUp('down')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬇️ for 1s")
            await message.delete()

        case "down":
            pyautogui.keyDown('down')
            time.sleep(1)
            pyautogui.keyUp('down')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬇️ for 1s")
            await message.delete()

        case "ld":
            pyautogui.keyDown('down')
            time.sleep(.3)
            pyautogui.keyUp('down')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬇️ for 0.3s")
            await message.delete()

        case "ldown":
            pyautogui.keyDown('down')
            time.sleep(.3)
            pyautogui.keyUp('down')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬇️ for 0.3s")
            await message.delete()

        case "hd":
            pyautogui.keyDown('down')
            time.sleep(3)
            pyautogui.keyUp('down')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬇️ for 3s")
            await message.delete()

        case "hdown":
            pyautogui.keyDown('down')
            time.sleep(3)
            pyautogui.keyUp('down')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬇️ for 3s")
            await message.delete()

# Move left

        case "l":
            pyautogui.keyDown('left')
            time.sleep(1)
            pyautogui.keyUp('left')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬅️ for 1s")
            await message.delete()

        case "left":
            pyautogui.keyDown('left')
            time.sleep(1)
            pyautogui.keyUp('left')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬅️ for 1s")
            await message.delete()

        case "ll":
            pyautogui.keyDown('left')
            time.sleep(.3)
            pyautogui.keyUp('left')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬅️ for 0.3s")
            await message.delete()

        case "lleft":
            pyautogui.keyDown('left')
            time.sleep(.3)
            pyautogui.keyUp('left')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬅️ for 0.3s")
            await message.delete()

        case "hl":
            pyautogui.keyDown('left')
            time.sleep(3)
            pyautogui.keyUp('left')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬅️ for 3s")
            await message.delete()

        case "hleft":
            pyautogui.keyDown('left')
            time.sleep(3)
            pyautogui.keyUp('left')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ⬅️ for 3s")
            await message.delete()

# Move right

        case "r":
            pyautogui.keyDown('right')
            time.sleep(1)
            pyautogui.keyUp('right')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ➡️ for 1s")
            await message.delete()

        case "right":
            pyautogui.keyDown('right')
            time.sleep(1)
            pyautogui.keyUp('right')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ➡️ for 1s")
            await message.delete()

        case "lr":
            pyautogui.keyDown('right')
            time.sleep(.3)
            pyautogui.keyUp('right')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ➡️ for 0.3s")
            await message.delete()

        case "lright":
            pyautogui.keyDown('right')
            time.sleep(.3)
            pyautogui.keyUp('right')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ➡️ for 0.3s")
            await message.delete()

        case "hr":
            pyautogui.keyDown('right')
            time.sleep(3)
            pyautogui.keyUp('right')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ➡️ for 3s")
            await message.delete()

        case "hright":
            pyautogui.keyDown('right')
            time.sleep(3)
            pyautogui.keyUp('right')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ➡️ for 3s")
            await message.delete()

# Run

        case "run":
            pyautogui.keyDown('shift')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🏃 enabled!")
            await message.delete()

        case "walk":
            pyautogui.keyUp('shift')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🏃 disabled!")
            await message.delete()

# Shoot

        case "autoshoot":
            pyautogui.keyDown('ctrl')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 enabled!")
            await message.delete()

        case "shoot":
            pyautogui.keyDown('ctrl')
            time.sleep(.3)
            pyautogui.keyUp('ctrl')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 for 0.3s")
            await message.delete()

        case "stopshoot":
            pyautogui.keyUp('ctrl')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 disabled!")
            await message.delete()

# Weapon

        case "1":
            pyautogui.keyDown('1')
            time.sleep(.3)
            pyautogui.keyUp('1')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ✊ Fist")
            await message.delete()

        case "2":
            pyautogui.keyDown('2')
            time.sleep(.3)
            pyautogui.keyUp('2')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 Pistol")
            await message.delete()

        case "3":
            pyautogui.keyDown('3')
            time.sleep(.3)
            pyautogui.keyUp('3')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 Shotgun")
            await message.delete()

        case "4":
            pyautogui.keyDown('4')
            time.sleep(.3)
            pyautogui.keyUp('4')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 Chaingun")
            await message.delete()

        case "5":
            pyautogui.keyDown('5')
            time.sleep(.3)
            pyautogui.keyUp('5')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 Rocket Launcher")
            await message.delete()

        case "6":
            pyautogui.keyDown('6')
            time.sleep(.3)
            pyautogui.keyUp('6')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 Plasma Rifle")
            await message.delete()

        case "7":
            pyautogui.keyDown('7')
            time.sleep(.3)
            pyautogui.keyUp('7')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 🔫 BFG")
            await message.delete()

# Menu

        case "menu":
            pyautogui.keyDown('escape')
            time.sleep(.3)
            pyautogui.keyUp('escape')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 📜 Menu")
            await message.delete()

        case "esc":
            pyautogui.keyDown('escape')
            time.sleep(.3)
            pyautogui.keyUp('escape')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n 📜 Menu")
            await message.delete()

        case "enter":
            pyautogui.keyDown('enter')
            time.sleep(.3)
            pyautogui.keyUp('enter')
            await message.channel.send("🕹️ Input done by "+message.author.name+"!\n ✅ Enter")
            await message.delete()

client.run(token)
