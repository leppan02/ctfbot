import discord
import sys
import asyncio
from command import *
from classes import *
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        await messagehandling(message)
        return

    async def on_message_edit(self,before, message):
        await messagehandling(message)
        return

async def messagehandling(message):
    if(message.content.split(' ')[0].lower() != 'ctf'):
        return
    current = MessageClass(message = message.content.split(' ')[1:], channel = message.channel,guild = message.guild, resp = [], resplinks = [], files = [])
    if(len(message.attachments)):
        current.files.append(message.attachments[0].url)
    current = await test(current)
    if(await current.hasresp()):
        await message.channel.send('\n'.join(await current.output()))
        current.resp = []
        return


if(len(sys.argv)==1):
    print('Specify: debug or deploy')
elif(sys.argv[1]=='deploy'):
    client = MyClient()
    client.run('Njg4NzY4NjA5NDE3NTYwMTg0.Xm5Inw.8OKgj8BIfTBdZ4g2KIN5BAteOAY')
elif(sys.argv[1]=='debug'):
    Input = input()
    while(Input!='done'):
        Input = input()
