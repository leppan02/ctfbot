import asyncio

from classes import *
from helpfile import *
from ctffile import *
allcommands = ['new','archive', 'add', 'solved', 'challs', 'scoreboard', 'links', 'link', 'file', 'remove']
async def test(obj):
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
    print(obj.resp)
    return obj
