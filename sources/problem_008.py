import textwrap

def wrap(string, max_width):
    result = ""
    return textwrap.fill(string, max_width)


# def wrap(string, max_width):
#     result = ""
#     for i in range(0, len(string), max_width):
#         result += string[i:i+max_width] + '\n'
#
#
#     return result


if (__name__ == '__main__'):
    s = input()
    max_length = int(input())
    if (len(s) > 1000 | max_length< len(s)):
        quit()
    print(wrap(s, max_length))


