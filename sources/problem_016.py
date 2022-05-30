from collections import deque

if (__name__ == '__main__'):
    n = int(input())
    d = deque()
    for i in range(0, n):
        command = input()
        if (command.split()[0] == 'append'):
            d.append(command.split()[1])
        elif (command.split()[0] == 'appendleft'):
            d.appendleft(command.split()[1])
        elif (command.split()[0] == 'pop'):
            d.pop()
        elif (command.split()[0] == 'popleft'):
            d.popleft()
        elif (command.split()[0] == 'clear'):
            d.clear()
        elif (command.split()[0] == 'remove'):
            d.remove(command.split()[1])
        elif (command.split()[0] == 'extend'):
            d.extend(command.split()[1])
        elif (command.split()[0] == 'extendleft'):
            d.extendleft(command.split()[1])
        elif (command.split()[0] == 'reverse'):
            d.reverse()
        elif (command.split()[0] == 'rotate'):
            d.rotate()
    print(*d)