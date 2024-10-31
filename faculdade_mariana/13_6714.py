inicial = int(input())
valor = inicial
while True:
    print(valor)
    lista = [int(i) for i in str(valor)]
    lista.sort()
    crescente = lista[0] * 1000 + lista[1] * 100 + lista[2] * 10 + lista[3] 
    decrescente = lista[3] * 1000 + lista[2] * 100 + lista[1] * 10 + lista[0]
    valor = decrescente - crescente
    if valor == 6174:
        print(valor)
        break