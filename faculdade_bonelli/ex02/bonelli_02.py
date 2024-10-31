# -*- coding: utf-8 -*-
""" f

@author: Quirijn

""" 
import math
WorkDir = r'C:\Users\Cacatua\Desktop\Programacao\python\bonelli\ex02' + '\\'

""" ************************************
*** Abrir e ler o arquivo do cenário 
************************************ """

RunFile = WorkDir + 'CropSim.run'
f = open(RunFile , 'r')
file = f.read()               # importa o arquivo inteiro numa string file
list_str = file.splitlines()  # separa o string file por linhas
MeteoFile = list_str[5]
CropFile = list_str[8]
IniDia = int(list_str[11])
#print(MeteoFile, CropFile, IniDia)  # para testar o input
MeteoFile = WorkDir + MeteoFile    
CropFile = WorkDir + CropFile    
#print(MeteoFile, CropFile, IniDia)  # para testar o input

""" ***************************************
*** Abrir e ler o arquivo meteorológico 
*************************************** """


f = open(MeteoFile , 'r')
file = f.read()               # importa o arquivo inteiro numa string file
list_str = file.splitlines()  # separa o string file por linhas

Rad, Tmin, Tmax, Vap, Vento, Chuva, Tmed = [''],[''],[''],[''],[''],[''],['']


for i in range(4,369):
    a = list_str[i].split()
    Rad.append(float(a[3]))
    Tmin.append(float(a[4]))
    Tmax.append(float(a[5]))
    Vap.append(float(a[6]))
    Vento.append(float(a[7]))
    Chuva.append(float(a[8]))
    
    Tmed.append((Tmin[i-3]+Tmax[i-3])/2)

#print(Rad[1], Vento[365])   #testar input

# raise SystemExit()   ###########################################


#print(Tmed[4], Tmin[365],Tmed[365],Tmax[365])

""" ***************************************
***  Abrir e ler o arquivo de cultura   
*************************************** """

f = open(CropFile , 'r')
file = f.read()               # importa o arquivo inteiro numa string file
list_str = file.splitlines()  # separa o string file por linhas

### Parte 1 - Tabela Kc
KcDVS = []
Kc = []
for i in range(7,13):
    a = list_str[i].split()
    KcDVS.append(float(a[0]))
    Kc.append(float(a[1]))
#print(KcDVS,Kc)
### Soma térmica etc.
TSum1 = float(list_str[16].split()[0])
TSum2 = float(list_str[17].split()[0])
Tb = float(list_str[18].split()[0])
MSi = float(list_str[22].split()[0])
IAFi = float(list_str[23].split()[0])
Vida = float(list_str[27].split()[0])
SLA = float(list_str[28].split()[0])
Kext = float(list_str[32].split()[0])
RUE = float(list_str[33].split()[0])

### Parte 5 - Tabela AMAX e Famax
AMAXDVS, AMAX = [],[]

for i in range(37,43):
    a = list_str[i].split()
    AMAXDVS.append(float(a[0]))
    AMAX.append(float(a[1]))

Tfamax, FAMAX = [],[]

for i in range(46,53):
    a = list_str[i].split()
    Tfamax.append(float(a[0]))
    FAMAX.append(float(a[1]))

###########################
#####   0 -FOLHAS   #######
#####   1 -RAIZES   #######
#####   2 -CAULE    #######
#####   3 -SEMENTE  #######
###########################

### Parte 6 e 7
EC = []
for i in range(56,60):
    EC.append(float(list_str[i].split()[0]))

#print(EC)
#raise SystemExit()   ###########################################
    
Q10 = float(list_str[63].split()[0])

fRM = []
for i in range(64,68):
    fRM.append(float(list_str[i].split()[0]))

#print(fRM)
#raise SystemExit()   ###########################################


### Parte 8 - Tabela Partição
FDVS, F = [],[]

b=[]
for i in range(73,80):
    a = list_str[i].split()
    FDVS.append(float(a[0]))
    for j in range(1,5):
        b.append(float(a[j]))
    F.append(b)
    b=[]
#raise SystemExit()   ###########################################


""" ***************************************
***                                     ***
***         CICLO PRINCIPAL             ***
***                                     ***
*** *********************************** """

# Inicialização

DVS = 0
Dia = IniDia - 1
TSum = 0
IAF = IAFi

Massa = []  ## Massa dos quatro órgãos
for i in range(4):
    Massa.append(MSi * F[0][i])
#print(Massa)

while DVS <= 2:
    
    Dia = Dia + 1
    TSum = TSum + Tmed[Dia] - Tb
    # Determinar DVS
    if TSum <= TSum1:
        DVS = TSum / TSum1
    else:
        DVS = 1 + (TSum-TSum1) / TSum2 

# Interpolar os fatores de partição para o DVS específico 
    Fdia = []
    for d in range(1,7):
        
       if DVS < FDVS[d]:
           for i in range(4):
               Fdia.append((F[d-1][i]*(FDVS[d]-DVS) + F[d][i]*(DVS-FDVS[d-1]))/(FDVS[d]-FDVS[d-1]))

           break
    #print(Dia, round(DVS,3), Fdia)
    #raise SystemExit()   ###########################################

                  
    # Calcular fotossíntese bruta 
    RadAbs = (1 - math.exp(-Kext*IAF)) * Rad[Dia] #kJ/m2
    FotoBr = RadAbs * RUE * 1e-6 * 1e4 # kg/ha
    # print(Dia, round(RadAbs,1), Rad[Dia], round(FotoBr,2))
    # print(RadAbs/Rad[Dia])

## Tarefa para a semana seguinte    
# Calcular a respiração de manutenção a 20°C
RM20 = []
for i in range(0,4):
    RM20.append(round(fRM[i] * Massa[i], 2))
print('RM20: ', RM20)

# Corrigir para a temperatura pelo Q10
RM = []
for componente in RM20:
    RM.append(round(componente * (Q10 ** ((Tmed[Dia] - 20) / 10)), 2))
print('RM: ', RM)

# Somar as RM dos quatro compoenentes para encontrar a RM total
RMTotal = round(sum(RM), 2)
print(f'RMTotal: {RMTotal} kgCH2O/kg/d')