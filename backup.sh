#!/bin/bash

# Obtén la fecha actual en el formato deseado (por ejemplo, YYYYMMDD).
fecha_actual=$(date +%Y-%m-%d)

# Obtén la fecha de ayer en formato "YYYY-MM-DD"
fecha_ayer=$(date -d "yesterday" +%Y-%m-%d)

# Crea la carpeta con la fecha actual en /var/tmp/Backups/
mkdir -p "/var/tmp/Backups/$fecha_actual"

# Realiza la copia de seguridad incremental al directorio creado
rsync -av --link-dest="/var/tmp/Backups/$fecha_ayer" /home/jon/Segurtasuna/ "/var/tmp/Backups/$fecha_actual/"

#crontab -e
