from Class import Feature,Message
import printformat as pf
import servermanager
BOTNAME = 'ctf'

def construction(obj):
    obj.response = ['feature under construction']
    return

async def MessageHandling(message):
    if message.content.split(' ')[0].lower() != BOTNAME:return

    obj = Message(channel = message.channel, guild = message.guild, objects = [i.url for i in message.attachments])
    if len( message.content.split(' ') ) != 1:
        obj.command = message.content.split(' ')[1]
        obj.message = message.content.split(' ')[2:]
            
    for i in featurelist.values():
        if i.com != obj.command: continue
        obj.handled = True
        if i.n in (None,len(obj.message)): 
            if await i.function(obj): continue
        obj.response.append(pf.bad_arguments.format(num = i.n, arguments = i.args))

    if not obj.handled:obj.response.extend([pf.helpheader]+[pf.helpmessage.format(i) for i in featurelist.values()])

    if obj.hasresponse():
        await message.channel.send(obj)
    return

featurelist = {
    'new' : Feature(n = 4 , args = 'new [name] [url] [username] [password]', com = 'new', description = 'Create new competion.',function=servermanager.new),
    'add' : Feature(n = 1 , args = 'add [name]', com = 'add', description = 'Add new chall.',function=servermanager.add),
    'objects' : Feature(n = 0 , args = 'objects', com = 'objects', description = 'List all saved objects.',function=construction),
    'save' : Feature(n = None , args = 'save [attach file or link]', com = 'save', description = 'Save links or file such as solution script or research link.',function=construction),
    'addcred' : Feature(n = None, args = 'addcred [cred]', com = 'cred', description = 'Save credentials sush as ssh login.',function=construction),
    'listcred' : Feature(n =  0, args = 'listcred', com = 'listcred', description = 'List saved credentials.',function=construction),
    'delete' : Feature(n =  1, args = 'delete iamcertain', com = 'delete', description = 'Deletes current competion.',function=servermanager.delete),
    'archive' : Feature(n =  1, args = 'archive iamcertain', com = 'archive', description = 'Archive current competion.',function=construction),
    'solved' : Feature(n = 0 , args = 'solved [flag]', com = 'solved', description = 'Tags chall with solved_.',function=construction),
    'remove' : Feature(n = 1 , args = 'remove iamcertain', com = 'remove', description = 'Remove current chall.',function=servermanager.remove)
}