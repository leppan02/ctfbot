import discord
import structs
import printformat as pf


def notvalid(obj):
    for i in obj.guild.channels:
        if(str(i.category) == str(obj.channel.category) and str(i.category) == str(i.name)):
            return False
    return True


async def new(obj):
    ctf = structs.CtfCompetition(url=obj.message[1], name=obj.message[0].lower(
    ), username=obj.message[2], password=obj.message[3])

    for i in obj.guild.channels:
        if(i.name != ctf.name or str(i.type) != 'category'):
            continue
        obj.response.append('Channel already exists')
        return True

    ctf.category = await obj.guild.create_category(ctf.name)

    await obj.guild.create_text_channel(name=ctf.name, category=ctf.category, topic=(pf.description.format(ctf)))
    await obj.guild.create_voice_channel(name=ctf.name, category=ctf.category)
    await ctf.category.edit(position=1)
    obj.response.append(pf.commandsuccesfull.format(
        obj.command+' '+' '.join(obj.message)))
    return True


async def add(obj):
    newname = obj.message[0]
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True

    for i in obj.guild.channels:
        if str(i.name) != str(newname) or str(i.category) != str(obj.channel.category):
            continue
        obj.response.append('Channel already exists')
        return True

    addedtextchat = await obj.channel.clone(name=newname)
    addedvoicechat = await obj.guild.create_voice_channel(name=newname, category=obj.channel.category)
    await addedtextchat.edit(position=0)
    await addedvoicechat.edit(position=0)

    for i in obj.guild.channels:
        # move master chat to top
        if str(i.name) == str(i.category) and str(i.category) == str(obj.channel.category):
            await i.edit(position=0)

    obj.response.append(pf.commandsuccesfull.format(
        obj.command+' '+' '.join(obj.message)))
    return obj


async def delete(obj):
    if obj.message[0] != 'iamcertain':
        return False

    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    cat = obj.channel.category
    for i in obj.guild.channels:
        if i.category == cat and i != cat:
            await i.delete()
    await cat.delete()
    return True


async def remove(obj):
    if obj.message[0] != 'iamcertain':
        return False
    if str(obj.channel) == str(obj.channel.category):
        obj.response.append('Cannot remove master chat.')
        return True
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    cat = obj.channel.category
    name = str(obj.channel)
    for i in obj.guild.channels:
        if i.category == cat and str(i) == name:
            await i.delete()
    return True

async def archive(obj):
    if obj.message[0] != 'iamcertain':
        return False
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    name = str(obj.channel)
    cat = str(obj.channel.category)
    if(name.startswith('archived_')):
        obj.response.append('already archived')
        return True
    if name != cat:
        obj.response.append('Must be in master chat.')
        return True
    for i in obj.guild.channels:
        if i.category == obj.channel.category and str(i.type) == 'voice':
            await i.delete()
    await obj.channel.edit(name='archived_'+name)
    return True


async def solved(obj):
    if str(obj.channel) == str(obj.channel.category):
        obj.response.append('Cannot solve master chat.')
        return True
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    name = str(obj.channel)
    if(name[:7] == 'solved_'):
        obj.response.append('already solved')
        return True
    cat = obj.channel.category
    objname = obj.channel

    await objname.edit(name='solved_'+name, position=100)
    for i in obj.guild.channels:
        if i.category == cat and str(i) == name:
            await i.delete()
    obj.response.append('Goodjob, one more off the list! :)')
    return True


async def change(obj):
    ctf = structs.CtfCompetition(
        url=obj.message[0], name='', username=obj.message[1], password=obj.message[2])
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True

    cat = obj.channel.category
    for i in obj.guild.channels:
        if i.category == cat and str(i.type) == 'text':
            await i.edit(topic=(pf.description.format(ctf)))
    return True
