# API (FastAPI)

Сервис анализа тональности: эндпоинт `POST /predict/` с телом `{"text": "..."}`.

Зависимости: **`requirements.txt` в этой папке**.

**Конфигурация:** скопируйте **`.env.example`** → **`.env`**. Параметры **`API_HOST`**, **`API_PORT`**, **`API_RELOAD`** читает скрипт **`run.py`**. Для фронта задайте тот же хост и порт в **`streamlit/.env`** (`API_BASE_URL`).

---

## Только бэкенд (без Streamlit)

Подходит, если нужен только API (например для вызовов из Postman, другого сервиса или только для проверки `/docs`).

Из каталога **`fastapi/`**:

```bash
python -m venv .venv
```

**Windows:** `.venv\Scripts\activate`  
**Linux / macOS:** `source .venv/bin/activate`

```bash
pip install -r requirements.txt
copy .env.example .env
```

(На Linux/macOS: `cp .env.example .env`.)

**Запуск** (из любого каталога — скрипт сам перейдёт в `fastapi/`):

Из **корня** репозитория:

```bash
python fastapi/run.py
```

Из папки **`fastapi/`**:

```bash
python run.py
```

Документация после старта: http://127.0.0.1:8000/docs (путь зависит от `API_HOST` и `API_PORT` в `.env`).

---

## Полный проект: бэкенд + фронт одним окружением

Из корня:

```bash
pip install -r fastapi/requirements.txt -r streamlit/requirements.txt
```

Дальше порядок запуска — **ReadMe.MD** в корне проекта.
