

def freq_of_char(str1):
    d ={}
    for chr in str1:
        if chr in d:
            d[chr] += 1
        else:
            d[chr]  = 1
    return d

from collections import Counter

def freq_of_char2(str2):
    return Counter(str2)


if __name__ == "__main__":
    str1 = "mississippi"
    freq_of_chars = freq_of_char(str1)
    print(freq_of_chars)

    str2 = "Mississippiiiii"
    freq_of_chars2 = freq_of_char2(str2)
    print(freq_of_chars2)





