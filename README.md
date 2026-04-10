# Avance Proyecto Final — Fundamentos de DevOps

**Universidad Tecmilenio**  
**Materia:** Fundamentos de DevOps  
**Docente:** Juan Manuel Cepeda Barragán  
**Fecha:** 10 de Abril del 2026

---

## Integrantes

| Nombre | Matrícula |
|---|---|
| César Julián Espronceda Pantoja | AL07040765 |
| Daniel Alejandro González Salazar | AL07076433 |

---

## Descripción

Este repositorio contiene el avance del proyecto final de la materia Fundamentos de DevOps. Se implementaron prácticas reales de DevOps usando AWS Learner Lab: automatización con Bash y Python/Boto3, infraestructura como código con CloudFormation y contenerización con Docker + nginx.

---

## Detalle por Componente

### bash/setup.sh
Automatiza la configuración inicial del entorno en la instancia EC2:
- Actualiza paquetes con `apt update`
- Instala `git`, `vim`, `docker.io`, `python3`, `python3-pip` y `boto3`
- Inicia el servicio Docker
- Crea la estructura de carpetas del proyecto: `scripts/`, `logs/`, `docker/`

### bash/limpiar_logs.sh
Script de limpieza programado vía cron (`0 2 * * *`):
- Elimina archivos `.log` con más de 7 días en `/home/ubuntu/proyecto/logs`
- Registra cada ejecución en `limpieza.log` con fecha y hora

### cloudformation/cloudformation.yaml
Plantilla de infraestructura como código que define:
- **BucketS3:** bucket con nombre dinámico `devops-stf-{AccountId}`
- **ServidorWeb:** instancia EC2 t2.micro con UserData que instala y arranca Docker automáticamente
- **ServidorApp:** instancia EC2 t2.micro con tag `devops-servidor-app`
- Ambas instancias usan `IamInstanceProfile: LabInstanceProfile`

### docker/Dockerfile
Multi-stage build en dos etapas:
1. **Builder:** `node:18-alpine` — copia el proyecto a `/app`
2. **Producción:** `nginx:latest` — sirve los archivos del builder desde `/usr/share/nginx/html` en el puerto 80

### docker/docker-compose.yml
Orquesta dos servicios sobre la red `devops-network` (driver: bridge):
- **web:** construye la imagen local, expone el puerto `8080:80`, monta `./logs:/var/log/nginx`
- **monitor:** usa `nginx:latest` directamente, expone el puerto `8081:80`

### scripts/aws_manager.py
Script Python con Boto3 que conecta a AWS en `us-east-1` y ejecuta 4 funciones:

| Función | Descripción |
|---|---|
| `crear_instancia()` | Lanza una instancia EC2 t2.micro con tag `devops-boto3` |
| `listar_instancias()` | Muestra ID, tipo e estado de todas las instancias |
| `listar_buckets()` | Lista buckets S3 con sus objetos y tamaños en bytes |
| `generar_reporte()` | Genera y guarda un reporte JSON en `/home/ubuntu/proyecto/logs/reporte.json` |

### .gitignore
Excluye del repositorio: `*.log`, `*.env`, `__pycache__/`, `.DS_Store`, `node_modules/`

---

## 📎 Recursos

- 📊 [Presentación en Canva](https://canva.link/za5dlaizxk6u9hc)

---
