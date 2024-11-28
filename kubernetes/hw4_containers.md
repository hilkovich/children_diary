# Контейнеризация и оркестрация: ЛР 4 - More Kubernetes

### Требования:
- Нужно развернуть сервис в связке из минимум 2 контейнеров + 1 init
- Минимум два Deployment, по количеству сервисов
- Кастомный образ для минимум одного Deployment (т.е. не публичный и собранный из своего Dockerfile)
- Минимум один Deployment должен содержать в себе контейнер и инит-контейнер
- Минимум один Deployment должен содержать volume (любой)
- Обязательно использование ConfigMap и/или Secret
- Обязательно Service хотя бы для одного из сервисов
- Liveness и/или Readiness пробы минимум в одном из Deployment
- Обязательно использование лейблов (помимо обязательных selector/matchLabel)
- Файлы нужных манифестов
- README.md с описанием хода работы

### 1. Сборка образа
```
docker build -t bot:latest
minikube image load bot:latest
```

### 2. Запуск minikube
```
minikube start
```

### 3. Применение Secret
```
kubectl apply -f db_service.yaml
```

### 4. Развертывание Postgres
```
kubectl apply -f db_volume.yaml
kubectl apply -f db_deployment.yaml
kubectl apply -f db_service.yaml
```

### 5. Развертывание приложения
```
kubectl apply -f bot_deployment.yaml
kubectl apply -f bot_service.yaml
```

### 6. Проверка подов
```
kubectl get pods
```

### 7. Запуск сервиса
```
minikube service bot-app
```
