""" Milk """

def main(price, stem, free, money):
    """ Main Function """
    lid = money//price
    cup = lid
    while cup >= stem and stem > 0:
        freemilk = (cup //stem) * free
        cup = cup%stem
        cup += freemilk
        lid += freemilk
    print(lid)
main(int(input()), int(input()), int(input()), int(input()))
