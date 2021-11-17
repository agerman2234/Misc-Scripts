
import re

message = 'This is my mobile number 484-538-0863 and this is my office number 123-456-7890'

#Create regex format. Using raw string because regex uses many backslashes
phoneNumberRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#Match Object and searching for first occurence
mo = phoneNumberRegEx.search(message)
print(mo.group())

#Finding all occurences 
mo = phoneNumberRegEx.findall(message)
print(str(mo[0]))
print(str(mo[1]))

#Use parentheses to mark 'groups' within a RegEx
message = 'This is my mobile number (484)-538-0863'
phoneNumberRegEx = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
mo = phoneNumberRegEx.search(message)
print(mo.group())

#Find a string of text finds variations of a string
#batMessage = "Quick Robin, get to the Batcopter, said Batman"
batMessage = "Batmobile"
batRegEx = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegEx.search(batMessage)
print(mo.group())

#Repetition with Greedy/Non-Greedy Matching
batRegEx = re.compile(r'Bat(wo)?man')
message = "The Adventures of Batwoman"
mo = batRegEx.search(message)
print(mo.group())

#phone number with or without area ccode included, question mark means it can appear
#0-1 times, using a * means it can appear 0-many times
phoneRegEx = re.compile (r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegEx.search('My number is 484-538-0863')
mo2 = phoneRegEx.search('My number is 538-0863')
print(mo1.group())
print(mo2.group())

#Using the + means a group must appear once and can appear more, use {x}
#to find an exact match to the number of times a pattern is found. 
#i.e. {3} to find exactly 3 matched in the compile function
# {0,5} zero to five matches
# {3,18} three to eighteen matches
# {8,} eight or more matches

batRegEx = re.compile(r'Bat(wo)+man')
message = "The Adventures of Batwoman"
mo = batRegEx.search(message)
print(mo.group())

message = "The Adventures of Batwowowowowowoman"
mo = batRegEx.search(message)
print(mo.group())

#Greedy matching matches the longest possible string. Default is greedy
digitRegEx = re.compile(r'(\d){3,5}')
mo = digitRegEx.search('123456789')
print('Greedy:  ' + str(mo.group()))
#Non-Greedy matching matches the least possible string with the question mark
digitRegEx = re.compile(r'(\d){3,5}?')
mo = digitRegEx.search('123456789')
print('Greedy:  ' + str(mo.group()))

#Findall method: finds all matches, not just the first
#this returns a list of string values
#if RegEx has zero or one groupt the findall method returns a list of strings
#if RegEx has two or more groups findall method returns a list of tuples of strings
phoneRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
numbers = 'Number 1 is 484-538-0863 number 2 is 212-345-6789 and number 3 is'
'456-123-7890'
#returns a list of tuples of stings
mo = phoneRegEx.findall(numbers)
print(mo)

#character classes:
#\d for digit (0-9)
#\D for any character which is NOT a digit
#\w any character that is a letter, digit, or the underscore character
#\W any character that is NOT a letter, digit, or the underscore character
#\s any space, tab, or newline character
#\s any character that is NOT a space, tab, or newline character

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partrideg in a pear tree'
xmasRegEx = re.compile(r'\d+\s\w+')
mo = xmasRegEx.findall(lyrics)
print(mo)

#create a custom character class with []
vowelRegEx = re.compile(r'[aeiouAEIOU]')
mo = vowelRegEx.findall(lyrics)
print(mo)
#negative character class matches everything that is NOT specified.
#now the code above looks for characters that are not vowels
vowelRegEx = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegEx.findall(lyrics)
print(mo)

#https://www.debuggex.com/cheatsheet/regex/python
#starting a character string with ^ means that the string must begin with that searched string
beginsWithHelloRegEx = re.compile(r'^Hello')
mo = beginsWithHelloRegEx.search('Hello there!')
print(mo.group())
mo = beginsWithHelloRegEx.search('Not hello there!')
print(mo)
# dollar sign at the end means the searched string must end with the regex
beginsWithHelloRegEx = re.compile(r'Hello$')
mo = beginsWithHelloRegEx.search('I said Hello')
print(mo.group())

#wildcard dot character . (period) means any character except newline
atRegEx = re.compile(r'.at')
mo = atRegEx.findall('The cat in the hat sat on the flat mat.')
print(mo)
atRegEx = re.compile(r'.{1,2}at')
mo = atRegEx.findall('The cat in the hat sat on the flat mat.')
print(mo)

#dot star method:get entire word with at but not white spaces
#   .* is the greedy match
#   .*? is the non greedy match
nameRegEx = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegEx.findall('First Name: Andrew Last Name: German')
print(mo)
nonGreedyRegEx = re.compile(r'<(.*?)>')
mo = nonGreedyRegEx.findall('<To serve humans> for dinner>')
print(mo)











