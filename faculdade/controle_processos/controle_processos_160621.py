import cmath

def primeiraOrdem(a, b, x):
    print(f'Resolvendo equação de Primeira Ordem passo a passo para obter o polo:')
    print(f'y = {x} / ({a}s + {b})')
    print(f'({a}s + {b}) = 0')
    print(f'{a}s = {-b}')
    print(f's = {-b} / {a}')
    print(f's = {-b / a}')
    print(f'Como não há "s" no numerador, então não é possível resolver, logo, não há nenhum zero.')
    
def segundaOrdem(a, b, c, x):
    print(f'Resolvendo equação de Segunda Ordem passo a passo para obter o polo:')
    print(f'y = {x} / ({a}s^2 + {b}s + {c})')
    print(f'{a}s^2 + {b}s + {c} = 0')
    print(f'd = {b}^2 - 4 * {a} * {c}')
    d = (b**2) - (4*a*c)
    print(f'd = {d}')
    print('Solução 1:')
    print(f'(-{b} + sqrt({d}) / 2 * {a}')
    print(f'({-b} + {cmath.sqrt(d)}) / {2*a}')
    print(f'{(-b + cmath.sqrt(d)) / 2*a}')
    print('Solução 2:')
    print(f'(-{b} - sqrt({d}) / 2 * {a}')
    print(f'({-b} - {cmath.sqrt(d)}) / {2*a}')
    print(f'{(-b - cmath.sqrt(d)) / 2*a}')
    print('Como não há s no numerador, então não há zeros nesta função.')

def ex4():
    print('Exercício 4')
    primeiraOrdem(3, 2, 18)

def ex5():
    print('Exercício 5')
    segundaOrdem(1,2,3,32)

def ex6():
    print('Exercício 6')
    K = 1.8
    T = 0.025
    L = 0

    A = 1 / T
    N = K * A
    # Y = N / (s + A)
    print(f'A = {A}')
    print(f'N = {N}')
    print(f'Y = {N} / (s + {A})')
    
def ex7():
    print('Exercício 7')
    # Y = 35 / (2s + 4)
    K = 35
    T = 2.08
    L = 0.10

    Kp = (0.9/K) * (T/L) 
    Ti = L/0.3
    Td = 0
    
    print(f'Kp = {Kp}')
    print(f'Ti = {Ti}')
    print(f'Td = {Td}')
    
def ex8():
    print('Exercício 8')
    #Y = 60 / (s^2 + 3s + 6)

    K = 60
    T = 1.0170
    L = 0.123

    Kp = (1.2/K) * (T/L) 
    Ti = 2*L
    Td = 0.5*L
    
    print(f'Kp = {Kp}')
    print(f'Ti = {Ti}')
    print(f'Td = {Td}')


def main():
    print('='*15)
    ex4()
    print('='*15)
    ex5()
    print('='*15)
    ex6()
    print('='*15)
    ex7()
    print('='*15)
    ex8()
    

if __name__ == '__main__':
    main()