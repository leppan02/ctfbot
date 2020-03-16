from classes import *
from func import *
import os.path
from os import path
import validators
import discord
from time import sleep
import pickle

async def add(obj):

    if(obj.message[0].lower() != 'add'):
        return obj
    if(len(obj.message) != 2):
        obj.resp.append('Incorrect input')
        obj.resp.append('1 arguments after add')
        obj.resp.append('[chall name]')
        return obj
    tmpchall = chall(name = str(obj.message[1]), category = str(obj.channel.category))
    if(tmpchall.category == None):
        obj.resp.append('this chat does not belong to a competition')
        return obj
    if(await check(obj)):
        obj.resp.append('master chat missing')
        return obj
    for i in obj.guild.channels:
        if(str(i.category) == str(tmpchall.category) and str(i.name) == str(tmpchall.name)):
            obj.resp.append('already-exists')
    if(len(await obj.output())!=0):
        return obj

    # 
    # input is correct 
    # 

    pickleempty(tmpchall.category,tmpchall.name)
    addedtextchat = await obj.channel.clone(name=tmpchall.name)
    addedvoicechat = await obj.guild.create_voice_channel(name=tmpchall.name, category = addedtextchat.category)
    await addedtextchat.edit(position = 0)
    await addedvoicechat.edit(position = 0)
    for i in obj.guild.channels:
        if(str(i.name) == str(i.category)): # move master chat to top 
            await i.edit(position = 0)
    obj.resp.append('new text and voice chat created')
    return obj
    

async def solved(obj):

    if(obj.message[0].lower() != 'solved'):
        return obj
    if(len(obj.message) != 1):
        obj.resp.append('Incorrect input')
        obj.resp.append('0 arguments after solved')
        return obj
    tmpchall = chall(name = str(obj.channel.name), category = str(obj.channel.category))
    if(tmpchall.category == None):
        obj.resp.append('this chat does not belong to a competition')
        return obj
    if(await check(obj)):
        obj.resp.append('master chat missing')
        return obj
    if(tmpchall.name[:7] == 'solved_'):
        obj.resp.append('already solved')
        return obj
    if(tmpchall.name == tmpchall.category):
        obj.resp.append('cannot solve master chat')
        obj.resp.append('use archive instead')
        return obj

    # 
    # input is correct 
    # 

    await obj.channel.edit(name = 'solved_'+tmpchall.name)
    await obj.channel.edit(position = 100)
    for i in obj.guild.channels: # deletes voice chat
        if(str(i.type)=='voice' and str(i.name) == tmpchall.name and str(i.category) == tmpchall.category):
            await i.delete()
    
    obj.resp.append('Congratulations you solved it!!!!!!')
    return obj

async def remove(obj):

    if(obj.message[0].lower() != 'remove'):
        return obj
    if(len(obj.message) != 2):
        obj.resp.append('Incorrect input')
        obj.resp.append('1 arguments after remove')
        obj.resp.append('iamcertain')
        return obj
    if(str(obj.message[1]) != 'iamcertain'):
        obj.resp.append('Incorrect input')
        obj.resp.append('1 arguments after remove')
        obj.resp.append('iamcertain')
        return obj
    tmpchall = chall(name = str(obj.channel.name), category = str(obj.channel.category))
    if(tmpchall.category == None):
        obj.resp.append('this chat does not belong to a competition')
        return obj
    if(await check(obj)):
        obj.resp.append('master chat missing')
        return obj
    if(tmpchall.name == tmpchall.category):
        obj.resp.append('cannot remove master chat')
        obj.resp.append('use archive or delete instead')
        return obj
    # 
    # input is correct 
    # 

    pickleempty(tmpchall.category,tmpchall.name)
    await obj.channel.delete()
    for i in obj.guild.channels: # deletes voice chat
        if(str(i.type)=='voice' and str(i.name) == tmpchall.name and str(i.category) == tmpchall.category):
            await i.delete()
    return obj

async def links(obj):

    if(obj.message[0].lower() != 'links'):
        return obj
    if(len(obj.message) != 1):
        obj.resp.append('Incorrect input')
        obj.resp.append('0 arguments after links')
        return obj
    if(obj.channel.category == None):
        obj.resp.append('this chat does not belong to a competition')
        return obj
    if(await check(obj)):
        obj.resp.append('master chat missing')
        return obj
    
    # 
    # input is correct 
    # 

    tmpchall = chall(name = str(obj.channel.name), category = str(obj.channel.category))
    obj.resplinks = picklereturn(tmpchall.category,tmpchall.name)
    return obj

async def save(obj):

    if(obj.message[0].lower() != 'save'):
        return obj
    obj.links.extend(obj.message[1:]) # move links to attchment 
    if(not obj.hasfiles()):
        obj.resp.append('no files or links added')
        return obj
    if(obj.channel.category == None):
        obj.resp.append('this chat does not belong to a competition')
        return obj
    if(await check(obj)):
        obj.resp.append('master chat missing')
        return obj

    # 
    # input is correct 
    # 

    pickleadd(str(obj.channel.category), str(obj.channel.name), obj.links)
    obj.resp.append('added links')
    obj.resplinks.extend(obj.links)
    return obj    

    