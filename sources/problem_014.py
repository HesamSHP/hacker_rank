def merge_the_tools(string, k):
    n = len(string)
    division = []
    division = [string[i:i + k] for i in range(0, len(string), k)]
    # print(division)
    for item in division:
        chain = ""
        for c in range(0, len(item)):
            if (chain.count(item[c]) <= 0):
                chain += item[c]
        item = chain
        print(item)
    return

if (__name__ == '__main__'):
    string, k = input(), int(input())
    merge_the_tools(string, k)





