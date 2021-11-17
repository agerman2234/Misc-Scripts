#! python3

# \' single 
# \" double quote in line with string
# \t for tabs
# \n for a new line or line break
# \\ for a backslash

#Using the backslash escape character
print('Just ignore grammar on the following strings')
print('Use backslash to show single quote\'s')
print("Use backslash to show double quote\"s")
print('\tTo insert a tab character')
print('Use a \n to create a new line')
print('Use two \\ to show the backslash')

#Raw strings ignore escape character
print(r'In a statement that uses many \ its easy to use the raw string r')

#Triple quotes are used for large, multi line strings
print('''Here is the start of a long strin of gibberrish jfjdkljkdf
asjhf djlkhdsfljahsdfjlh asdfkjhjkasl
jsdahljkdhf djskhfdjshfjds jdhfdjhfjdah dsjfhajshf
kfaksdljfj jhfjasfhlj jahfjksdhlfjkash dkjhfjadshfjl''')

#METHODS

#use this to clean input from users
spam = 'this will all be upper case'
print(spam.upper())
eggs = 'THIS WILL ALL BE LOWER CASE'
print(eggs.lower())


#boolean check if is lower or upper
print(spam.isupper())
print(eggs.islower())

#Can identify is a speciifc locaation is upper or lower
name = 'Andrew'
print(name[0].isupper())

#isalpha() returns true if strin is only letters
#isalnum() true if string contains letters and numbers
#isdecimal() true if strin is only numbers
#isspace() true if there are only space characters
#istitle() true if string contains only words with first letter capital and the rest lower

#startswith() and endswith()
print('Hello World'.startswith('Hello'))
print('Goodbye World'.endswith('chair'))

#join() and split()
eggs = ['cats','rats','bats']
print(eggs)
print(','.join(eggs))
spam = 'Here is the string that will be split by default spaces'
print(spam)
print(spam.split())
bacon = 'This string will be split on the letter i'
print(bacon)
print(bacon.split('i'))

#center(), ljust() and rjust() to control output size
spam ="RJust 40 spaces with hashtag as default"
print(spam.rjust(40,'#'))
eggs = ' Center this with dash '
print(eggs.center(40,'-'))

#strip(), lstrip(), rstrip()
eggs = '      Hello'
print(eggs.strip())
spam = '####Hello######'
print(spam.lstrip('#'))

#replace()
spam = 'Hello World'
print(spam.replace('l','LLLLLLLL'))

#String formatting (also called string interpollation
name= 'Andrew'
place = 'Washington, D.C.'
time = '6:00PM'
food = 'cake'

print('Hello ' + name + ', you are invited to a party at ' + place +
      'when the time is ' + time + '. Please be sure to bring ' + food + '.')
#string formatting can simplify this
print('Hello %s, you are invited to a ' 
'party at %s when the time is %s.'
'Please be sure to bring %s.' % (name, place, time, food))























