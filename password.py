passwordfile = open('secretPasswordfile.txt')
secretPassword = passwordfile.read()
print('enter your password.')
typedpassword = input()
if typedpassword == secretPassword:
    print('access granted')
    if typedPassword == '12345':
        print('that password is that an idiot puts on their luggage')
    else:
        print('acess denied')
        
