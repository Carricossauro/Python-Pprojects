#!/usr/bin/env python3

import random
import linecache

ind = random.randint(0, 267750)

line = linecache.getline('sowpods.txt', ind)
line = line[:-1]
letters = list(line)
corrects = []

dic = {'won': False, 'tries': 0}
leng = len(set(letters))

for i in letters:
    print("_ ", end='')

playing = True
while playing:
    playing = False
    let = (input("\nLetter: ")).upper()
    dic['tries'] = dic['tries'] + 1
    if let == line:
        print("You guessed the word!")
        break
    for i in letters:
        if let == i:
            corrects.append(let)
        if i in corrects:
            print(i + " ", end='')
        else:
            print("_ ", end='')
            playing = True
    print()


if dic['tries'] < leng:
    print("You did really good! Only " + str(dic['tries']) + " tries with " + str(leng) + " letters!")
elif dic['tries'] > leng + (leng / 2):
    print("You did OK. " + str(dic['tries']) + " tries with " + str(leng) + " letters.")
elif dic['tries'] == leng:
    print("You did great! " + str(dic['tries']) + " tries with " + str(leng) + " letters.")
else:
    print("You can do better! Took you " + str(dic['tries']) + " tries with " + str(leng) + " letters.")
