import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

#Conexão
#Substitua: usuario, senha, host (geralmente localhost), porta (5432) e nome_do_banco
string_conexao = 'postgresql+psycopg2://usuario:senha@localhost:5432/trabalho_ibd'
db_connection = create_engine(string_conexao)

#Populacao
query0 = """
SELECT
	uf,
	municipio,
	ano,
	populacao
	
FROM v_dados_completos
WHERE cod_ibge in ('311535', '150215', '316190', '313370')
ORDER BY cod_ibge, ano;
"""

#Pib per capita 
query1 = """
SELECT
	uf,
	municipio,
	ano,
	pib_per_capita_rs
	
FROM v_dados_completos
WHERE cod_ibge in ('311535', '150215', '316190', '313370')
ORDER BY cod_ibge, ano;
"""

#Query homicidios
query2 = """
SELECT
	h.cod_ibge,
	h.homicidios,
	h.ano,
	v.uf,
	v.municipio,
	
	ROUND((h.homicidios::NUMERIC / NULLIF(v.populacao, 0)) * 100000, 2) AS taxa_homicidios_100k
	
FROM v_dados_completos v, "homicidiosPorMunicipio" h
WHERE h.cod_ibge = v.cod_ibge
AND h.ano = v.ano
AND h.cod_ibge in ('311535', '150215', '316190', '313370')
ORDER BY h.cod_ibge, h.ano;
"""

df_populacao = pd.read_sql(query0, db_connection)
df_pib = pd.read_sql(query1, db_connection)
df_homicidio = pd.read_sql(query2, db_connection)


df_populacao = df_populacao.drop_duplicates()
df_pib = df_pib.drop_duplicates()
df_homicidio = df_homicidio.drop_duplicates()


fig, eixos = plt.subplots(nrows=3, ncols=1, figsize=(12, 15), sharex=True)

#Gráfico pib
sns.lineplot(
    data= df_pib,
    x= 'ano',
    y= 'pib_per_capita_rs',
    hue= 'municipio',
    palette= 'deep',
    style = 'municipio',
    dashes= True,
    marker= 'o',
    markersize=8,
    linewidth= 3.5, 
    ax=eixos[0]
    )     

#Gráfico pop
sns.lineplot(
    data= df_populacao,
    x= 'ano',
    y= 'populacao',
    hue= 'municipio',
    palette= 'deep',
    marker= 'o',
    markersize=8,
    linewidth= 3.5,
    ax=eixos[1]
    )   

#Gráfico homicidio
sns.lineplot(
    data=df_homicidio, 
    x = 'ano', 
    y = 'taxa_homicidios_100k', 
    marker="o",
    markersize=9,
    dashes=True, #permite o tracejado 
    linewidth=3, 
    hue='municipio', #pintar para cada cidade
    style='municipio', #cria um estilo para cada cidade
    palette='deep', #paleta de cores
    ax=eixos[2]
    )

#Definições
eixos[0].set_title("Evolução da PIB Per Capita ao longo dos anos")
eixos[0].set_ylabel("PIB Per Capita")
eixos[0].legend(fontsize='11', loc='upper left')
eixos[0].grid(True, linestyle='--', alpha=0.5) 

eixos[1].set_title("Evolução da população ao longo dos anos")
eixos[1].set_ylabel("População")
eixos[1].get_legend().remove()
eixos[1].grid(True, linestyle='--', alpha=0.5) 

eixos[2].set_title("Comparativo de violência em cidades consideradas Outliers")
eixos[2].set_ylabel("Homícidios a cada 100 mil habitantes")
eixos[2].get_legend().remove()
eixos[2].grid(True, linestyle='--', alpha=0.5)

todos_os_anos = sorted(df_pib['ano'].unique())
plt.xticks(todos_os_anos, fontsize=12, rotation=45)

sns.despine(top=True, right=True) # Remove bordas superior e direita
plt.tight_layout()

nome_fig = "tres_graficos.png"
plt.savefig(nome_fig, dpi=400)

plt.show()

