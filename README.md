# CommonURL - Сервис сокращения ссылок
CommonURL - это высокопроизводительный RESTful API сервис для сокращения длинных URL-адресов, построенный на FastAPI с использованием PostgreSQL для хранения данных и Redis для кэширования.

Реализован простейший фронт на Jinja2

### Возможности
Сокращение ссылок: Преобразование длинных URL в короткие коды
Редирект: Перенаправление по коротким ссылкам
Статистика: Сбор статистики переходов по каждой ссылке
Кэширование: Redis кэширование

REST API: Полностью документированный Swagger/OpenAPI интерфейс

### Технологический стек
Backend: FastAPI (Python 3.12)
База данных: PostgreSQL 16
Кэширование: Redis 7.4
Миграции: Alembic
Контейнеризация: Docker + Docker Compose
Асинхронность: asyncpg, SQLAlchemy 2.0

## Установка и запуск
Клонируйте репозиторий:
```bash
git clone <your-repo-url>
cd CommonURL
```

Создайте файл окружения:
```bash
cp .env.example .env
```

Настройте переменные окружения в .env:
```env
DB_HOST=database
DB_PORT=5432
DB_NAME=commonurl
DB_USER=admin
DB_PASS=0000
REDIS_URL=redis://redis:6379/0
```

Запустите приложение:
```bash
docker-compose up -d
```

Примените миграции базы данных:
```bash
docker-compose exec commonurl_back_service alembic upgrade head
```

#### Откройте в браузере:
- API документация: http://localhost:7777/docs
- Интерфейс приложения: http://localhost:7777
