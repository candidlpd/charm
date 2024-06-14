
def common_letter(str1, str2):
    word = ""
    for ch in str1:
        if ch in str2:
            word = word + ch
    return word

def common_letter2(str1,str2):
    return [set(str1) & set(str2)]

if __name__ == "__main__":
    print("hello  python")
    str1 = "NAINA"
    str2 = "REENE"
    common_letters = common_letter(str1,str2)
    print(common_letters)

    common_letters2 = common_letter2(str1, str2)
    print(common_letters2)




