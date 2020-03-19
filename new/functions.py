import Class
import printformat as pf

class function():
    def __init__(self, n, args, com, description, function):
        self.n = n
        self.com = com
        self.args = args
        self.description = description
        self.function = function

def construction(obj):
    obj.response = ['under construction']
    obj.respobjects = ['link']
    obj.handled = True
    return
    
funclist = {
    'new' : function(n = 4 , args = 'new [name] [url] [username] [password]', com = 'new', description = 'Create new competion.',function=construction),
    'add' : function(n = 1 , args = 'add [name]', com = 'add', description = 'Add new chall.',function=construction),
    'objects' : function(n = 0 , args = 'objects', com = 'objects', description = 'List all saved objects.',function=construction),
    'save' : function(n = None , args = 'save [attach file or link]', com = 'save', description = 'Save links or file such as solution script or research link.',function=construction),
    'addcred' : function(n = None, args = 'addcred [cred]', com = 'cred', description = 'Save credentials sush as ssh login.',function=construction),
    'listcred' : function(n =  0, args = 'listcred', com = 'listcred', description = 'List saved credentials.',function=construction),
    'delete' : function(n =  1, args = 'delete iamcertain', com = 'delete', description = 'Deletes current competion.',function=construction),
    'archive' : function(n =  1, args = 'archive iamcertain', com = 'archive', description = 'Archive current competion.',function=construction),
    'solved' : function(n = 0 , args = 'solved [flag]', com = 'solved', description = 'Tags chall with solved_.',function=construction),
    'remove' : function(n = 1 , args = 'remove iamcertain', com = 'remove', description = 'Remove current chall.',function=construction)
}
