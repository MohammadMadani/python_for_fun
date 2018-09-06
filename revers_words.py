#reverse functions


s = input('enter string: ')
s_count = int(input('enter n for count:\n--> '))

def reverse_word(word):
    reverse = ''
    for i in word:
        reverse = i + reverse

    return reverse



def srting_counter(s):
    counter = s.count(s_count)

    return counter


def word_counter(s):
    for i in s.split():
        print('{:<7s} = {} char \t reverse = {}'.format(i,len(i),reverse_word(i)))
        

def counter_word(s,n):
    for i in s.split():
        if len(i) == n :
            print ('{} char is {}'.format(n,i))
            #continue


counter_word(s,s_count)
print('-----------------')
word_counter(s)
print('-----------------')
print(reverse_word(s))
print('-----------------')
