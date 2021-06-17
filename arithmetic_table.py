#programa Tabuada em Python

def tabuada(x):
    for cont in range(1,11):
        print('{0}*{1}={2}'.format(x,cont, x*cont))

if __name__ == '__main__':
    num = int(input('digite um número:  '))
    tabuada(num)


