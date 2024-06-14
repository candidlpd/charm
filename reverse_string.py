
def rev1(str1):
    return str1[::-1]


def rev2(str2):
    res = "".join(reversed(str2))
    return res


def rev3(str3):
    new_str =[]
    for i in range(len(str3)-1,-1,-1):
        new_str.append(str3[i])
        res = "".join(new_str)
    return res



def rev4(str4):
    empty_str = ""
    for i in range(len(str4)):
        empty_str = str4[i] + empty_str
    return empty_str


def rev5(str5):
    output = ''
    i = len(str5)-1
    while i>=0:
        output = output + str5[i]
        i = i-1
    return output

str6 = "learning python is very easy"
def rev6(str6):
    str6_list = str6.split()
    l= []
    for word in str6_list:
        l.append(word[::-1])
        output = ' '.join(l)
    return output











if __name__ == "__main__":
    print("string reverse examples")
    str1 = "durga"



rev1s = rev1(str1)
print(rev1s)


rev2s = rev2(str1)
print(rev2s)

rev3s = rev3(str1)
print(rev3s)


rev4s = rev4(str1)
print(rev4s)


rev5s = rev5(str1)
print(rev5s)



rev6s = rev6(str6)
print(rev6s)