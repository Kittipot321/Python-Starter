""" Coprimes """

def gcd(num, num2):
    """ Greatest Common Division """
    nums = min(num, num2)
    answer = max(num, num2)
    for i in range(nums, 0, -1):
        if num%i == 0 and num2%i == 0:
            answer = i
            break
    return answer

def coprime(num, num2):
    """ integer 2 amounts -> Y/N """
    gcdv1 = gcd(num, num2)
    if gcdv1 == 1:
        print("YES")
    else:
        print("NO")
    print(gcdv1)
coprime(int(input()), int(input()))
