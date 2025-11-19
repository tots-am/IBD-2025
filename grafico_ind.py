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

    for vetor in dicionario.values():
        vetor.append(0)

def plota_grafico(x, y, cor, fonte_titulo, fonte_leg, ano):

    plt.figure(figsize = (30,15))
    plt.plot(x, y, color = cor)
    plt.title(f'Número de homicídios por Unidade Federativa {ano}', fontsize = fonte_titulo, pad = 20)
    plt.xlabel('Unidade Federativa', fontsize= fonte_leg , labelpad= 30)
    plt.ylabel('Número de homicídios', fontsize = fonte_leg , labelpad= 30)
    plt.grid()
    # plt.show() se tiver versão interativa

    plt.savefig("homicidios.png")

def organiza_dados(nome, i_ano, ano, i_dado, i_munic):

    dicionario = uf()
    zera_vetor(dicionario)

    x = []
    y = []

    with open(nome, 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')

        next(leitor)

        for linha in leitor:
            if linha[i_ano] == ano:
                dicionario[int(linha[i_munic][0:2])][1] += float(linha[i_dado])  # soma todos os homicídios para cada UF no ano dado

        for dados in dicionario.values():
            x.append(dados[0])
            y.append(dados[1])

    plota_grafico(x, y, 'pink', 28, 22, ano)



organiza_dados('homic.csv', 1, '2011', 2, 0)


