if (__name__ == '__main__'):
    T = int(input())
    result = []

    for i in range(0, T):
        found_exception = False
        number_of_elements_in_A = int(input())
        A = list(map(int, input().split()))
        number_of_elements_in_B = int(input())
        B = list(map(int, input().split()))
        for item in A:
            if (item not in B):
                result.append('False')
                found_exception = True
                break
        if (found_exception == False):
            result.append('True')
    for item in result:
        print(item)
