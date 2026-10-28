# function to check whether first and last characters of a string are same or not
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 0 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words whith same first and last character\n", lst)
    return ctr


count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words with same first and last character:", count)