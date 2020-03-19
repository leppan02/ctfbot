import pickle
import discord
import os.path
import printformat as pf
import features

class Feature():
    def __init__(self, n, args, com, description, function):
        self.n = n
        self.com = com
        self.args = args
        self.description = description
        self.function = function

class Message():
    def __init__(self,  channel, guild, objects):
        self.command = ''
        self.message = []
        self.objects = objects
        self.response = []
        self.respobjects = []
        self.channel = channel
        self.guild = guild
        self.handled = False
        self.output = []
    
    def hasobjects(self):
        return len(self.objects)!=0

    def hasrespobjects(self):
        return len(self.respobjects)!=0
    
    def hasresponse(self):
        return len(self.response)+len(self.respobjects)!=0

    def hasmessage(self):
        return len(self.message)!=0

    def __str__(self):
        r = '\n'.join(self.response)
        o = []
        if self.hasrespobjects() :
            o = [pf.objectsheader.format(len(self.respobjects))]
            for i, l in enumerate(self.respobjects):
                o.append(pf.objects.format(num = i+1,objects = l))
        r = '\n'.join([r,'\n'.join(o)])
        return r

class CtfCompetition():
    def __init__(self, name, url, password, username):
        self.name = name
        self.url = url
        self.password = password
        self.username = username

class PersitentStorage():
    def __init__(self, name):
        self.dir = 'persistent/'+str(name)
        self.items = {}
        self.read()
        
    def write(self):
        with open( self.dir, "wb" ) as f:
            pickle.dump( self.items, f,  protocol=pickle.HIGHEST_PROTOCOL)
        return

    def read(self):
        if(os.path.exists(self.dir)):
            with open(self.dir, "rb" ) as f:
                self.items = pickle.load( f )
        else:
            self.write()
        return

    def check(self,key):
        self.read()
        if(key not in self.items.keys()):
            self.items[key] = []
            self.write()
        return
    
    def add(self ,key , listofitems):
        self.check(key)
        if type(listofitems) != type([]) :
            listofitems = [listofitems]
        self.items[key].extend(listofitems)
        self.write()
        return
    
    def get(self, key):
        self.check(key)
        return self.items[key]
    
    def remove(self, key):
        self.read()
        self.check(key)
        self.items[key] = []
        self.write()

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        await features.MessageHandling(message)
        return

    async def on_message_edit(self,before, message):
        await features.MessageHandling(message)
        return