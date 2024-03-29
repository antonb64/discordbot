#Import all libraries
import discord
import random

#Open File and read token out of it
f = open("TOKEN")
token = f.readline()
f.close()



#Start Client with Token
client = discord.Client(intents=discord.Intents.all())


def readinfile(name):
    f = open(name)
    l2 = f.readlines()
    l = []
    for i in l2:
        l.append(int(i))
    f.close()
    return l

# Read contents of File and fill it into a list (type str)
def readstrfile(name):
    f = open(name)
    l2 = f.readlines()
    l = []
    for i in l2:
        l.append(i)
    f.close()
    return l

#If bot ready... change status and log to Console
@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    await client.change_presence(activity=discord.Game('targetS ist ein Inter'))#, status=discord.Status.invisible)

#On Message recieved
@client.event
async def on_message(message):
    #Print Content of new Message and Author
    print(f'Message from {message.author}: {message.content}')

    #Read the IDs as strings of all Users able to control the Bot into a List
    l = readinfile("mods")



    #If User is in the "Mods" File
    if message.author.id in l:
        #Check if the Message starts with an excalmation mark
        if message.content.startswith("!"):

            #The message without the exclamation mark
            message_without = message.content[1:]

            #If the Message was help print the help message
            if message_without.lower().startswith("help"):
                await message.reply("Befehle: \n '!add victim VICTIMID' - adds a new victim \n '!add user USERID'- adds a new user, able to control the bot"
                                            " \n '!add targetSfact YOURtargetSFACT' - to add your fact about targetS \n '!add nickname NICKNAME'")

            #If the message was to add a new victim to the list
            if message_without.lower().startswith("add victim"):

                #Variable with Message without
                wm = message_without[len("add victim") +1 :]

                #Check if the number is valid
                if wm.isnumeric():
                    #If true - write ID in 'victims' file and log to console and channel
                    f = open("victims", "a")
                    f.write(wm)
                    f.write("\n")
                    print("User: {} added!".format(wm))
                    f.close()
                    await message.channel.send("User: {} added to victims!".format(wm))
                else:
                    #Else print Error in channel and console
                    print("Fehlgeschlagen - ID muss eine Zahl sein.")
                    await message.channel.send("Sorry, gibt bitte eine Zahl ein!")

            #Check if user wants to add a new person, able to use the Bot
            if message_without.lower().startswith("add user"):
                #Message without command prefix
                wm = message_without[len("add user") +1 :]

                #Check if the ID is a Number
                if wm.isnumeric():
                    #If successful add to 'mods' File
                    f = open("mods", "a")
                    f.write(wm)
                    f.write("\n")
                    print("User: {} added!".format(wm))
                    f.close()
                    await message.channel.send("User: {} added!".format(wm))
                else:
                    # Else print Error in channel and console
                    await message.channel.send("Sorry, gibt bitte eine Zahl ein!")
                    print("Fehlgeschlagen - ID muss eine Zahl sein.")

            #Check if user wants to add a new Fact about targetS
            if message_without.lower().startswith("add targetSfact"):

                #Message without command
                wm = message_without[len("add targetSfact")+ 1:]

                #Replace all 'Umlaute'
                wm = wm.replace("ä", "ae")
                wm = wm.replace("ö", "oe")
                wm = wm.replace("ü", "ue")
                wm = wm.replace("Ä", "Ae")
                wm = wm.replace("Ö", "Oe")
                wm = wm.replace("Ü", "Ue")


                #Add to file
                f = open("facts", "a")
                f.write(wm)
                f.write("\n")
                f.close()

                #Feedback
                await message.channel.send("Fact: '{}' added!".format(wm))
                print("Fact: '{}' added!".format(wm))

            #Check if user wants to add a new nickname for targetS
            if message_without.lower().startswith("add nickname"):

                wm = message_without[len("add nickname")+1:]


                wm = wm.replace("ä", "ae")
                wm = wm.replace("ö", "oe")
                wm = wm.replace("ü", "ue")
                wm = wm.replace("Ä", "Ae")
                wm = wm.replace("Ö", "Oe")
                wm = wm.replace("Ü", "Ue")

                #Add to file
                f = open("nicknames", "a")
                f.write(wm)
                f.write("\n")
                f.close()


                #Feedback
                print("Nickname: '{}' added to nicknames.".format(wm))
                await message.channel.send("Nickname: '{}' added to nicknames.".format(wm))



        #If message is not a command and contains targetS
        elif "targetS" in message.content.lower():
            #Read all facts out of File
            fl = readstrfile("facts")
            print(random.choice(fl))
            """
            #Send back a random fact
            await message.channel.send(random.choice(fl))
            """




#When any Member updates the profile
@client.event
async def on_member_update(before, after):

    print("{} tried to change the Name!".format(before.nick))
    #Read List of victims
    l = readinfile("victims")

    #Import all cringe Names
    names = readstrfile("nicknames")

    #If the user is in the victims list and the name is restricted
    if (not (after.nick + "\n" )in names) and after.id in l:
        nickname = random.choice(names)
        await after.edit(nick=nickname)
        await client.change_presence(activity=discord.Game('{} ist ein Inter'.format(nickname)))


#Run The client
client.run(token)
