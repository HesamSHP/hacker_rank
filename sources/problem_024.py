import re

if (__name__ == "__main__"):
    n = int(input())

    for i in range(0, n-1):
        code = input()
        if (re.match("^#",code)):
            continue
        iterations = re.findall("#[0-9a-fA-F]+", code)

        for item in iterations:
            if (len(item) >= 3):
                print(item)
