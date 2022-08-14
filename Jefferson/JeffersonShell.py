import random
import string

text = [""]
key = []
n = []
file = open("MP-1ARI.txt", "w")
cylinder = {1: 'ZWAXJGDLUBVIQHKYPNTCRMOSFE', 2: 'KPBELNACZDTRXMJQOYHGVSFUWI', 3: 'BDMAIZVRNSJUWFHTEQGYXPLOCK',
            4: 'RPLNDVHGFCUKTEBSXQYIZMJWAO', 5: 'IHFRLABEUOTSGJVDKCPMNZQWXY', 6: 'AMKGHIWPNYCJBFZDRUSLOQXVET',
            7: 'GWTHSPYBXIZULVKMRAFDCEONJQ', 8: 'NOZUTWDCVRJLXKISEFAPMYGHBQ', 9: 'XPLTDSRFHENYVUBMCQWAOIKZGJ',
            10: 'UDNAJFBOWTGVRSCZQKELMXYIHP'}
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def covertLetters(text):
    text.remove(' ', '!', '?', '.', ',', ';', ':', 'é', 'è', 'ê', 'à', 'ù',)
    text.upper()
    return text


def mix():
    random.choice(string.ascii_uppercase)


def createCylinder(file, n):
    n > 0
    while n > 0:
        file.write(mix())
        n -= 1
        return True


def loadCylinder(file):
    return cylinder


def keyOK(key, n):
    key = []
    n > 0
    if 1 <= key <= n:
        return True


def createKey(n):
    n >= 0
    if n >= 0:
        return key == [random.randint(1, n) for i in range(10)]


def find(letter, alphabet):
    for i, letter2 in enumerate(alphabet):
        if letter == letter2:
            return i


def shift(i):
        return (i + 6) % 26


def cipherLetter(letter, alphabet):
    position = find(letter, alphabet)
    position2 = shift(position)
    return alphabet[position2]


def cipherText(cylinder, key, text):
    if keyOK(key, n):
        text2 = [""]
        text2 = covertLetters(text)
        for i, letter in enumerate(text):
            cylinder(key)


print(key)
procedure = file.write
cipherText(procedure, key, text)
print(cipherText)
print(procedure)
