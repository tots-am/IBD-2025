WITH z_score_tab AS (
	SELECT
		uf,
		cod_ibge,
		municipio,
		pib_per_capita_rs,
		
		AVG(pib_per_capita_rs) OVER () as media_geral,
		STDDEV(pib_per_capita_rs) OVER () as desvio_padrao_geral
		
	FROM v_dados_completos
	WHERE ano = (SELECT MAX(ano) FROM v_dados_completos)
)
SELECT
	uf,
	municipio,
	cod_ibge,
	pib_per_capita_rs,
	media_geral,
	
	(pib_per_capita_rs - media_geral) / desvio_padrao_geral AS z_score
	
FROM z_score_tab
WHERE ABS((pib_per_capita_rs - media_geral) / desvio_padrao_geral) > 3
ORDER BY z_score DESC;