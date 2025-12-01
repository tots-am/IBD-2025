CREATE TABLE municipio AS
SELECT 
	pop.cod_ibge,
	pop.municipio,
	pib.uf
FROM populacao_municipio pop, pib_municipio pib
WHERE pop.cod_ibge = pib.cod_ibge
GROUP BY pop.cod_ibge, pop.municipio, pib.uf;