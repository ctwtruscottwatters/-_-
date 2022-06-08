# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:46:14 2022
Polynomial cipher using Primes
I love MIT

Authored by Charles Truscott Watters

runfile('C:/Users/Charles_Truscott/Desktop/linearpolycipher.py', wdir='C:/Users/Charles_Truscott/Desktop')
Plain text: 
Charles Thomas Wallace Truscott. Mark William Watters. Tai William Wedekind Truscott
Cipher text: 
The primes used to encrypt the cipher are: [19551993, 19551995, 19551997, 19551999, 19552001, 19552003, 19552005, 19552007]
382287820925841
383011733476636
382281016832013
421392295958676
387585335717340
382356722150653
433375771179153
382280958176028
448132070952028
383011733476636
398184060597153
390141856579581
382281016832013
433375771179153
382280958176028
513833630437921
382281016832013
387585335717340
387585335717340
382281016832013
382287820925841
382356722150653
382280958176028
448132070952028
421392295958676
466116834923133
433375771179153
382287820925841
398184060597153
448132070952028
448132070952028
382280958176028
382280958176028
390141856579581
382281016832013
421392295958676
385742110667473
382280958176028
513833630437921
383578017855693
387585335717340
387585335717340
383578017855693
382281016832013
390141856579581
382280958176028
513833630437921
382281016832013
448132070952028
448132070952028
382356722150653
421392295958676
433375771179153
382280958176028
382280958176028
448132070952028
382281016832013
383578017855693
382280958176028
513833630437921
383578017855693
387585335717340
387585335717340
383578017855693
382281016832013
390141856579581
382280958176028
513833630437921
382356722150653
382307236055388
382356722150653
385742110667473
383578017855693
393601249378948
382307236055388
382280958176028
448132070952028
421392295958676
466116834923133
433375771179153
382287820925841
398184060597153
448132070952028
448132070952028

Working on decryption but need to lower the order of the polynomial ... 
The primes used to encrypt the cipher are: [19551993, 19551995, 19551997, 19551999, 19552001, 19552003, 19552005, 19552007]
3822878209258411
3830117334766366
3822810168320133
4213922959586766
3875853357173400
3823567221506533
4333757711791533
3822809581760288
4481320709520288
3830117334766366
3981840605971533
3901418565795811
3822810168320133
4333757711791533
3822809581760288
5138336304379211
3822810168320133
3875853357173400
3875853357173400
3822810168320133
3822878209258411
3823567221506533
3822809581760288
4481320709520288
4213922959586766
4661168349231333
4333757711791533
3822878209258411
3981840605971533
4481320709520288
4481320709520288
3822809581760288
3822809581760288
3901418565795811
3822810168320133
4213922959586766
3857421106674733
3822809581760288
5138336304379211
3835780178556933
3875853357173400
3875853357173400
3835780178556933
3822810168320133
3901418565795811
3822809581760288
5138336304379211
3822810168320133
4481320709520288
4481320709520288
3823567221506533
4213922959586766
4333757711791533
3822809581760288
3822809581760288
4481320709520288
3822810168320133
3835780178556933
3822809581760288
5138336304379211
3835780178556933
3875853357173400
3875853357173400
3835780178556933
3822810168320133
3901418565795811
3822809581760288
5138336304379211
3823567221506533
3823072360553888
3823567221506533
3857421106674733
3835780178556933
3936012493789488
3823072360553888
3822809581760288
4481320709520288
4213922959586766
4661168349231333
4333757711791533
3822878209258411
3981840605971533
4481320709520288
4481320709520288
[3822878150600033.5, 3830117276107988.5, 3822810109661755.5, 4213922900928388.5, 3875853298515022.5, 3823567162848155.5, 4333757653133155.5, 3822809523101910.5, 4481320650861910.5, 3830117276107988.5, 3981840547313155.5, 3901418507137433.5, 3822810109661755.5, 4333757653133155.5, 3822809523101910.5, 5138336245720833.0, 3822810109661755.5, 3875853298515022.5, 3875853298515022.5, 3822810109661755.5, 3822878150600033.5, 3823567162848155.5, 3822809523101910.5, 4481320650861910.5, 4213922900928388.5, 4661168290572955.0, 4333757653133155.5, 3822878150600033.5, 3981840547313155.5, 4481320650861910.5, 4481320650861910.5, 3822809523101910.5, 3822809523101910.5, 3901418507137433.5, 3822810109661755.5, 4213922900928388.5, 3857421048016355.5, 3822809523101910.5, 5138336245720833.0, 3835780119898555.5, 3875853298515022.5, 3875853298515022.5, 3835780119898555.5, 3822810109661755.5, 3901418507137433.5, 3822809523101910.5, 5138336245720833.0, 3822810109661755.5, 4481320650861910.5, 4481320650861910.5, 3823567162848155.5, 4213922900928388.5, 4333757653133155.5, 3822809523101910.5, 3822809523101910.5, 4481320650861910.5, 3822810109661755.5, 3835780119898555.5, 3822809523101910.5, 5138336245720833.0, 3835780119898555.5, 3875853298515022.5, 3875853298515022.5, 3835780119898555.5, 3822810109661755.5, 3901418507137433.5, 3822809523101910.5, 5138336245720833.0, 3823567162848155.5, 3823072301895510.5, 3823567162848155.5, 3857421048016355.5, 3835780119898555.5, 3936012435131110.5, 3823072301895510.5, 3822809523101910.5, 4481320650861910.5, 4213922900928388.5, 4661168290572955.0, 4333757653133155.5, 3822878150600033.5, 3981840547313155.5, 4481320650861910.5, 4481320650861910.5]



"""

import numpy as np
import sys


def find_root(number, root):
    high = number
    low = 0
    guess = (high + low) / 2.0
    epsilon = 0.0000001
    while (guess ** root != number):
        #print("guess: {} high: {} low: {}".format(guess, high, low))
        if guess ** root > number:
            high = guess
        elif guess ** root < number:
            low = guess
        guess = ((high + low) / 2.0)
        if (guess ** root <= number - 0.00001):
            break
    return guess
def is_prime(numbers):
    if numbers == 1:
        return True
    for x in range(2, numbers, 1):
        if numbers % x == 0:
            return False
        else:
            return True
def find_primes(start, end):
    if end - start < -8:
        print("Cannot continue ...")
        sys.exit(1)
    nums = []
    primes = []
    for n in range(start, end, 1):
        nums.append(n)
    for n in nums:
        if is_prime(n): primes.append(n)
  
    return primes
def encrypt(string):
    ciphertext = ""
    list_of_primes = find_primes(19551993, 19552009)
    print("The primes used to encrypt the cipher are: {}".format(list_of_primes))
    a = list_of_primes[0]
    b = list_of_primes[1]
    c = list_of_primes[2]
    d = list_of_primes[3]
    e = list_of_primes[4]
    f = list_of_primes[5]
    g = list_of_primes[6]

    
    for n in range(0, len(string), 1):
        numrep = 0
        if string[n] == "A" or string[n] == "a":
            numrep = 1
        elif string[n] == "B" or string[n] == "b":
            numrep = 2
        elif string[n] == "C" or string[n] == "c":
            numrep = 3
        elif string[n] == "D" or string[n] == "d":
            numrep = 4
        elif string[n] == "E" or string[n] == "e":
            numrep = 5
        elif string[n] == "F" or string[n] == "f":
            numrep = 6
        elif string[n] == "G" or string[n] == "g":
            numrep = 7
        elif string[n] == "H" or string[n] == "h":
            numrep = 8
        elif string[n] == "I" or string[n] == "i":
            numrep = 9
        elif string[n] == "J" or string[n] == "j":
            numrep = 10
        elif string[n] == "K" or string[n] == "k":
            numrep = 11
        elif string[n] == "L" or string[n] == "l":
            numrep = 12
        elif string[n] == "M" or string[n] == "m":
            numrep = 13
        elif string[n] == "N" or string[n] == "n":
            numrep = 14
        elif string[n] == "O" or string[n] == "o":
            numrep = 15
        elif string[n] == "P" or string[n] == "p":
            numrep = 16
        elif string[n] == "Q" or string[n] == "q":
            numrep = 17
        elif string[n] == "R" or string[n] == "r":
            numrep = 18
        elif string[n] == "S" or string[n] == "s":
            numrep = 19
        elif string[n] == "T" or string[n] == "t":
            numrep = 20
        elif string[n] == "U" or string[n] == "u":
            numrep = 21
        elif string[n] == "V" or string[n] == "v":
            numrep = 22
        elif string[n] == "W" or string[n] == "w":
            numrep = 23
        elif string[n] == "X" or string[n] == "x":
            numrep = 24
        elif string[n] == "Y" or string[n] == "y":
            numrep = 25
        elif string[n] == "Z" or string[n] == "z":
            numrep = 26
        ciphertext += str(a * numrep ** 5 + b * numrep ** 4 + c * numrep ** 3 + d + e + f + g ** 2)
        ciphertext += "\n"

    return ciphertext

def decrypt(string, a, b, c, d, e, f, g):
    letters_to_decrypt = []
    decrypted_letters = []
    tempstr = ""
    for x in range(len(string) - 1):
        tempstr += string[x] 
        if string[x + 1] == "\n":
            tempstr += string[x]
            letters_to_decrypt.append(tempstr)
            tempstr = ""
        if string[x] == "\n":
            continue
    for n in letters_to_decrypt:
        print(int(n))
        decrypted_letters.append(int(n) - find_root(g, 2) - f - e - d - int(find_root(int(n), 3)) / c - find_root(int(n), 4) / b - find_root(int(n), 5) / a)
#            print(temp_decryption_phrase)
    print(decrypted_letters)
def main():
    print("Plain text: ")
    print("Charles Thomas Wallace Truscott. Mark William Watters. Tai William Wedekind Truscott")
    print("Cipher text: ")
    print(encrypt("Charles Thomas Wallace Truscott. Mark William Watters. Tai William Wedekind Truscott"))
    print("Working on decryption but need to lower the order of the polynomial ... ")
    decrypt(encrypt("Charles Thomas Wallace Truscott. Mark William Watters. Tai William Wedekind Truscott"), 19552005, 19552003, 19552001, 19551999, 19551997, 19551995, 19551993)
if __name__ == "__main__": main()
