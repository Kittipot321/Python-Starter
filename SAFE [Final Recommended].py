""" SAFE """

def topfy(key, text, box, answer):
    """ Main Function """
    for character in key:
        box.append(ord(character))
    for character in text:
        box.append(ord(character))
    save = len(key+text)
    for i in range(int(save/2)):
        aaa = box[i]-box[int(save/2+i)]
        aaa = abs(aaa)
        if aaa > 13:
            aaa -= 26
        answer.append(abs(aaa))
    print(sum(answer))
topfy(input(), input(), [], [])
