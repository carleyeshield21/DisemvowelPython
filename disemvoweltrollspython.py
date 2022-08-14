# This is the link to this Python Coding Challenge
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel():
    str = input('Type any word/phrase/sentence:\n')
    # print(str)
    vowels = 'aeiouAEIOU'
    # print(str)
    newstr = str
    # counter = 0
    for i in vowels:
        for j in str:
            # print(i, j)
            if i == j:
                # counter += 1
                # print(i)
                newstr = newstr.replace(i,'')
        # print('========')
    # print(counter)
    print(newstr)
disemvowel()