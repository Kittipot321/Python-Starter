""" Keymidterm """

def main():
    """ Mian Function """
    num = input()
    i = 0
    total = 0
    dos = 1
    while i <= 12:
        ans = num[i:dos]
        total += int(ans)
        dos += 1
        i += 1

    das = (int(num)%1000)*10
    totaln = (das+total)
    if totaln <= 1000:
        totaln = totaln + 1000
        print(totaln)
    elif totaln >= 10000:
        totals = totaln%1000
        print("%04d" %(totals))
    else:
        print(totaln)
main()
