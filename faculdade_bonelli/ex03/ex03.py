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
SLA1 = float(list_str[28].split()[0])     ################
SLA2 = float(list_str[29].split()[0])     ################
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
NDia = 0
TSum = 0
IAF = IAFi

Massa = []  ## Massa dos quatro órgãos
for i in range(4):
    Massa.append(MSi * F[0][i])
#print(Massa)

DeltaIAF = ['']
DeltaMassaf = ['']
IAFmax=0

while DVS <= 2:
    
    Dia = Dia + 1    # conta dia ordinal
    NDia = NDia + 1  # conta a partir de 1
    TSum = TSum + Tmed[Dia] - Tb
    # Determinar DVS
    if TSum <= TSum1:
        DVS = TSum / TSum1
    else:
        DVS = 1 + (TSum-TSum1) / TSum2 

    # Interpolar o SLA entre SLA1 e SLA2 
    if DVS < 1:                            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        SLA = SLA1 + (SLA2-SLA1)*DVS       #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:                                  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        SLA = SLA2                         #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


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


    #print(Dia, round(RadAbs,1), Rad[Dia], round(FotoBr,2))
    

   # Calcular a respiração de manutenção 
    RM = []
    RMtot = 0
    for i in range(4):
        RM.append(Massa[i] * fRM[i] * (Q10 ** ((Tmed[Dia]-20)/10)))
        RMtot = RMtot + RM[i]
    #print(Dia,round(FotoBr,3), round(RMtot,3))    
    # Calcular fotossíntese líquida e particionar
    FotoLiq = FotoBr - RMtot
    
    # Somar a fotossíntese líquida particionada à massa de cada órgão
    for i in range(4):
        Massa[i]= Massa[i] + FotoLiq * Fdia[i] * EC[i]


    # Incluir a vida útil das folhas, calcular o novo IAF e Massa[0] das folhas
    #IAF = SLA * Massa[0]     - ANTIGO!
    
    DeltaIAF.append(float(SLA * FotoLiq * Fdia[0] * EC[0]))
    DeltaMassaf.append(float(FotoLiq * Fdia[0] * EC[0]))
    #print(DeltaIAF)
    
    if NDia <= Vida:
        IAF = IAF + DeltaIAF[NDia]
    else:
        IAF = IAF + DeltaIAF[NDia] - DeltaIAF[NDia - int(Vida)]
        Massa[0] = Massa[0] - DeltaMassaf[NDia - int(Vida)]

    if IAF > IAFmax:
        IAFmax = IAF
    
    
    print(Dia,round(DVS,3),round(IAF,3),round(Massa[3],1))    