import keyboard


def translateKeypress(keys): 
    # Takes a list of events and translates them according to my use
    returnList = []
    toAppend = False
    for i in keys[:-1]:
        if i.event_type=='up' and i.name == ";":
            toAppend=True
        if i.event_type=='down' and toAppend==True and i.name not in ['right alt', 'right windows', 'ctrl', 'right shift', 'left shift', 'alt', 'alt gr', 'left ctrl', 'right ctrl', 'windows', 'shift', 'left windows', 'left alt']:
            if i.name == 'space':
                i.name = " "
            if i.name == 'backspace':
                try:
                    returnList.pop(-1)
                except IndexError:
                    pass
                continue
            returnList.append(i.name)
    return "".join(returnList)
def dumpResult(keys):
    with open('exchanger','w') as f:
        f.write(keys)
while True:        
    dumpResult(translateKeypress(keyboard.record(until='caps lock')))