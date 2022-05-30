# Enter your code here. Read input from STDIN. Print output to STDOUT
def sortDigit(item1):
    if ((int(item1) % 2 == 0)):
        return 1
    elif ((int(item1) % 2 != 0)):
        return 0
    return 0


if (__name__ == '__main__'):
    s = input()
    result = ""

    uppercaseChars = []
    lowercasechars = []
    digits = []
    for i in range(len(s)):
        if ((ord(s[i]) >= 65) & (ord(s[i])<= 90)):
            uppercaseChars.append(s[i])
        if ((ord(s[i]) >= 97) & (ord(s[i])<= 122)):
            lowercasechars.append(s[i])
        if ((ord(s[i]) >= 48) & (ord(s[i])<= 57)):
            digits.append(s[i])
    uppercaseChars.sort()
    lowercasechars.sort()
    digits.sort()
    digits.sort(key=sortDigit)
    print(*lowercasechars,*uppercaseChars,*digits, sep='')

