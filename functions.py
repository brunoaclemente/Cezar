from time import sleep

def access(file, name=''):
    try:
        a = open(file, 'at')
    except FileNotFoundError or FileExistsError:
        print('There was an ERROR opening the file!')
    else:
        try:
            c = checker(file, name)
            if not c:
                a.write(f'{name}\n')
        except FileNotFoundError or FileExistsError:
            print('There was an ERROR writing the data!')
        else:
            a.close()
    sleep(1)


def checker(name, word):
    a = 0
    try:
        a = open(name, 'rt', encoding='utf-8')
    except FileNotFoundError or FileExistsError:
        print('Error reading file')
    else:
        tf = False
        if len(word) != 1:
            wor = f'{word.lower()}\n'
            for lines in a:
                lines.lower()
                if lines == wor:
                    tf = True
        return tf
    finally:
        a.close()


def color(msg, c='red'):
    s = '\033[31m{}\033[m'.format(msg)
    if c == 'green':
        s = '\033[32m{}\033[m'.format(msg)
    elif c == 'yellow':
        s = '\033[33m{}\033[m'.format(msg)
    elif c == 'blue':
        s = '\033[34m{}\033[m'.format(msg)
    elif c == 'pink':
        s = '\033[35m{}\033[m'.format(msg)
    elif c == 'light blue':
        s = '\033[36m{}\033[m'.format(msg)
    elif c == 'grey':
        s = '\033[37m{}\033[m'.format(msg)
    return s


def frequency(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    alphanumeric = []
    for letter in alphabet:
        n = text.count(letter)
        alphanumeric.append(n)
    order = []
    for num, let in enumerate(alphabet):
        order.append([alphanumeric[num], let])
    order.sort(reverse=True)
    return order


def header(txt, tam=35, ce=35):
    print(line(tam))
    print(txt.center(ce))
    print(line(tam))


def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: please enter a valid integer.\033[m')
            readInt(msg)
        else:
            return n


def readStr(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: please enter a valid text1.\033[m')
            return 0
        else:
            return n


def line(siz=35):
    return "-" * siz


def menu(roster):
    header('main panel')
    c = 1
    for item in roster:
        print(f'{color(c, "green")} - {color(item, "blue")}')
        c += 1
    print(line())
    opc = readInt(f'{color("Your Option:", "green")} ')
    return opc
