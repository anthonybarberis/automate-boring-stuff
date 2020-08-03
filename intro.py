def askName(owner):
    name = input('What is your name?')
    if name == owner:
        return 'Hello, ' + name
    else:
        return f'{name}, what are you doing on {owner}\'s computer?'


def guessNumber():
    import random
    randNum = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20')
    guess = None
    guesses = 0
    while guess != randNum:
        guess = int(input('Guess my numnber: '))
        guesses += 1
        if guess < randNum:
            print('Too low')
        elif guess > randNum:
            print('Too high')
        elif guess == randNum:
            print(f'You got it in {guesses} guesses!')


def collatz():
    number = None
    while type(number) != int:
        try:
            number = int(input('Choose any integer: '))
        except:
            print('That ain\'t no number')
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        elif number % 2 != 0:
            number = number * 3 + 1
        print(number)


def printGroceryList():
    groceries = ['apples', 'bananas', 'corn dogs', 'cheese', 'coffee']
    groceryList = ''
    for each in groceries[:-1]:
        groceryList = groceryList + f'{each}, '
    groceryList = groceryList + f'and {groceries[-1]}'
    print(groceryList)


if __name__ == '__main__':
    # print(askName('Anthony'))
    # guessNumber()
    # collatz()
    #printGroceryList()
    pass
