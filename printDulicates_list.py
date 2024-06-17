

def print_duplicates1(l1):
    counts ={}

    for ele in l1:
        if ele in counts:
            counts[ele] += 1
        else:
            counts[ele] = 1

    unique = []
    for k,v in counts.items():
        if v>1:
            unique.append(k)
    return unique



def print_duplicates2(l1):
    l2=[]
    for ele in l1:
        if l1.count(ele)>1:
            l2.append(ele)
    return set(l2)


def print_duplicates3(l1):
    unique=[]
    dup =[]
    for ele in l1:
        if ele not in unique:
            unique.append(ele)
        else:
            dup.append(ele)
    return dup


def print_duplicates4(l1):
    l2=[]
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i] == l1[j] and l1[i] not in l2:
                l2.append(l1[i])
    return l2




if __name__ == '__main__':
    print("print duplicates from list")
    l1 = [1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 7, 9]
    print(print_duplicates1(l1))

    print(print_duplicates2(l1))

    print(print_duplicates3(l1))


    print(print_duplicates4(l1))