#simple telephone list

import os

my_list = {'mammad':'0914 713',
            'babm':'0914 948 ',
            'xabat':'0914 942'
            }
            
clear = os.system('clear')

def add_list():
    while True:
        print('\n[0]: back to menu')
        print('[00]: show list\n')

        name = input('please enter name:\n[add]--> ')
        for i in my_list.keys():
            if i == name :
                print('your input name "{}" in list.\n are youe sure to edit? [y/n] '.format(name))
                try:
                    ans = input('\n-->')
                    if ans=='y':
                        continue
                    elif ans=='n':
                        add_list()
                except:
                    print('valid characters')    
                    break
        if name == '0':
            menu()
            continue
        elif name == '00':
            show_list()
            continue
        number = input('please enter his/her number\n[add]--> ')
        if number == '0':
            menu()
        elif number == '00':
            show_list()
            
        my_list[name] = number
        os.system('clear')
        print('name: "{}" , number: "{}" added successfully!'.format(name,number))

def show_list():
    os.system('clear')
    print('{:^15s} |{:^15s}'.format('name','phone'))
    for i in my_list.items():
        print('|---------------|---------------|\n',end='')
        for j in i:
            print('|',end='')
            print('{:^15}'.format(j),end='')
        print('|')


def edit_list():
    os.system('clear')
    print('[1]: edit')
    print('[2]: delete')
    print('[3]: back to menu')
    print('--------------')
    javab = input('[edit]--> ')
    while True:
        if javab == '1':
            #os.system('clear')
            print('[1]: show list')
            print('[2]: edit')
            print('[3]: back')

            javab1 = input('--> ')

            try:
                if javab1 == '1' :
                    show_list()
                    print()
                    continue
                
                elif javab1 == '2':
                    edit1_list()
                
                elif javab1 == '3':
                    edit_list()
            except :
                os.system('clear')
                print('\nenter valid key\n')
                continue

        elif javab == '2':
            os.system('clear')
            delete_list()

        elif javab == '3':
            menu()


def delete_list():
    try:
        print('\n[0]: back')
        print('[00]: show list\n--------------------')

        name = input('\nenter name for delete:\n[delete]--> ')
        
        if name=='0':
                os.system('clear')
                edit_list()

        elif name=='00':
                show_list()
                delete_list() 

        elif name not in my_list:
            os.system('clear')
            print('"{}" not exist'.format(name)) 
            delete_list()

        else:
            os.system('clear')
            del my_list[name]
            print('"{}" deleted from list'.format(name))
            delete_list()

    except ValueError:
        print('please enter valid charactes\n')
    
    except KeyError:
        print('please enter name of list')


def edit1_list():
    os.system('clear')
    name = input('please enter name of list:\n--> ')
    for i in my_list.keys():
        if i == name :
            print('"{}" : "{}" '.format(name,my_list.get(name)))
            ans = input('\nare you edit? [y/n)\n--> ').lower()
            if ans == 'y':
                number = input('please enter his/her number\n-->')
                my_list[name] = number
                print('\nname: "{}" , number: "{}" edited successfully\n'.format(name,number))
                os.system('sleep 3')
                for i in range(6):
                    print('back to menu wait... {}/6 secand'.format(i))
                    os.system('sleep 1')
                    os.system('clear')
                    
                    

                edit_list()
            else:
                edit_list()
    else:
        show_list()
        print('\n"{}" not found!!!\n'.format(name))



def search():
    print('\ninput name:')
    name = input('--> ')
    for i in my_list.keys():
        if i == name :
            print('number of your name is "{}" '.format(my_list.get(name)))
            break
    else:
        print('"{}" not found!!!'.format(name))


def menu():
    os.system('clear')
    while True:
        print('[1]: show list')
        print('[2]: add phone number')
        print('[3]: edit/delete number')
        print('[4]: search')
        print('----------------------------')

        try:
            javab = input('--> ')

            if javab == '1':
                os.system('clear')
                show_list()
                print()
            elif javab == '2':
                os.system('clear')
                add_list()
                print()
            elif javab == '3':
                os.system('clear')
                edit_list()    
                print()
            elif javab == '4':
                search()
                print()
        except ValueError:
            os.system('clear')
            print('please input valid keys') 
menu()
