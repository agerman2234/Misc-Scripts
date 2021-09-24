#! python3

password = 'spam'
i = True
while i == True:
    userpassword = input('What is the password?')
    if userpassword == password:
        print('Access Granted')
        i = False
    elif userpassword == '':
        print('Please enter a password')
    else:
        print('Wrong Password')
