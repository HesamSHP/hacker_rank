def sort_func(e):
    return e[1]
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=sort_func)
    second_lowest = students[0][1]
    for item in students:
        if (item[1] > second_lowest):
            second_lowest = item[1]
            break

    result= []
    for item in students:
        if (item[1] == second_lowest):
            result.append(item[0])
    result.sort()
    for item in result:
        print(item)


