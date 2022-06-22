import re
import email.utils

if (__name__== '__main__'):
    n = int(input())
    result = []
    for i in range(0,n):
        entry = input().split()
        name = entry[0]
        mail = entry[1][1:len(entry[1]) - 1]
        #pattern = r"^[a-z0-9]+[\._-]+[a-z0-9]+[@]\w+[.]\w{2,3}$"
        pattern = r"[A-Za-z](\w|-|\.|_)+@[A-Za-z]+[\.][A-Za-z]{1,3}$"
        if (bool(re.match(pattern, mail))):
            result.append(email.utils.formataddr((name, mail)))
    for item in result:
        print(item)
