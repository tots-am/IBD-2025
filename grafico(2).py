import matplotlib.pyplot as plt
import csv

def uf():
    # Primeiros dígitos de cod_ibge e UF correspondente

    cod = { 11: ['RO'], 12: ['AC'], 13:	['AM'], 14: ['RR'], 15:	['PA'], 16:	['AP'],
    17: ['TO'], 21:	['MA'], 22:	['PI'], 23:	['CE'], 24:	['RN'], 25:	['PB'], 26:	['PE'],
    27:	['AL'], 28:	['SE'], 29:	['BA'], 31:	['MG'], 32:	['ES'], 33:	['RJ'], 35:	['SP'],
    41:	['PR'], 42:	['SC'], 43:	['RS'], 50:	['MS'], 51:	['MT'], 52:	['GO'], 53:	['DF']}

    return cod

def zera_vetor(dicionario):
    # Cria em uf() um vetor com zeros para acumular dados (homicidios, pib, população, num de municipios contados)

    for vetor in dicionario.values():
        vetor.append(0)
        vetor.append(0)
        vetor.append(0)
        vetor.append(0)

def plota_grafico(ano, x1, y1, x2, y2, x3, y3, cor1, cor2, cor3, fonte_titulo, fonte_leg, dist):
    
    fig, eixos = plt.subplots(3, 1, figsize=(32, 24))

    plt.subplots_adjust(hspace=0.8) #Espaçamento 

    eixos[0].plot(x1, y1, color = cor1)
    eixos[0].set_title(f'Número percentual de homicídios por Unidade Federativa {ano}', fontsize = fonte_titulo, pad = dist)
    eixos[0].set_xlabel('Unidade Federativa', fontsize= fonte_leg, labelpad= dist)
    eixos[0].set_ylabel("Homicídios", fontsize= fonte_leg, labelpad= dist)
    eixos[0].fill_between(x1, y1, color = cor1, alpha=0.1)

    eixos[1].plot(x2, y2, color = cor2)
    eixos[1].set_title(f'PIB per capita por Unidade Federativa {ano}', fontsize = fonte_titulo, pad = dist)
    eixos[1].set_xlabel('Unidade Federativa', fontsize= fonte_leg, labelpad= dist)
    eixos[1].set_ylabel('PIB per capita medio', fontsize= fonte_leg, labelpad=dist)
    eixos[1].fill_between(x2, y2, color = cor2, alpha=0.1)

    eixos[2].plot(x3, y3, color = cor3)
    eixos[2].ticklabel_format(style='plain', axis='y')
    eixos[2].set_title(f'População por Unidade Federativa {ano}', fontsize = fonte_titulo, pad = dist)
    eixos[2].set_xlabel('Unidade Federativa', fontsize= fonte_leg, labelpad=dist)
    eixos[2].set_ylabel('População', fontsize= fonte_leg, labelpad=dist)
    eixos[2].fill_between(x3, y3, color = cor3, alpha=0.1)

    for ax in eixos:
        ax.grid(True)
    
    for eixo in eixos:
        eixo.tick_params(axis='both', labelsize=22)  # aumenta fonte dos ticks

    plt.savefig("graficos_comparativos.png")

def le_dados(nome, dicionario, x, y, i_ano, ano, i_dado, i_munic, i_vetor):

    with open(nome, 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')

        next(leitor)

        for linha in leitor:
            if linha[i_ano] == ano:
                dicionario[int(linha[i_munic][0:2])][i_vetor] += float(linha[i_dado])  # soma todos os dados para cada UF no ano dado
                
                if i_vetor == 2:
                    dicionario[int(linha[i_munic][0:2])][4] += 1  # acumula número de municípios que o pib per capita foi somado

        for dados in dicionario.values():
            x.append(dados[0])

            if i_vetor == 2:
                y.append(round(dados[i_vetor] / dados[4], 2))
            elif i_vetor == 1:
                y.append((dados[i_vetor] / dados[3])*100)
            else:
                y.append(round(dados[i_vetor], 2))

        

def organiza_dados():

    ano= '2020'

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    dicionario = uf()

    zera_vetor(dicionario)

    le_dados('pop.csv', dicionario, x3, y3, 2, ano, 3, 0, 3)
    le_dados('homic.csv', dicionario, x1, y1, 1, ano, 2, 0, 1) 
    le_dados('pib.csv', dicionario, x2, y2, 0, ano, 4, 2, 2)


    plota_grafico(ano, x1, y1, x2, y2, x3, y3, 'pink', 'yellow', 'red', 40, 30, 26)

organiza_dados()






