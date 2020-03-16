import asyncio
from competition import *
from func import *
from classes import *
from helpfile import *
from chall import *
allcommands = ['links','save','alllinks','delete', 'new','archive', 'add', 'solved', 'challs', 'scoreboard', 'links', 'link', 'file', 'remove']
async def command(obj):

    if(obj.hasmessage() == False):
        obj.resp = help()
        return obj
    if((obj.message[0].lower() in ['help', 'hjälp']) or ((obj.message[0].lower() in allcommands) == False)):
        obj.resp = help()
        return obj

    obj = await new(obj)
    obj = await add(obj)
    obj = await solved(obj)
    obj = await remove(obj)
    obj = await archive(obj)
    obj = await erase(obj)
    obj = await links(obj)
    obj = await save(obj)
    obj = await alllinks(obj)

    return obj
