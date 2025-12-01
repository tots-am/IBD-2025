select m.municipio, m.uf, sum(h.homicidios) as total_homicidios_desde_2010
from municipio m
join homicidio h on m.cod_ibge = h.cod_ibge
where ano > 2009
group by m.municipio, m.uf
order by total_homicidios_desde_2010 desc