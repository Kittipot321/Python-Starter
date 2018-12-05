""" Classify """

def classify(student):
    """ This code is hard for me. """
    while True:
        stid = input()
        if stid == 'END':
            break
        student.append(stid)
    stdict = {}
    for std in student:
        key = int(std[0:2]), int(std[2:4])
        stdict[key] = stdict.get(key, 0) + 1
    prev = ''
    for key in sorted(stdict):
        if key[0] != prev:
            print(key[0], key[1], stdict[key])
            prev = key[0]
        else:
            print('--', key[1], stdict[key])
classify([])
