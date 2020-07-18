import Class
from servermanager import notvalid
async def save(obj):
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    if len(obj.message) + len(obj.objects) == 0:
        obj.response.append('No objects saved.')
        return False
    s = Class.PersitentStorage('linksandfiles')
    s.add( (obj.channel.category.id,obj.channel.id), obj.message+obj.objects)
    obj.response.append('added {} items'.format(len(obj.message) + len(obj.objects)))
    return True

async def objects(obj):
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    s = Class.PersitentStorage('linksandfiles')
    obj.respobjects.extend(s.get( (obj.channel.category.id,obj.channel.id)))
    return True

async def remove(obj):
    if notvalid(obj):
        obj.response.append('Not a valid competition.')
        return True
    s = Class.PersitentStorage('linksandfiles')
    n = s.remove( (obj.channel.category.id,obj.channel.id) )
    obj.response.append('removed {} item(s)'.format(n))
    return True
