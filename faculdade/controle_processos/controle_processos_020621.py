def ex2():
    print('Exercício 2')
    K = 1
    T = 0.994
    L = 0.1

    kp = (1.2/K) * (T/L)
    ti = 2*L
    td = 0.5*L
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')
    
def ex3():
    print('Exercício 3')
    K = 1
    T = 0.994
    L = 0.1

    kp = (0.6/K) * (T/L)
    ti = T
    td = 0.5*L
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')

def ex4():
    print('Exercício 4')
    K = 1
    T = 0.994
    L = 0.1

    kp = (0.95/K) * (T/L)
    ti = 1.357*T
    td = 0.474*L
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')
    
def ex5():
    print('Exercício 5')
    K = 1
    T = 0.994
    L = 0.1

    kp = (1/K) * (0.25+1.35*(T/L))
    ti = L*( (1.35+0.25*(L/T)) / (0.54+0.33*(L/T)) )
    td = ( 0.5*L / (1.35+0.25*(L/T)) )
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')
    
def ex6():
    print('Exercício 6')
    K = 1
    T = 0.994
    L = 0.1

    kp = 1/K * (1.435*(L/T)**-0.921)
    ti = T / (0.878*(L/T)**-0.749)
    td = T * (0.482*(L/T)**1.137)
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')
    
def ex7():
    print('Exercício 7')
    K = 1
    T = 0.994
    L = 0.1

    kp = 1/K * (1.357*(L/T)**-0.947)
    ti = T / (0.842*(L/T)**-0.738)
    td = T * (0.381*(L/T)**0.995)
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')
    
def ex8():
    print('Exercício 8')
    K = 1
    T = 0.994
    L = 0.1

    kp = (0.965/K) * ((T/L)**0.85)
    ti = T / (0.796-0.1465*(L/T))
    td = 0.308*T * ((L/T)**0.929)
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')
    
def ex9():
    print('Exercício 9')
    K = 1
    T = 0.994
    L = 0.1

    kp = (1.357/K) * ((T/L)**0.947)
    ti = (T/0.842) * ((L/T)**0.738)
    td = 0.381*T * ((L/T)**0.995)
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')

def ex10():
    print('Exercício 10')
    K = 1
    T = 0.994
    L = 0.1

    kp = (2*T+L) / (2.6*K*L)
    ti = T+(L/2)
    td = (T*L) / (2*T+L)
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')

def ex11():
    print('Exercício 11')
    K = 1
    T = 0.994
    L = 0.1

    kp = 1 / K*(L+T)
    ti = 4*(L+T)
    td = T*2
    
    print(f'kp = {kp}')
    print(f'ti = {ti}')
    print(f'td = {td}')



def main():
    ex2()
    print('='*15)
    ex3()
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
    print('='*15)
    ex9()
    print('='*15)
    ex10()
    print('='*15)
    ex11()
    print('='*15)

if __name__ == '__main__':
    main()