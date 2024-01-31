# QRKot

Приложение для Благотворительного фонда поддержки котиков QRKot.
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

# Технологии

Python
FastAPI
SQL Alchemy

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Sergey-K2/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

- Если у вас Linux/macOS

  ```
  source venv/bin/activate
  ```

- Если у вас windows

  ```
  source venv/scripts/activate
  ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API досупна по адресам:

Swagger: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

## Автор:

Сергей Козлов
GitHub: [Sergey-K2](https://github.com/Sergey-K2)
