
class MessageClass():
    def __init__(self, message=[], files=[], resp=[], resplinks=[], channel = None, guild = None):
        self.message = message
        self.files = files
        self.resp = resp
        self.resplinks = resplinks
        self.channel = channel
        self.guild = guild
    
    def hasfiles(self):
        return len(self.links)!=0

    def hasrespfiles(self):
        return len(self.resplinks)!=0
    
    async def hasresp(self):
        return len(await self.output())!=0

    def hasmessage(self):
        return len(self.message)!=0

    async def output(self):
        resp = self.resp
        if(self.hasrespfiles()):
            resp.append('Here are {} links:'.format(len(self.resplinks)))
            for i, l in enumerate(self.resplinks):
                resp.append('Link #{} is {}'.format(i,l))
        return resp

class ctf():
    def __init__(self, category = None,  name = None, url = None, password = None, username = None):
        self.category = category
        self.name = name
        self.url = url
        self.password = password
        self.username = username

class chall():
    def __init__(self, name = None, category = None):
        self.name = name
        self.category = category

