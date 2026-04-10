#!/bin/bash
find /home/ubuntu/proyecto/logs -name "*.log" -mtime +7 -delete
echo "Logs limpiados: $(date)" >> /home/ubuntu/proyecto/logs/limpieza.log
