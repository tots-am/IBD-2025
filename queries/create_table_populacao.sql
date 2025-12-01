CREATE TABLE populacao AS
SELECT 
	pop.cod_ibge,
	pop.ano,
	pop.populacao
FROM populacao_municipio pop;