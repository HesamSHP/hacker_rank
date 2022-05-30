def mutation(string, origin, step = 0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        count = CountOccurrences(origin, "".join(string))
        # print("".join(string), count)
        return count
    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [c for c in string]
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the stringthat has not been swapped yet
        return (mutation(string_copy, origin, step + 1))

def minion_game(string):
    Kevin_count = 0
    Stuart_count = 0
    processed_words = []
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            word = s[i:j + 1]
            if (s[i] in ('A', 'E', 'I', 'O', 'U')):
                if (word in processed_words):
                    continue
                processed_words.append(word)
                Kevin_count += int(mutation(word, s))
                print(F'Kevin {word} ' + str(mutation(word, s)))
            else:
                if (word in processed_words):
                    continue
                processed_words.append(word)
                Stuart_count += int(mutation(word, s))
                # print(F'Stuart {word} ' + str(mutation(word, s)))
    # print("Kevin", Kevin_count)
    if (Stuart_count > Kevin_count):
        print("Stuart", Stuart_count)
    elif (Stuart_count < Kevin_count):
        print("Kevin", Kevin_count)
    else:
        print('Draw')


def CountOccurrences(string, substring):
    # Initialize count and start to 0
    count = 0
    start = 0

    # Search through the string till
    # we reach the end of it
    while start < len(string):

        # Check if a substring is present from
        # 'start' position till the end
        pos = string.find(substring, start)

        if pos != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            start = pos + 1

            # Increment the count
            count += 1
        else:
            # If no further substring is present
            break
    # return the value of count
    return count

if __name__ == '__main__':
    s = input()
    minion_game(s)
