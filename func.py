import Class
import functions

async def notvalid(obj):
    for i in obj.guild.channels:
        if(str(i.category) == str(obj.channel.category) and str(i.category) == str(i.name)):
            return False
    return True

async def messagehandling(message):
    if message.content.split(' ')[0].lower() != 'ctf':
        return
    obj = Class.Message(command = '' ,message = [], channel = message.channel, guild = message.guild)
    if len( message.content.split(' ') ) != 1:
        obj.command = message.content.split(' ')[1]
        obj.message = message.content.split(' ')[2:]
    else:
        obj = Class.Message(command = message.content.split(' ')[1] ,message = message.content.split(' ')[2:], channel = message.channel, guild = message.guild)
        for i in message.attachments:
            obj.objects.append(i.url)

    for i in funclist.values():
        if i.com == obj.command:
            obj.handled = True
            if i.n == None or i.n == len(obj.message):
                if(i.function(obj)):
                    obj.response.append(pf.bad_arguments.format(num = i.n, arguments = i.args))
            else:
                obj.response.append(pf.bad_arguments.format(num = i.n, arguments = i.args))
    if(not obj.handled):
        obj.response.append(pf.helpheader)
        for i in funclist.values():
            obj.response.append(pf.helpmessage.format(i))
    return
    if obj.hasresponse():
        await message.channel.send(obj)
    return