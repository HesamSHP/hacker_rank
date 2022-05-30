if (__name__== '__main__'):
    n, m = map(int, input().split())
    print(n,m)
    pattern = '.|.'
    line = ''
    for i in range(n//2):
        print((pattern*((i*2)+1)).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in range(n//2-1,-1, -1):
        print((pattern*((i*2)+1)).center(m, '-'))
