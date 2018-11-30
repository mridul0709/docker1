rm -rf consul db_ip db_port
curl consul:8500/v1/catalog/service/db\?pretty > consul
cat consul | grep ServiceAddress |awk -F '\"' '{print $4}' > db_ip
#cat consul | grep ServiceAddress | awk '{print $2}' | cut -d ',' -f1 > db_ip
cat consul |grep ServicePort |awk -F ': ' '{print $2}' |awk -F ',' '{print $1}' > db_port
