

#finding fibonacci upto  n number
def fibo(n):
    a = 0
    b = 1
    if n<0:
        print("only positive")
    elif n==0:
        return 0
    elif n ==1:
        return b
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return b





if __name__ == '__main__':
    print("fibonacci series")

# n = 9
# fibos = fibo(n)
# print(fibos)

for j in range(10):
    print(fibo(j))

