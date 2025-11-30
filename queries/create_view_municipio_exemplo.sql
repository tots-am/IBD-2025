CREATE VIEW v_dados_completos as
SELECT pib.uf,
	pib.pib_mil_rs,
	pop.ano,
	pop.cod_ibge,
	pop.populacao,
	pop.municipio,
	pib.pib_per_capita_rs
FROM populacaoPorMunicipio pop, pibPorMunicipio pib
WHERE pop.cod_ibge = pib.cod_ibge
AND pop.ano = pib.ano;