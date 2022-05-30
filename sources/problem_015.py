if (__name__ == '__main__'):
    n = int(input())
    dic = {}
    for i in range(0, n):
        s = input()
        if (s in dic):
            dic[s] += 1
            continue
        dic[s] = 1

    print(len(dic))
    print(*dic.values())
