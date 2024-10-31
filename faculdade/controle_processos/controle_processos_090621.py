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

def ex3():
    print('Exercício 3')
    primeiraOrdem(2, 3, 18)

def ex4():
    print('Exercício 4')
    # ( [-b + sqrt( (b**2)-4*a*c )] / (2 * a) )
    # y = 32 / (s**2 + 3s + 4)
    segundaOrdem(1,3,4,32)

def ex5():
    print('Exercício 5')
    K = 18
    T = 0.25
    L = 0

    A = 1 / T
    N = K * A
    # Y = N / (s + A)
    print(f'A = {A}')
    print(f'N = {N}')
    print(f'Y = {N} / (s + {A})')
    
def ex6():
    print('Exercício 6')
    # Y = 35 / (2s + 4)
    K = 35
    T = 0.52
    L = 0.1

    Kp = (0.9/K) * (T/L) 
    Ti = L/0.3
    Td = 0
    
    print(f'Kp = {Kp}')
    print(f'Ti = {Ti}')
    print(f'Td = {Td}')
    
def ex7():
    print('Exercício 7')
    #Y = 26 / (s^2 + 5s + 7)

    K = 26
    T = 1.48
    L = 0.17

    Kp = (1.2/K) * (T/L) 
    Ti = 2*L
    Td = 0.5*L
    
    print(f'Kp = {Kp}')
    print(f'Ti = {Ti}')
    print(f'Td = {Td}')


def main():
    ex3()
    print('='*15)
    ex4()
    print('='*15)
    ex5()
    print('='*15)
    ex6()
    print('='*15)
    ex7()
    

if __name__ == '__main__':
    main()