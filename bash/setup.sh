#!/bin/bash
echo "Instalar dependencias"
sudo apt update -y
sudo apt install git vim docker.io python3 python3-pip -y
sudo pip3 install boto3 --break-system-packages

echo "Se esta iniciando Docker"
sudo service docker start

echo "Creando carpetas "
mkdir -p /home/ubuntu/proyecto/{scripts,logs,docker}

echo "Se ha terminado, todo listo"
