def askName(owner):
    name = input('What is your name?')
    if name == owner:
        return 'Hello, ' + name
    else:
        return f'{name}, what are you doing on {owner}\'s computer?'


if __name__ == '__main__':
    # print(askName('Anthony'))
    pass
