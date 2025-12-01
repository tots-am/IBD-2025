CREATE TABLE homicidio AS
SELECT 
	h.cod_ibge,
	h.ano,
	h.homicidios
FROM homicidios_municipio h;