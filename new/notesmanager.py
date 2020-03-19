import Class
from servermanager import notvalid
async def save(obj):
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    if len(obj.message)== 0:
        obj.response.append('No notes saved.')
        return False
    s = Class.PersitentStorage('notes')
    s.add( (obj.channel.category.id,obj.channel.id), [' '.join(obj.message)])
    obj.response.append('added {}'.format(' '.join(obj.message) ))
    return True

async def notes(obj):
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    s = Class.PersitentStorage('notes')
    obj.respobjects.extend(s.get( (obj.channel.category.id,obj.channel.id)))
    return True

async def remove(obj):
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    s = Class.PersitentStorage('notes')
    n = s.remove( (obj.channel.category.id,obj.channel.id) )
    obj.response.append('removed {} note(s)'.format(n))
    return True
