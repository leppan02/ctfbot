from Class import Feature,Message
import printformat as pf
import servermanager
import objectmanager
import notesmanager
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
    'objects' : Feature(n = 0 , args = 'objects', com = 'objects', description = 'List all saved objects in current chall.',function=objectmanager.objects),
    '-objects' : Feature(n = 0 , args = '-objects iamcertain', com = '-objects', description = 'Deletes all saved objects in current chall.',function=objectmanager.remove),
    '+objects' : Feature(n = None , args = '+objects [attach file or link]', com = '+objects', description = 'Save links or files such as solution scripts or research links.',function=objectmanager.save),
    '+notes' : Feature(n = None, args = '+notes [very important note]', com = '+notes', description = 'Save notes sush as ssh login.',function=notesmanager.save),
    'notes' : Feature(n =  0, args = 'notes', com = 'notes', description = 'List saved notes in current chall.',function=notesmanager.notes),
    '-notes' : Feature(n =  0, args = '-notes', com = '-notes', description = 'Removes saved notes in current chall.',function=notesmanager.remove),
    'delete' : Feature(n =  1, args = 'delete iamcertain', com = 'delete', description = 'Deletes current competion.',function=servermanager.delete),
    'archive' : Feature(n =  1, args = 'archive iamcertain', com = 'archive', description = 'Archive current competion.',function=construction),
    'solved' : Feature(n = 1 , args = 'solved [flag]', com = 'solved', description = 'Tags chall with solved_.',function=servermanager.solved),
    'remove' : Feature(n = 1 , args = 'remove iamcertain', com = 'remove', description = 'Remove current chall.',function=servermanager.remove),
    'change' : Feature(n = 3 , args = 'change [url] [username] [password]', com = 'change', description = 'Change description in competition chat.',function=servermanager.change)
}