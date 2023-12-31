# TuneTreasureDRF

## Описание
TuneTreasureDRF - это каталог музыки на базе Django Rest Framework, включающий в себя информацию о исполнителях, альбомах и песнях.

## Основные особенности:
- Обработка песен, появляющихся в нескольких альбомах с разными порядковыми номерами.
- Покрытие проекта тестами (APITestCase).
- Интеграция с Swagger и Redoc для документации.
- Проект упакован в контейнер с помощью Docker и запускается через Docker Compose.
- Используется база данных PostgreSQL.
- Использование сигналов для обновления порядкового номера трека после удаления.
- Код документирован с помощью докстрингов.
- Код оформлен в соответствии с стандартом PEP 8.
- Все секретные данные и ключи хранятся в файле .env для усиления безопасности.
  
## Структура проекта 

- api: Папка с реализацией API и тестами. _Этот модуль содержит все необходимое для обработки запросов к API._
- musical_catalog: Папка с моделями Album, AlbumSong, Artist, и Song. _Содержит основные модели данных для музыкального каталога._
- tune_treasure_drf: Главная папка проекта с настройками. _Здесь содержатся настройки Django-приложения._
- .dockerignore: Файл для исключения файлов и директорий из сборки Docker.
- .env.example: Пример файла с переменными среды для вашего приложения.
- .gitignore: Указывает, какие файлы или директории игнорировать в Git.
- Dockerfile: Инструкции для сборки Docker-образа.
- docker-compose.yml: Файл для определения и запуска многоконтейнерных Docker-приложений.
- requirements.txt: Список зависимостей Python для проекта.

## Запуск проекта
1. В корневой папке проекта создайте файл .env, используя в качестве образца файл env.example.
2. В корневой папке проекта выполните:
   `docker-compose up`
3. Примените миграции:
   `docker compose run web python manage.py migrate `
4. Создайте суперпользователя:
`docker compose run web python manage.py createsuperuser `

После запуска, проект будет доступен по адресу http://127.0.0.1:8000.

## Эндпоинты 

### Главные URL-адреса:

- API: /api/ (включает в себя все URL-адреса из api.v1.urls)
- Admin: /admin/
- Swagger JSON/YAML: /swagger(.json/.yaml)
- Swagger UI: /swagger/
- Redoc: /redoc/

### URL-адреса API v1:

- Artists: /api/artists/
- Albums: /api/albums/
- Songs: /api/songs/
- Album Songs: /api/album-songs/

### Стек технологий:
- Django REST Framework
- Swagger
- PostgreSQL
- Docker
- APITestCase

### Автор
Tina Kirilenko 📧 Telegram: @Mi_2018

🔗 LinkedIn: linkedin.com/in/iultina
