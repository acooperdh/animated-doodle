import discord
import discord.ext.commands as commands

class myClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.content.startswith('!hello'):
            await self.send_message(message.channel, 'Hello!')
client = myClient()
client.run() #token goes here   