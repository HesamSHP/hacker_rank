# if __name__ == "__main__":
#     n = int(input())
#     dic_students = {}
#     for _ in range(n):
#         entry = input()
#         lst_entry = entry.split()
#         dic_students.setdefault(lst_entry[0], lst_entry[1:])
#
#     selected_student = str(input())
#     sum = 0
#     for grade in dic_students[selected_student]:
#         sum += int(grade)
#
#     print(f"{sum/3:0.2f}")


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    sum = 0
    for grade in student_marks[query_name]:
        sum += grade

    print(student_marks)
    print(sum)
    print(f"{sum/3:0.2f}")



# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika