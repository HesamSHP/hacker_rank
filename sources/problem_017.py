from collections import deque

if (__name__ == '__main__'):
    T = int(input())
    result = []
    for i in range(0, T):
        n = int(input())
        alist = input().split(' ', n-1)
        cubes = map(int, alist)
        d = deque(cubes)
        max_value = 100000
        res = 'Yes'
        for j in range(0, n):
            left = 0
            right = 0
            local_value = 0
            if (len(d) != 0):
                left = d.popleft()
                local_value = left
            if (len(d) != 0):
                right = d.pop()
                local_value = right if right > left else left
            if (local_value > max_value):
                res = 'No'
            max_value = local_value
        result.append(res)
    for item in result:
        print(item)

# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2
