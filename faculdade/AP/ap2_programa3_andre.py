def Conversor_Inteiro(lista_de_entrada):
    lista_de_saida = []
    for item in lista_de_entrada:
        if item == "I":
            lista_de_saida.append(1)
        elif item == "V":
            lista_de_saida.append(5)
        elif item == "X":
            lista_de_saida.append(10)
        elif item == "L":
            lista_de_saida.append(50)
        elif item == "C":
            lista_de_saida.append(100)
        elif item == "D":
            lista_de_saida.append(500)
        elif item == "M":
            lista_de_saida.append(1000)
    return lista_de_saida

def Somador(lista_de_entrada):
  soma = 0
  for indice in range(0, len(lista_de_entrada)-1):
    if lista_de_entrada[indice] < lista_de_entrada[indice+1]:
      soma = soma - lista_de_entrada[indice]
    else:
      soma = soma + lista_de_entrada[indice]
  soma = soma + lista_de_entrada[len(lista_de_entrada)-1]
  return soma

validador_de_entradas = True
while validador_de_entradas:
  try:
    resposta_entrada = (input("Deseja digitar um novo número romano (s/n) ? ").lower())
    if resposta_entrada == "n":
        print ("Término do Programa!")
        validador_de_entradas = False

    elif resposta_entrada == "s":
      numero_romano = list(input("Digite o numero Romano:").upper())
      lista_inteiro = Conversor_Inteiro(numero_romano)
      if len(numero_romano) != len(lista_inteiro):
        print("Número inválido!")
      else:
        print(f"Numero romano convertido é {Somador(lista_inteiro)}")
        
  except KeyboardInterrupt:
    print("\nExecução Interrompida!")
    validador_de_entradas = False