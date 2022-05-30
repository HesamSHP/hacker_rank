if __name__ == '__main__':
    n = 5 #int(input())
    arr = map(int, '34 50 50 50'.split())

    #5
    #2    3    6    6    5
    winner =0
    runner_up = 0

    arr_sorted = sorted(arr)
    print(arr_sorted)
    for i in range(len(arr_sorted) -2,-1,-1):
        if ( arr_sorted[i] !=  arr_sorted[i+1]):
            runner_up =arr_sorted[i]
            break

    print(runner_up)