def print_rangoli(size):
    a= 97
    ch = a + size
    line_width = 4 * (size - 1) + 1
    step = -1
    message = ""
    for i in range(ch - 1,a-1, -1):
        # step += 1
        if (i == ch -1):
            message += chr(i)
        else:
            message += chr(i)
            for j in range(i+1, ch):
                message = chr(j) + '-' + message
                message += '-' + chr(j)
        print(message.center(line_width, '-'))
        message = ""

    for i in range(a+1, ch):
        if (i == ch -1):
            message += chr(i)
        else:
            message += chr(i)
            for j in range(i + 1, ch):
                message = chr(j) + '-' + message
                message += '-' + chr(j)
        print(message.center(line_width, '-'))
        message = ""

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)