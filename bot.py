#Import all libraries
import discord
import random

#Create MyClient class
class MyClient(discord.Client):

    #Read contents of File and fill it into a list (type int)
    def readinfile(self, name):
        f = open(name)
        l2 = f.readlines()
        l = []
        for i in l2:
            l.append(int(i))
        f.close()
        return l

    # Read contents of File and fill it into a list (type str)
    def readstrfile(self, name):
        f = open(name)
        l2 = f.readlines()
        l = []
        for i in l2:
            l.append(i)
        f.close()
        return l

    #If bot ready... change status and log to Console
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(activity=discord.Game('Enes ist ein Inter'), status=discord.Status.invisible)

    #On Message recieved
    async def on_message(self, message):
        #Print Content of new Message and Author
        print('Message from {0.author}: {0.content}'.format(message))

        #Read the IDs as strings of all Users able to control the Bot into a List
        l = self.readinfile("mods")



        #If User is in the "Mods" File
        if message.author.id in l:

            #Check if the Message starts with an excalmation mark
            if message.content.startswith("!"):

                #The message without the exclamation mark
                message_without = message.content[1:]

                #If the Message was help print the help message
                if message_without.lower().startswith("help"):
                    await message.channel.send("Befehle: \n '!add victim VICTIMID' - adds a new victim \n '!add user USERID'- adds a new user, able to control the bot"
                                               " \n '!add enesfact YOURENESFACT' - to add your fact about Enes")

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

                #Check if user wants to add a new Fact about Enes
                if message_without.lower().startswith("add enesfact"):

                    #Message without command
                    wm = message_without[len("add enesfact")+ 1:]

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
                    print("Quote: '{}' to added to facts!".format(wm))
                    f.close()

                    #Feedback
                    await message.channel.send("Fact: '{}' added!".format(wm))
                    print("Fact: '{}' added!".format(wm))



            #If message is not a command and contains Enes
            elif "enes" in message.content.lower():
                #Read all facts out of File
                fl = self.readstrfile("facts")

                #Send back a random fact
                await message.channel.send(random.choice(fl))





    #When any Member updates the profile
    async def on_member_update(self, before, after):

        #Read List of victims
        l = self.readinfile("victims")


        i = self.get_all_members()
        for enes in i:
        #For every Member
            if enes.id in l:
                #If Member is in List
                print("Changing Name!")
                e = enes
                #Change Nickname
                await e.edit(nick='SchnuggiBuggi')

#Open File and read token out of it
f = open("TOKEN")
token = f.readline()
f.close()

#Start Client with Token
client = MyClient()
client.run(token)