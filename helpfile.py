def help():
    h = [
    '***general commands:***',
    'new [name(one short word)] [website] [username] [password] *create new competion.*',
    'links *list saved files and links*',
    'save *saves attached files or links*',
    'alllinks *list all list in competition*',
    'delete iamcertain *deletes competion*',
    '***competition chat commands:***',
    'archive iamcertain *archive competion, use with caution.*',
    'add [chall name] *add chall text and voice chat.*',
    '***chall chat commands:***',
    'solved *moves chat to bottom, removes voice chat and changes name to solved_chall.*',
    'remove *deletes chat.*',
    '',
    '*might be buggy if you use nonascii chars*',
    '***todo:***', 
    'finding all the bugs, rsa solver, ctfd integration, command execution, ctf-katana integration, simple commands on string and files']
    return h

c = ['links','save','alllinks','delete', 'new','archive', 'add', 'solved', 'challs', 'scoreboard', 'links', 'link', 'file', 'remove']