#1° Etapa de construccion
FROM node:18-alpine AS builder
WORKDIR /app
COPY . .

#2° etapa de produccion
FROM nginx:latest
COPY --from=builder /app /usr/share/nginx/html
EXPOSE 80
