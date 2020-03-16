from classes import *
import os.path
from os import path

import urllib3
import discord
from time import sleep
import pickle
lk = dict()
pdir = 'pkl/ctfpickle.pkl'


def picklewrite():
    with open( pdir, "wb" ) as f:
        pickle.dump( lk, f,  protocol=pickle.HIGHEST_PROTOCOL)
    print(lk)
    return
def pickleread():
    global lk
    if(os.path.exists(pdir)):
        print(1)
        with open( pdir, "rb" ) as f:
            lk = pickle.load( f )
    else:
        picklewrite()
    return
def pickleempty(cat, name):
    pickleread()
    lk[(cat,name)] = []
    picklewrite()
    return
def pickleadd(cat , name , toadd):
    global lk
    pickleread()
    lk[(cat,name)].extend(toadd)
    picklewrite()
    return
def picklereturn(cat, name):
    pickleread()
    print(lk[(cat,name)])
    return lk[(cat,name)]
async def check(obj):
    for i in obj.guild.channels:
        if(str(i.category) == str(obj.channel.category)):
            if(str(i.category) == str(i.name)):
                return False
    return True
  