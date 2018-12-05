""" Inverter """

def topfy():
    """ 0 -> 1 Experimental"""
    code = input()
    detect = ''
    for i in code:
        if i == '0':
            detect += '1'
        elif i == '1':
            detect += '0'
    if detect.find('1') >= 1:
        print(detect[detect.find('1'):])
    elif detect.find('0'):
        print(detect)
topfy()
