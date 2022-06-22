if (__name__ == "__main__"):
    A = list(map(int, input().split()))
    n = int(input())
    result = True
    for i in range(0, n-1):
        found_exception = False
        set_temp = list(map(int, input().split()))
        for item in set_temp:
            if (item not in A):
                found_exception = True
                result = False
                break
        if (found_exception != True & len(A) > len(set_temp)):
            result = True
        else:
            result = False
            break
    print(result)
