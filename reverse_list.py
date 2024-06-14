

def rev(list1):
    result = []
    for i in range(len(list1)-1,-1,-1):
        result.append(list1[i])
    return result

def rev2(list2):
    return list2[::-1]

def rev3(list3):
    return list(reversed(list3))

def rev4(list4):
    new_list =[]
    for num in list4:
        new_list.insert(0, num)
    return new_list


def rev5(list5):
    result5 = [list5[len(list5) - i] for i in range(1, len(list5)+1)]
    return result5

def rev6(list6):
    left = 0
    right = len(list6)-1
    while(left<right):
        temp = list6[left]
        list6[left] = list6[right]
        list6[right]= temp
        left += 1
        right -= 1
    return list6



if __name__ == '__main__':
    print('Starting main program')
    list1 = [2, 33, 4, -5, 100, 8, 10, 45]

    revs = rev(list1)
    print(revs)

    rev2s = rev2(list1)
    print(rev2s)

    rev3s = rev3(list1)
    print(rev3s)

    rev4s = rev4(list1)
    print(rev4s)

    rev5s = rev5(list1)
    print(rev5s)

    rev6s = rev6(list1)
    print(rev6s)




