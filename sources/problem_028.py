def hasRepeatedChars(s):
    for i in range(len(s)):
        if i != s.rfind(s[i]):
            return True
    return False

if (__name__== "__main__"):
    n = int(input())
    result = []
    for i in range(0,n):
        entry= input()
        uppercasechars = 0
        lowercasechars = 0
        digits = 0
        for char in entry:
            if (ord(char) >= 97 and ord(char) <= 122):
                lowercasechars += 1
            if (ord(char) >= 65 and ord(char) <= 90):
                uppercasechars += 1
            if (ord(char) >= 48 and ord(char) <= 57):
                digits += 1
        if ((uppercasechars >= 2) and (digits >= 3) and (lowercasechars + uppercasechars + digits == len(entry)) and (len(entry) == 10) and (not hasRepeatedChars(entry))):
            result.append('Valid')
        else:
            result.append('Invalid')

for item in result:
    print(item)


