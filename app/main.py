import features
import discord
import sys


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        await features.MessageHandling(message)
        return

    async def on_message_edit(self, before, message):
        await features.MessageHandling(message)
        return


if __name__ == "__main__":
    client = Client()
    try:
        TOKEN = sys.argv[1]
    except:
        raise Exception("TOKEN missing")
    client.run(TOKEN)
