def fact1(n):
    if n < 0:
        print("no factorial for negative nummber")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial = factorial * i
        return factorial


def fact2(n):
    if n < 0:
        print("no factorial for negative nummber")
    elif n == 0 or n == 1:
        return 1
    else:
        return n*fact2(n-1)






if __name__ == '__main__':
    print("factorial methods")
    n = 6
    fact1s = fact1(n)
    print(fact1s)

    fact2s = fact2(n)
    print(fact2s)





