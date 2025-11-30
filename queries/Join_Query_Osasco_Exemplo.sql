SELECT
    homicidios_municipio.cod_ibge,
	populacao_municipio.municipio,
    homicidios_municipio.ano,
    populacao_municipio.populacao,
    pib_municipio.pib_mil_rs,
    pib_municipio.pib_per_capita_rs,
    homicidios_municipio.homicidios
FROM homicidios_municipio
LEFT JOIN populacao_municipio
    ON homicidios_municipio.cod_ibge = populacao_municipio.cod_ibge
    AND homicidios_municipio.ano = populacao_municipio.ano
LEFT JOIN pib_municipio
    ON homicidios_municipio.cod_ibge = pib_municipio.cod_ibge
    AND homicidios_municipio.ano = pib_municipio.ano
WHERE municipio = 'Osasco'; -- Colocar a condição especifica