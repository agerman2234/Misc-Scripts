#! python3

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error you tried to divide by zero")


print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(4))

numCats = input('How many cats do you have?')
while True:
    try:
        numCats = int(numCats)
        if numCats > 4:
            print('Woah, that\'s a lot of cats!')
            break
        elif numCats < 0:
            print('Did you kill those cats?')
            break
        elif numCats == 0:
            print ('That\'s the perfect number of cats')
            break
        else:
            print('That\'s not too many cats')
            break
    except ValueError:
        print('Please enter response numerically.')
        numCats = input('How many cats do you have?')