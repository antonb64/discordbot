import discord
import random
from discord.ext.commands import MemberConverter

class MyClient(discord.Client):

    def readinfile(self, name):
        f = open(name)
        l2 = f.readlines()
        l = []
        for i in l2:
            l.append(int(i))
        f.close()
        return l

    def readstrfile(self, name):
        f = open(name)
        l2 = f.readlines()
        l = []
        for i in l2:
            l.append(i)
        f.close()
        return l


    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(activity=discord.Game('Enes ist ein Inter'), status=discord.Status.invisible)


    async def on_message(self, message):
        valid_users = [253983342402338816, 249615488991232000, 206000522841292800]
        print('Message from {0.author}: {0.content}'.format(message))

        l = self.readinfile("mods")



        if message.author.id in l:
            if message.content.startswith("!"):

                message_without = message.content[1:].lower()
                if message_without.startswith("help"):
                    await message.channel.send("Befehle: \n '!add victim VICTIMID' - adds a new victim \n '!add user USERID'- adds a new user, able to control the bot"
                                               " \n '!add enesfact YOURENESFACT' - to add your fact about Enes")

                if message_without.startswith("add victim"):

                    wm = message_without[len("add victim") +1 :]
                    if wm.isnumeric():
                        f = open("users", "a")
                        f.write(wm)
                        f.write("\n")
                        print("User: {} added!".format(wm))
                        f.close()
                        await message.channel.send("User: {} added to victims!".format(wm))
                    else:
                        await message.channel.send("Sorry, gibt bitte eine Zahl ein!")


                if message_without.startswith("add user"):
                    f = open("mods", "a")
                    wm = message_without[len("add user") +1 :]

                    if wm.isnumeric():
                        f.write(wm)
                        f.write("\n")
                        print("User: {} added!".format(wm))
                        f.close()
                        await message.channel.send("User: {} added!".format(wm))
                    else:
                        await message.channel.send("Sorry, gibt bitte eine Zahl ein!")

                if message_without.startswith("add enesfact"):
                    f = open("facts", "a")
                    wm = message_without[len("add enesfact")+ 1:]
                    try:
                        wm = wm.capitalize()
                    except:
                        pass
                    f.write(wm)
                    f.write("\n")
                    print("Quote: '{}' to added to facts!".format(wm))
                    f.close()
                    await message.channel.send("Fact: '{}' added!".format(wm))




            elif "enes" in message.content.lower():
                fl = self.readstrfile("facts")
                await message.channel.send(random.choice(fl))






    async def on_member_update(self, before, after):

        l = self.readinfile("users")
        i = self.get_all_members()
        for enes in i:
            if enes.id in l:
                print("Restricted username change detected!")
                e = enes
                await e.edit(nick='SchnuggiBuggi')


f = open("TOKEN")
token = f.readline()
f.close()

client = MyClient()
client.run(token)