""" ProgessiveTAX """

def topfy():
    """ Calculate of Thai Tax in daily life"""
    num = int(input())
    total = 0
    if num >= 0 and num <= 150000:
        total += 0
    elif num > 150000 and num <= 300000:
        total = (num - 150000) * 0.05
    elif num > 300000 and num <= 500000:
        total = ((num - 300000) * 0.10) + 7500
    elif num > 500000 and num <= 750000:
        total = ((num - 500000) * 0.15) + 27500
    elif num > 750000 and num <= 1000000:
        total = ((num - 750000) * 0.20) + 65000
    elif num > 1000000 and num <= 2000000:
        total = ((num - 1000000) * 0.25) + 115000
    elif num > 2000000 and num <= 4000000:
        total = ((num - 2000000) * 0.30) + 365000
    elif num > 4000000:
        total = ((num - 4000000) * 0.35) + 965000
    print(int(total))
topfy()
