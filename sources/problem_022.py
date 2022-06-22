import re

if (__name__== '__main__'):
    n = int(input())
    result = []
    for i in range(0,n):
        phone = input()
        pattern = r"[789]\d{9}"

        result.append(bool(re.match(pattern, phone)))
    for item in result:
        if (item):
            print("YES")
        else:
            print("NO")

#9587456281