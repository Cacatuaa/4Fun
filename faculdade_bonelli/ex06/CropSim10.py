# -*- coding: utf-8 -*-
""" f

@author: Quirijn

""" 
import math
import sys
WorkDir = r'C:\Users\Cacatua\Desktop\Programacao\python\bonelli\ex06' + '\\'

# Funcoes criadas

# Equação de Magnus/Tetens
def tet(T, A, B, C):
    '''Retorna o valor da função de Magnus/Tetens 
    T em °C, Resultado em kPa
    '''

    tet1 =  A * math.exp((B * T)/(C + T))
    return tet1

# Derivada da Equação de Magnus/Tetens
def dtet(T, A, B, C):
    '''Retorna o valor da derivada da função de Magnus/Tetens 
    T em °C,  Resultado em kPa/°C
    '''

    dtet1 = tet(T, A, B, C) * (B / (C + T) - B * T / (C + T)**2)        
    return dtet1

# equacao de evapotranspiracao
def EVp(T, Rn, u, e_a):
    '''Retorna a evapotranspiracao potencial em mm/dia
    '''
    gamma_a = 0.067290539
    R_u = 0.8 * Rn / 1000   # o /1000 é pra transf kJ em MJ
    
    dv = dtet(T, A, B, C)
    e_sat = tet(T, A, B, C)
    
    EVpot_numerador = 0.408*dv*R_u + gamma_a*u*(e_sat-e_a)*900/(T + 273)
    EVpot_denominador = dv + gamma_a*(1 + 0.34*u)
    EVpot = EVpot_numerador/EVpot_denominador
    return EVpot

def fator_p(GrupoCultura, ETc):
    #Retorna o valor do fator p (AFD/AD) 
    
    a1 = -.00723
    a2 = -.04643
    b1 = .142589
    b2 = .453571
    a = a1 * GrupoCultura + a2
    b = b1 * GrupoCultura + b2
    
    p = a * ETc + b
    #print(p)
    return p

""" ************************************
*** Constantes 
************************************ """
# Eq de Magnus/Tetens
A = .61078
B = 17.27
C = 237.3
# Eq de Magnus/Alduchov
#A = .61094
#B = 17.625
#C = 243.04


""" ************************************
*** Abrir e ler o arquivo do cenário 
************************************ """

RunFile = WorkDir + 'CropSim.run'

f = open(RunFile , 'r')
file = f.read()               # importa o arquivo inteiro numa string file
list_str = file.splitlines()  # separa o string file por linhas
SoilFile = WorkDir + list_str[5]                    # <<=======================
CropFile = WorkDir + list_str[8]

NMetFiles = int(list_str[11].split()[0])            # <<=======================
MeteoFile = []
for i in range(NMetFiles):
    MeteoFile.append(WorkDir + list_str[12+i])
IniDia = int(list_str[14+NMetFiles])
#print(SoilFile, MeteoFile, CropFile, IniDia)  # para testar o input

""" ********************************************
*** Abrir e ler o arquivo do solo 
******************************************** """

Zcamada, TetaINI, TetaCC, TetaPMP, ArmazCC = [0],[''],[''],[''],['']

f = open(SoilFile , 'r')
file = f.read()               # importa o arquivo inteiro numa string file
list_str = file.splitlines()  # separa o string file por linhas

NCamadas = int(list_str[5])
ZeMax = float(list_str[8])
for i in range(1,NCamadas+1):
    Zcamada.append(float(list_str[11+i].split()[0]))
    TetaINI.append(float(list_str[11+i].split()[1]))
    TetaCC.append(float(list_str[11+i].split()[2]))
    TetaPMP.append(float(list_str[11+i].split()[3]))
    ArmazCC.append(TetaCC[i] * 10 * (Zcamada[i] - Zcamada[i-1])) 
#print(ZeMax, TetaINI, TetaCC, TetaPMP)  # para testar o input

""" ********************************************
*** Abrir e ler o(s) arquivo(s) meteorológico(s) 
******************************************** """

Rad, Tmin, Tmax, Vap, Vento, Chuva, Tmed = [''],[''],[''],[''],[''],[''],['']

for j in range(NMetFiles):                    # <<=======================
    f = open(MeteoFile[j] , 'r')
    file = f.read()               # importa o arquivo inteiro numa string file
    list_str = file.splitlines()  # separa o string file por linhas

    for i in range(4,369):
        a = list_str[i].split()
        Rad.append(float(a[3]))
  #       Rad.append(float(f.read().splitlines()[i].split()[3]))
        Tmin.append(float(a[4]))
        Tmax.append(float(a[5]))
        Vap.append(float(a[6]))
        Vento.append(float(a[7]))
        Chuva.append(float(a[8]))
    
        Tmed.append((Tmin[i-3]+Tmax[i-3])/2)


#print(Tmed[4], Tmin[365],Tmed[365],Tmax[365])

""" ***************************************
***  Abrir e ler o arquivo de cultura   
*************************************** """

f = open(CropFile , 'r')
file = f.read()               # importa o arquivo inteiro numa string file
list_str = file.splitlines()  # separa o string file por linhas

### Parte 1 - Tabela Kc
KcDVS, Kc, Ze = [], [], []
for i in range(7,13):
    a = list_str[i].split()
    KcDVS.append(float(a[0]))
    Kc.append(float(a[1]))
    Ze.append(float(a[2]))                                # <<=======================

#print(KcDVS,Kc)
### Soma térmica etc.
TSum1 = float(list_str[16].split()[0])
TSum2 = float(list_str[17].split()[0])
Tb = float(list_str[18].split()[0])
MSi = float(list_str[22].split()[0])
IAFi = float(list_str[23].split()[0])
VidaR = float(list_str[26].split()[0])                    # <<=======================
VidaF = float(list_str[27].split()[0])                    # <<=======================
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

### checar se fatores de partição somam 1             # <<=======================                 
for i in range(7):
    FSum = 0.
    for j in range(4):
        FSum = FSum + F[i][j]
    if FSum != 1:
        print('Soma da partição do DVS ', FDVS[i], 'não é igual a 1' )
        sys.exit()

GrupoCultura = int(list_str[83].split()[0])

f.close()

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

DeltaIAF, DeltaMassaf, DeltaMassar = [''], [''], ['']
IAFmax=0

FracZ, Armaz, Teta = [0.],[0.],[0.]
for n in range(1,NCamadas+1):
    FracZ.append(float(0.))
    Armaz.append(float(0.))
    Teta.append(TetaINI[n])
    
ChuvaTot = 0
TransTot = 0
EvapoTot = 0
ExcedTot = 0

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
        SLA = SLA2                         

    # Interpolar Kc e Ze para o DVS específico 
    for i in range(1,6):
        
       if DVS < KcDVS[i]:
           Zedia = (Ze[i-1]*(KcDVS[i]-DVS) + Ze[i]*(DVS-KcDVS[i-1]))/(KcDVS[i]-KcDVS[i-1])
           Kcdia = (Kc[i-1]*(KcDVS[i]-DVS) + Kc[i]*(DVS-KcDVS[i-1]))/(KcDVS[i]-KcDVS[i-1])
           if Zedia > ZeMax:
               Zedia = ZeMax
           break
           #print(Dia, NDia, round(DVS,2), round(Zedia,3),round(Kcdia,3))


# Interpolar os fatores de partição para o DVS específico 
    Fdia = []
    for d in range(1,7):
        
       if DVS < FDVS[d]:
           for i in range(4):
               Fdia.append((F[d-1][i]*(FDVS[d]-DVS) + F[d][i]*(DVS-FDVS[d-1]))/(FDVS[d]-FDVS[d-1]))

           break
    #print(Dia, round(DVS,3), Fdia)

   # Cálculo da ETp - ETc
   
    ETp = EVp(Tmed[Dia], Rad[Dia], Vento[Dia], Vap[Dia])
    #print(f'Dia: {Dia}  Tmed: {round(Tmed[Dia],1)}  ETp: {round(ETp,3):0<5}')
     
    ETc = ETp * Kcdia
    Evapo = ETc * math.exp(-IAF)
    Trans = ETc - Evapo

    # Fator de fracionamento da Trans entre as camadas do solo
    for n in range(1,NCamadas+1):
        if Zcamada[n] <= Zedia:
            FracZ[n] = (Zcamada[n] - Zcamada[n-1]) / Zedia
        elif Zcamada[n-1] > Zedia: 
            FracZ[n] = 0
        else: 
            FracZ[n] = (Zedia - Zcamada[n-1]) / Zedia 
    #print(Dia, NDia, FracZ)


    # Chama a função do cálculo do fator p                     $$$$$$$$$$$$$$$$$$$$$$$
    p = fator_p(GrupoCultura, ETc)
    # print(p)

   
###    INSERIR AQUI O CÁLCULO DA REDUÇÃO DE TRANSPIRAÇÃO      ***
    arrayPrint = []
    arrayPrint.append(Dia)

    Ta = 0
    for n in range(1,NCamadas+1):
        umidade = TetaPMP[n] + ((1 - p) * (TetaCC[n] - TetaPMP[n]))
        arrayPrint.append(umidade)
        if TetaINI[n] >= umidade:
            sRel = 1
        elif TetaINI[n] <= TetaPMP[n]:
            sRel = 0
        elif TetaINI[n] > TetaPMP[n] and TetaINI[n] < umidade:
            sRel = (TetaINI[n] - TetaPMP[n]) / (umidade - TetaPMP[n])
        
        if GrupoCultura == 0:
            sRel = 1

        extracao = FracZ[n] * Trans * sRel
        Ta = Ta + extracao

# Calcular nova úmidade (balanço hídrico por camada)
    Excedente = 0
    
    for n in range(1,NCamadas+1):
        Armaz[n] = Teta[n] * 10 * (Zcamada[n] - Zcamada[n-1]) # em mm
        Armaz[n] = Armaz[n] - extracao + Excedente
        if n == 1:
            Armaz[n] = Armaz[n] - Evapo + Chuva[Dia]
        if Armaz[n] > ArmazCC[n]:
            Excedente = Armaz[n] - ArmazCC[n]
            Armaz[n] = ArmazCC[n]
        else:
            Excedente = 0
            
            
        Teta[n] = Armaz[n] / (Zcamada[n] - Zcamada[n-1]) / 10

        
    # Valores totais, acumulados
    ChuvaTot = ChuvaTot + Chuva[Dia]
    TransTot = TransTot + Trans
    EvapoTot = EvapoTot + Evapo
    ExcedTot = ExcedTot + Excedente
  
                  
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
    FotoLiq = (FotoBr * (Ta / TransTot)) - RMtot
    arrayPrint.append(Ta / Trans)
    
    for item in arrayPrint:
        print(item, end='\t')
    print()
    
    # Somar a fotossíntese líquida particionada à massa de cada órgão
    for i in range(4):
        Massa[i]= Massa[i] + FotoLiq * Fdia[i] * EC[i]


    # Incluir a vida útil das folhas, calcular o novo IAF e Massa[0] das folhas
    #IAF = SLA * Massa[0]     - ANTIGO!
    
    DeltaIAF.append(float(SLA * FotoLiq * Fdia[0] * EC[0]))
    DeltaMassaf.append(float(FotoLiq * Fdia[0] * EC[0]))
    DeltaMassar.append(float(FotoLiq * Fdia[1] * EC[1]))
    #print(DeltaIAF)
    
    if NDia <= VidaF:
        IAF = IAF + DeltaIAF[NDia]
    else:
        IAF = IAF + DeltaIAF[NDia] - DeltaIAF[NDia - int(VidaF)]
        Massa[0] = Massa[0] - DeltaMassaf[NDia - int(VidaF)]

    if NDia > VidaR:                            # <<=======================
        Massa[1] = Massa[1] - DeltaMassar[NDia - int(VidaR)]
    
    
   # print(Dia,round(DVS,3),round(IAF,3),round(Massa[3],1))    
