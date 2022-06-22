if (__name__ == "__main__"):
    A = set(map(int, input().split()))
    n = int(input())
    result = True

    for i in range(0, n):
        set_temp = set(map(int, input().split()))
        if ((not A.issuperset(set_temp)) | (len(A)<= len(set_temp))):
            result = False
            break
    print(result)