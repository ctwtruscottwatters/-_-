# -*- coding: utf-8 -*-
"""
Charles Truscott, I love MIT
Problem Set one, exercise 3/3
Week 1 - 2
runfile('C:/Users/Charles_Truscott/.spyder-py3/temp.py', wdir='C:/Users/Charles_Truscott/.spyder-py3')
Longest substring in alphabetical order is: pqrstuv

"""
s = 'xyzcharlesabcstevemnoharrowpqrstuvjamespqstuvwxyz'

num_posn = []
counter = 0
for n in range(0, len(s) - 1):
    if s[counter] < s[counter + 1]:
        consecutive_found = True    
        num_posn += [counter]
    counter += 1
#print(num_posn)
len_found = 0
max_found = 0
num_found = 0
string = ""
list_of_strings = []
for n in num_posn:
    i = 1
    j = 2
    string += s[n]
    s += "\x00\x00"
    while (j <= len(s) - n - 2):
       # print("{} {} {}".format(n, i, j))
        #print(s[n], s[n + i], s[n + j])
        if s[n + i] <= s[n + j]:
            string += s[n + i]
            num_found += 1
            #print("Match {} letters".format(num_found))
            if s[n + j] > s[n + j + 1]:
                string += s[n + j]
            i += 1
            j += 1

        else:
            break
        if num_found > max_found:
            max_found = num_found
            #print("Max found: {}".format(max_found))
    num_found = 0
    list_of_strings.append(string)
    string = ""
print("Longest substring in alphabetical order is: {}".format(max(list_of_strings, key=len)))
