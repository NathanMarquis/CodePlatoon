select *
from stations
join reports on stations.id = reports.station_id
;