def checkForRule1(s):
    if (s[0] not in ['4', '5','6']):
        return False
    return True
def checkForRule2(s):
    if ((str(s).__contains__('-')) and (len(s) != 19)):
        return False
    elif ((not str(s).__contains__('-')) and (len(s) != 16)):
        return False
    return True
def checkForRule3(s):
    if (str(s).__contains__('-')):
        splitted_string = s.split('-')
        for item in splitted_string:
            if ((not item.isnumeric()) or (len(item) != 4)):
                return False
    return True
def checkForRule4(s):
    if ((len(s) != 16) and (len(s) != 19)):
        return False
    elif ((len(s) == 16) and (not s.isnumeric())):
        return False
    elif ((len(s) == 19) and str(s).count('-') != 3):
        return False
    return True
def checkForRule5(s):
    repeatedChar = 0
    preChar = s[0]
    for char in s:
        if (not char.isdigit()):
            continue
        if (char == preChar):
            repeatedChar += 1
        else:
            repeatedChar = 1
        if (repeatedChar >= 4):
            return False
        preChar = char
    return True
# def checkForRule6(s):
#     if (s[0] not in ['4', '5','6']):
#         return False

if (__name__== "__main__"):
    n = int(input())
    result = []
    for i in range(0,n):
        entry= input()
        answer = (checkForRule1(entry) and checkForRule2(entry) and checkForRule3(entry) and checkForRule4(entry) and checkForRule5(entry))
        if (answer):
            result.append('Valid')
        else:
            result.append('Invalid')

for item in result:
    print(item)
