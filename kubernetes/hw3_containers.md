# Контейнеризация и оркестрация: ЛР 3 - Kubernetes

### Требования:
- Осуществить махинации над манифестами из примера
- Для постгреса перенести POSTGRES_USER и POSTGRES_PASSWORD из конфигмапы в секреты (очевидно, понадобится новый манифест для сущности Secret)
- Для некстклауда перенести его переменные (NEXTCLOUD_UPDATE, ALLOW_EMPTY_PASSWORD и проч.) из деплоймента в конфигмапу (очевидно, понадобится новый манифест для сущности ConfigMap)
- Для некстклауда добавить Liveness и Readiness пробы
- Файлы нужных манифестов
- README.md с описанием хода работы и скриншотами
- Ответы на доп. вопросы

### Запуск minikube
![Запуск minikube](https://github.com/hilkovich/children_diary/blob/hw3_containers/kubernetes/images/image_1.png)

### Проверка контейнера и файла конфигурации
![Проверка контейнера и файла конфигурации](https://github.com/hilkovich/children_diary/blob/hw3_containers/kubernetes/images/image_2.png)

### Создание объектов из манифестов
![Создание объектов из манифестов](https://github.com/hilkovich/children_diary/blob/hw3_containers/kubernetes/images/image_3.png)

### Проверка созданных ресурсов
![Проверка созданных ресурсов](https://github.com/hilkovich/children_diary/blob/hw3_containers/kubernetes/images/image_4.png)

### Проверка логов nextcloud
![Проверка логов nextcloud](https://github.com/hilkovich/children_diary/blob/hw3_containers/kubernetes/images/image_5.png)

### Создание service для nextcloud c перенаправлением портов
![Создание service для nextcloud c перенаправлением портов](https://github.com/hilkovich/children_diary/blob/hw3_containers/kubernetes/images/image_6.png)

## Вопросы
1. **Важен ли порядок выполнения этих манифестов? Почему?**

2. **Что (и почему) произойдет, если отскейлить количество реплик postgres-deployment в 0, затем обратно в 1, после чего попробовать снова зайти на Nextcloud?**
