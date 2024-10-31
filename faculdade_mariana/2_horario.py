# Importação das bibliotecas
from datetime import datetime

def sono():
    h_1 = input() # Hora do primeiro horário
    m_1 = input() # Minutos do primeiro horário
    h_2 = input() # Hora do segundo horário
    m_2 = input() # Minutos do segundo horário

    # Convertendo os valores lidos para horários e assim realizar cálculos entre eles
    horario1 = datetime.strptime(f"{h_1}:{m_1}", "%H:%M")
    horario2 = datetime.strptime(f"{h_2}:{m_2}", "%H:%M")

    # Calculando a diferença entre os horários
    diferenca = horario2 - horario1

    # Verificando se dormiu 8 horas ou mais
    if diferenca.seconds >= 28800: #28800 equivale a 8 horas em segundos
        print("True")
    else:
        print("False")
    
def main():
    sono()

if __name__ == '__main__':
    main()