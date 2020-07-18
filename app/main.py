import features
import printformat as pf
import discord
TOKEN = 'Njg4NzY4NjA5NDE3NTYwMTg0.Xm5Inw.8OKgj8BIfTBdZ4g2KIN5BAteOAY'
class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        await features.MessageHandling(message)
        return

    async def on_message_edit(self,before, message):
        await features.MessageHandling(message)
        return

if __name__ == "__main__":    
    client = Client()
    client.run(TOKEN)
