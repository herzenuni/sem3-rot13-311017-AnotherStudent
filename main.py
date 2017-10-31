def rot13(s):
    """
    Функция преобразовавает строку по алгоритму rot13.

    Аргументы:
      s -- исходная строка

    Возвращаемое значение:
      преобразованная строка
    """

    def transform(ch):
        index = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(ch)
        if index != -1:
            return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[index]
        else:
            return ch

    return "".join(map(transform, s))
#--------------------------------
def loadLines(fileName):
    lines = list()
    try:
        f = open(str(fileName), 'rt')

        for line in f:
            lines.append(line)
        f.read()

    except OSError:
        print('Error load from file!')
        return None

    finally:
        f.close()

    return lines
#--------------------------------
def saveLines(fileName, lines):
    try:
        f = open(str(fileName), 'wt')

        for line in lines:
            f.write(line)

    except OSError:
        print('Error write to file!')
        return None

    finally:
        f.close()
#--------------------------------
lines = loadLines('in.txt')

if lines:
    res = list()
    for line in lines:
        res.append(rot13(line))

    print('coded:')
    for line in res:
        print(' ' * 4, line, end = '')

    saveLines('out.txt', res)