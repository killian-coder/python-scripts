userName = input("hallo welcome to the fun world! \n\nUsername: ") #asking the user for password
password = input("Password: ")

count = 0
count += 1
while  userName == userName and password == password:
    if count ==3:
        print('\nthree username and password attempts have been used. bye')
        break
    elif userName == 'killian' and password =='blue':
        print('you have logged in ')
        break
    elif userName != 'killian' and password != 'blue':
        print("Your username and password is wrong")
        userName = input("\n\nUsername: ")
        password = input("Password ")
        count += 1
        continue
    elif userName == 'killian' and password != 'blue':
        print("Your password is wrong")
        userName = input("\n\nUsername: ")
        password = input("Password: ")
        count += 1
        continue
        continue
    elif userName != 'killian' and password == 'blue':
        print("Your username is wrong")
        userName = input("\n\nUsername: ")
        password = input("Password: ")
        count += 1
        continue
