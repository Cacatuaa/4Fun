pontuacao = [".", ",", ":", ";", "!", "?"]
frase = ''
palindromes = {}
for _ in range(int(input(''))):
    frase += input('').lower()
    frase += " "

frase = frase.rstrip()

for item in pontuacao:
    frase = frase.replace(item, "")

palavras = frase.split(" ")
for palavra in palavras:
    if palavra == palavra[::-1]:
        if palavra not in palindromes:
            palindromes[palavra] = 1
        else:
            palindromes[palavra] = palindromes[palavra] + 1

for palavra, valor in palindromes.items():
    print(f'{palavra} {valor}')
