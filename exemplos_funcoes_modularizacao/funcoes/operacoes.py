def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b
def modulo(a, b):
    if b == 0:
        return None
    return a % b

if __name__ == '__main__':
    print('somar:', somar(2,3))
    print('subtrair:', subtrair(2,3))
    print('multiplicar:', multiplicar(2,3))
    print('dividir:', dividir(2,3))