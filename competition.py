import validators
import discord


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

    # 
    # input is correct 
    # 

    for i in obj.guild.channels:
        if(str(i.type)=='voice' and str(i.category) == tmpchall.category):
            await i.delete()
    await obj.channel.category.edit(position = 100)
    await obj.channel.category.edit(name = 'archive_'+tmpchall.name)
    obj.resp.append('archived')
    return obj

async def new(obj):

    if(obj.message[0].lower() != 'new'):
        return obj
    if(len(obj.message) != 5):
        obj.resp.append('Incorrect input')
        obj.resp.append('4 arguments after new')
        obj.resp.append('[name] [website] [username] [password]')
        return obj
    tmpctf = ctf(url = obj.message[2], name = obj.message[1].lower(), username = obj.message[3], password = obj.message[4])
    if not validators.url(tmpctf.url):
        obj.resp.append('url incorrect')
        return obj
    for i in obj.guild.channels:
        if(i.name == tmpctf.name and str(i.type) == 'category'):
            print(i.name)
            obj.resp.append('name already used')
            return obj
    if(await obj.hasresp()):
        return obj

    # 
    # input is correct 
    # 
    pickleempty(str(obj.channel.category), obj.channel.id)
    tmpctf.category = await obj.guild.create_category(tmpctf.name)
    await tmpctf.category.edit(position = 1)
    await obj.guild.create_text_channel(name = tmpctf.name, category = tmpctf.category, topic = ('{0.url} {0.username} {0.password}'.format(tmpctf)))
    obj.resp.append('done')
    return obj

async def erase(obj):
    if(obj.message[0].lower() != 'delete'):
        return obj
    if(len(obj.message) != 2):
        obj.resp.append('Incorrect input')
        obj.resp.append('1 arguments after delete')
        obj.resp.append('iamcertain')
        return obj
    if(str(obj.message[1]) != 'iamcertain'):
        obj.resp.append('Incorrect input')
        obj.resp.append('1 arguments after delete')
        obj.resp.append('iamcertain')
        return obj
    tmpchall = chall(name = str(obj.channel.name), category = str(obj.channel.category))
    if(tmpchall.category == None):
        obj.resp.append('this chat does not belong to a competition')
        return obj
    if(await check(obj)):
        obj.resp.append('master chat missing')
        return obj
    if(tmpchall.name != tmpchall.category):
        obj.resp.append('send in master chat')
        obj.resp.append('use remove or solve instead for chall command')
        return obj

    # 
    # input is correct 
    # 
    
    pickleempty(str(obj.channel.category), obj.channel.id)
    await obj.channel.delete()
    for i in obj.guild.channels:
        if(str(i.category) == tmpchall.category):
            await i.delete()
    for i in obj.guild.channels:
        if(str(i.name) == tmpchall.name):
            await i.delete()
    return obj


async def alllinks(obj):

    if(obj.message[0].lower() != 'alllinks'):
        return obj
    if(len(obj.message) != 1):
        obj.resp.append('Incorrect input')
        obj.resp.append('0 arguments after alllinks')
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

    for i in obj.guild.channels:
        if i.category.id == obj.channel.category.id:
            obj.resplinks.extend(picklereturn(i.category,i.id))
    return obj  