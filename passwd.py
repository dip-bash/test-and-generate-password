
import random
import subprocess


def passwd_create():
    upper = 'ABCDEFGHIJKLMNOPQRST'
    lower = upper.lower()
    digits = '1234567890'
    special = '~!@#$%^&*()_+=-`[]\}{|;"",./?><'

    try:
        length = int(input("length: "))
    except:
        subprocess.run('clear')     
        print('enter int value')
        passwd_create()
    else:  
        print('password: ',end='')
        for i in range(length):
            up = random.choice(upper)
            lo = random.choice(lower)
            di = random.choice(digits)
            sp = random.choice(special)
            char = [up,lo,di,sp]
            print(random.choice(char), end='')

        print('')

def passwd_chk():
    passwd = input('input your password: ')
    subprocess.run('clear')

# add 1 for fond upper, lower or digit in passwd
    length = len(passwd)
    upper = sum(1 for char in passwd if char.isupper())
    lower = sum(1 for char in passwd if char.islower())
    digit = sum(1 for char in passwd if char.isdigit())
    special = int(length) -( int(upper) + int(lower) + int(digit))

    number = 0

    def result(x):
        match x:
            case 1:
                print('Your password is very week')
                
            case 2:
                print('Your password is crackable')
                
            case 3:
                print('Your password is below average')
                
            case 4:
                print('Your password is good')
                
            case 5:
                print('Your password is quite good')
                
            case 6:
                print('Your password is strorng')
                
            case 7:
                print('Your password is very storng')
                
            case 8:
                print('Your password is very strong and satisfy all security lavel')

    if length > 6:
        number+=1
        if length > 8:
            number+=1
        if length > 12:
            number+=1
        if length > 18:
            number+=1
        if int(upper) > 1:
            number+=1
        if int(lower) > 1:
            number+=1
        if int(digit) > 1:
            number+=1
        if special > 1:
            number+=1
        result(number)
    else:
        print('password is too short')

    if int(upper) < 1 or int(lower) < 1 or int(digit) < 1 or special < 1:
        print('\nto improve your password: ')   
    if int(upper) < 1:
        print('> add some upper case <')
    if int(lower) < 1:
        print('>add some lower case <')
    if int(digit) < 1:
        print('> add some digits <')
    if special < 1:
        print('> add some special chracters <')


while True:
    choice = input('''type 1 for passwd checking\ntype 2 for create password\n>> ''')
    if choice == '1':
        passwd_chk()
    elif choice == '2':
        passwd_create()
    else:
        subprocess.run('clear')
        print('invalid input')
        y_or_n = input('Do you want to exit? y/n:\n>> ')
        print(y_or_n)
        subprocess.run('clear')
        if y_or_n == 'y':
            exit()
        else:
            pass

    