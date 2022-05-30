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

def minion_game(string):
    Kevin_count = 0
    Stuart_count = 0
    processed_words = []
    for i in range(0, int((len(s)/2)+1)):
        for j in range(i, len(s)):
            word = s[i:j + 1]
            if (s[i] in ('A', 'E', 'I', 'O', 'U')):
                if (word in processed_words):
                    continue
                processed_words.append(word)
                count = CountOccurrences(string, word)
                # p = permutations(word)
                # print(len(p))
                Kevin_count += int(count)
                # print(F'Kevin {word} ' + str(Kevin_count))
            else:
                if (word in processed_words):
                    continue
                processed_words.append(word)
                # p = permutations(word)
                count = CountOccurrences(string, word)
                Stuart_count += int(count)
                # print(F'Stuart {word} ' + str(Stuart_count))
    if (Stuart_count > Kevin_count):
        print("Stuart", Stuart_count)
    elif (Stuart_count < Kevin_count):
        print("Kevin", Kevin_count)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)