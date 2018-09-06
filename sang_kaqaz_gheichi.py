#in yek bazi minimal sang kaqaz, ghechi ast

import os
import random

my_list = ['sang','kaqaz','gheichi']


def menu():
    os.system('cls' if os.name=='nt' else 'clear') 
    print('|---------------------------------------------------------------------|')
    print('|                   welcome to my game!                               |')
    print('|                                                                     |')
    print('|                   SANG , KAQAZ , GHEICHI                            |')
    print('|                                                                     |')
    print('|     for play game you shuold exam your chance in 6 repeat           |')
    print('|---------------------------------------------------------------------|')

    print('[1]: start')
    print('[2]: exit')

    while True:
        try :
            ans = int(input('\n->> '))
            if ans == 1:
                main_game()
            elif ans == 2:
                exit
        except ValueError:
            print('ERROR: enter 1 or 2')    
            continue
            


def check_game(name):
    
    my_random = random.choice(my_list)

    #we can so use this command random.choice(my_list)
    
    if name == 'sang' and my_random == 'gheichi' : 
        return 1,my_random
    
    elif name == 'gheichi' and my_random == 'kaqaz':
        return 1,my_random
        
    elif name == 'kaqaz' and my_random == 'sang' :
        return 1,my_random

    elif name == my_random:
        return 0,my_random

    else:
        return 2,my_random

def start_game():

    you = 0
    computer = 0
    i = 0
    your_input = ''
    computer_input = ''
    list_computer = []
    list_you = []
    error = ''

    while i <= 6:

        os.system('cls' if os.name=='nt' else 'clear') 
        print('[1] sang')
        print('[2] kaqaz')
        print('[3] gheichi')
        print("\nnote: input words not numbers")
        print('------------------')
        print('\nyou      : ({}) {:^10s}  {}'.format(you,your_input,list_you))
        print('\ncomputer : ({}) {:^10s}  {}\n'.format(computer,computer_input,list_computer))
    
        print('------------------')

        try :
            if i == 6:
                break
            your_input = input('[{}/6 {}] >>  '.format(i,error))

            if your_input == 'sang' or your_input == 'kaqaz' or your_input == 'gheichi':
                
                error = ''
                x , computer_input = check_game(your_input)
                #x, computer_input is return from check_game
                
                if x == 1:
                    you = you + 1
                    list_you.append(1)
                    list_computer.append(0)
                elif x == 0:
                    continue

                else :
                    computer = computer + 1
                    list_you.append(0)
                    list_computer.append(1)
            else:
                error = 'error: input just words of list'
                continue
        except KeyboardInterrupt:
            print('\nyou breaked game\nGOOD BYE')
            exit()

        i += 1   
    return you,computer

def main_game():
    you , computer = start_game()

    if you > computer :
        print('you {} : {} computer'.format(you,computer))
        print('\n*********** you win ***********\n')
        exit()
    elif you == computer:
        print('you {} : {} computer'.format(you,computer))
        print('\n*********** you equal ***********\n')
        exit()
    else:
        print('you {} : {} computer'.format(you,computer))
        print('\nGAME OVER\n')
        exit()
    
#start_game()
menu()


