#hadse kalame

#make a new list of words
#select randome them

import random
import os

my_list = [
    'mammad',
    'xabat',
    'nasrin',
    'manij',
    'dlnia'
]


def clear():
    os.system('clear')


def srting_counter(s):
    counter = choice.count(i)
    return counter

clear()
choice = random.choice(my_list)
my_gussess = []
bad_gussess = []
good_gussess = []

def main_game():
    while True :

        random_word = input('\ngussess a words: ')
        if len(list(random_word)) == 1:
            my_gussess.append(random_word)        
        else:
            print('ERROR: ENTER JUST ONE CHARACHTER')
            main_game()
        
        clear()

        if random_word in choice:
            if random_word not in good_gussess:
                good_gussess.append(random_word) 
        else:
            if random_word not in bad_gussess:
                bad_gussess.append(random_word)

        print('good gussess: {}\n'.format(good_gussess))
        print('bad gussess: {}\n'.format(bad_gussess))
        print('secret word is [{}/{}]: '.format(len(bad_gussess),3),end=' ')


        for i in choice:
            if i in my_gussess:
                print(i,end='')
            else:
                print('-',end='')
        print('')


        if len(good_gussess) == len(set(choice)):
            print('\n***** YOU WIN *****')
            break

        elif len(bad_gussess) > 3 :
            print('\nGAME OVER')
            print('\nsecret word is: {} \n'.format(choice))
            break

main_game()

