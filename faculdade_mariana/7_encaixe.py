n = int(input())

for _ in range(n):
    Peça1 = [int(m) for m in input().split()]
    Peça2 = [int(m) for m in input().split()]

    K1 = len(Peça1)
    K11 = len(Peça1)
    K2 = len(Peça2)
    K22 = len(Peça2)

    a = True
    b = True
    t = [] #pontuação em cada posição
    t2 = [] #pontuação em cada posição invertida
    T11 = Peça1.reverse()
    T22 = Peça2.copy()
    
    while K2 >= K1:
        m = 0
        w = []
        while m < K1:
            x = Peça1[m] + Peça2[m]
            w.append(x)
            m = m + 1
        l = max(w) #altura máx
        l1 = l * K1 - sum(w)
        t.append(l1)
        if l1 == 0:
            a = False
        Peça2.pop(0)
        K2 = K2 - 1

    if a == False:
        r = t.index(0) + 1 #encaixe perfeito
        print('Encaixe Perfeito!')
        print('Posição de Encaixe:', r)
        print('Peca 1: Normal')
    else:
        while K22 >= K11:
            m = 0
            w = []
            while m < K11:
                x = T11[m] + T22[m]
                w.append(x) #soma das alturas das peças
                m = m + 1
            l = max(w) 
            l1 = l * K11 - sum(w)
            Peça2.append(l1) 
            if l1 == 0:
                b = False 
            T22.pop(0)
            K22 = K22 - 1

        if b == False:
            f = Peça2.index(0) + 1
            print('Encaixe Perfeito!')
            print('Posicao de Encaixe:', f)
            print('Peca 1: Invertida')
        else:
            c1 = min(t)
            c2 =  min(w)
            if c1 <= c2:
                c11 = t.index(c1) + 1
                print('Pontuacao:', c1)
                print('Posicao de Encaixe:', c11)
                print('Peca 1: Normal')
            else:
                c22 = Peça2.index(c2) + 1
                print('Pontuacao:', c2)
                print('Posicao de Encaixe:', c22)
                print('Peca 1: Invertida')