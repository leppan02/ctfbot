from classes import *
import os.path
from os import path
import validators
import discord
from time import sleep
names = []
links = dict(dict())

async def check(obj):
    for i in obj.guild.channels:
        if(str(i.category) == str(obj.channel.category)):
            if(str(i.category) == str(i.name)):
                return False
    return True
async def add(obj):
    if(obj.message[0].lower() != 'add'):
        return obj
    if(len(obj.message) != 2):
        obj.resp.append('Incorrect input')
        obj.resp.append('1 arguments after add')
        obj.resp.append('[chall name]')
        return obj
    
    tmpchall = chall(name = obj.message[1], category = obj.channel.category)
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
    
    addedtextchat = await obj.channel.clone(name=tmpchall.name)
    addedvoicechat = await obj.guild.create_voice_channel(name=tmpchall.name, category = addedtextchat.category)
    await addedtextchat.edit(position = 0)
    await addedvoicechat.edit(position = 0)
    for i in obj.guild.channels:
        if(str(i.name) == str(i.category)):
            await i.edit(position = 0)
    obj.resp.append('new text and voice chat created')
    return obj
    
async def archive(obj):
    if(obj.message[0].lower() != 'archive'):
        return obj

    if(len(obj.message) != 2):
        obj.resp.append('Incorrect input')
        obj.resp.append('1 arguments after archive')
        obj.resp.append('iamcertain')
        return obj
    tmpchall = chall(name = str(obj.channel.name), category = str(obj.channel.category))
    if(tmpchall.category == None):
        obj.resp.append('this chat does not belong to a competition')
        return obj
    if(await check(obj)):
        obj.resp.append('master chat missing')
        return obj
    if(tmpchall.name!=tmpchall.category):
        obj.resp.append('not master chat')
        obj.resp.append('goto {}'.format(tmpchall.category))
    for i in obj.guild.channels:
        if(str(i.type)=='voice' and str(i.category) == tmpchall.category):
            await i.delete()
    await obj.channel.category.edit(position = 100)
    await obj.channel.category.edit(name = 'archive_'+tmpchall.name)
    
    obj.resp.append('archived')
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
    await obj.channel.edit(name = 'solved_'+tmpchall.name)
    await obj.channel.edit(position = 100)
    for i in obj.guild.channels:
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
        obj.resp.append('1 arguments after solved')
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
        obj.resp.append('use archive instead')
        return obj
    await obj.channel.delete()
    for i in obj.guild.channels:
        if(str(i.type)=='voice' and str(i.name) == tmpchall.name and str(i.category) == tmpchall.category):
            await i.delete()
    return obj

async def new(obj):
    if(obj.message[0].lower() != 'new'):
        return obj

    if(len(obj.message) != 5):
        obj.resp.append('Incorrect input')
        obj.resp.append('3 arguments after new')
        obj.resp.append('[website] [username] [password]')
        return obj

    tmpctf = ctf(url = obj.message[2], name = obj.message[1], username = obj.message[3], password = obj.message[4])

    if(validators.url(tmpctf.url)==False):
        obj.resp.append('url incorrect')
    

    for i in obj.guild.channels:
        if(i.name == tmpctf.name and str(i.type) == 'category'):
            print(i.name)
            obj.resp.append('name already used')

    if(await obj.hasresp()):
        return obj
    print('{0.url} {0.username} {0.password}'.format(tmpctf))
    tmpctf.category = await obj.guild.create_category(tmpctf.name)
    await tmpctf.category.edit(position = 1)
    await obj.guild.create_text_channel(name = tmpctf.name, category = tmpctf.category, topic = ('{0.url} {0.username} {0.password}'.format(tmpctf)))
    obj.resp.append('done')
    return obj
    

    
    

    