def askName(owner):
    name = input('What is your name?')

    if name == owner:
        print('Hello, ' + name)
    else:
        print(f'{name}, what are you doing on {owner}\'s computer?')

askName('Anthony')