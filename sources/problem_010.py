def print_formatted(number):
    txt = ""
    length = len(bin(number)[2:])
    format_binary = '{0:' + str(length) +'b}'
    for i in range(1, number+1, 1):
        decimal = ("%i" % i).rjust(length, " ")
        octal = ("%o" % i).rjust(length, " ")
        hexa = ("%X" % i).rjust(length, " ")
        binary = (f"{format_binary}".format(i)).rjust(length, " ")
        txt = f"{decimal} {octal} {hexa} {binary}"
        print(txt)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)