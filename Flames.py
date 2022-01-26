print("WELCOME TO THE WORLD OF FLAMES, HERE I CAN TELL YOUR UNIVERSAL CONNECTION BY SIMPLY TELLING YOUR NAME AND YOUR PARTNER'S, FRIENDS'S OR ANY OTHERS' NAME")
print("I'LL FIND YOUR UNIVERSAL RELATIONSHIP WITH THEM\n")


name1 = input("Please Enter Your Name: ")
print('\n')
fname1 = name1.lower().replace(' ', '')
namelist1 = [letter for letter in fname1]  # getting the name and passing the string into a list

name2 = input("Please Enter Another Name: ")
print('\n')
fname2 = name2.lower().replace(' ', '')
namelist2 = [letter for letter in fname2]  # getting another name and passing the string into a list


def ASCIIword(word):  # for getting the ASCII values of the strings and returning the sum (to prevent using same name)
    sum = 0
    for m in word:
        ASCIIvalue = ord(m)
        sum = sum + ASCIIvalue
    return sum


word1 = ASCIIword(fname1)   # calling those functions
word2 = ASCIIword(fname2)


if word1 != word2:  # if those ASCII values are not equal then this will execute
    for i in namelist1[0:]:
        if i in namelist2:  # removing the same characters in both the lists
            namelist1.remove(i)
            namelist2.remove(i)
        else:
            continue

    num_of_letters1 = len(namelist1)    # measuring the length
    num_of_letters2 = len(namelist2)

    total_num_of_letters = num_of_letters1 + num_of_letters2    # adding those lengths to get the total number of words left
    flames = ['F', 'L', 'A', 'M', 'E', 'S']

    for i in flames:
        num = (total_num_of_letters % len(flames)) - 1  # this condition will choose the word to be removed from FLAMES, as it is possible for the num to go out of index I put mod
        if num >= 0:
            popped = flames.pop(num)    # removes a letter from FLAMES
            flames = flames[num:] + flames[0:num]   # rearranging the values, cuz after removing the word, we'll start from the letter next to the striked letter
        elif num < 0:   # in some cases the index will go -1 so I put this statement to ensure that it'll still work
            popped = flames.pop(num)
            flames = flames[num + 1:] + flames[0:num + 1]

    if flames[0] == 'F':    # assigning description for each letter for making a good user experience
        print(name1[0].upper() + name1[1:] + ' and ' + name2[0].upper() + name2[1:] + " You Got F")   # name1[0].upper() + name1[1:] will make the first letter of the string to upper and others lower
    elif flames[0] == 'L':
        print(name1[0].upper() + name1[1:] + ' and ' + name2[0].upper() + name2[1:] + " You Got An L")
    elif flames[0] == 'A':
        print(name1[0].upper() + name1[1:] + ' and ' + name2[0].upper() + name2[1:] + " You Got An A")
    elif flames[0] == 'M':
        print(name1[0].upper() + name1[1:] + ' and ' + name2[0].upper() + name2[1:] + " You Got An M")
    elif flames[0] == 'E':
        print(name1[0].upper() + name1[1:] + ' and ' + name2[0].upper() + name2[1:] + " You Got An E")
    else:
        print('For ' + name1[0].upper() + name1[1:] + ',' + name2[0].upper() + name2[1:] + " You Got An S")

    # everybody have their FLAMES abbreviation different so I just left it 'F' 'L' 'A' 'M' 'E' 'S'.

else:   # if the both ASCII values are same then it'll execute this
    print('YOU EITHER ENTERED THE SAME NAME TWICE OR THE NAMES WITH SAME EXACT LETTERS')
    print("IF YOU MEET THEM ANYWHERE, BELIEVE ME THAT'S YOUR ALTER EGO!!")
