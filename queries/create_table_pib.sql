CREATE TABLE pib AS
SELECT 
	pib.cod_ibge,
	pib.ano,
	pib.pib_mil_rs,
	pib_per_capita_rs
FROM pib_municipio pib;