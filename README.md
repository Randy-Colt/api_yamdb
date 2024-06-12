### Описание

**YaMDb** - это бэкенд для сайта, на котором собраны различные произведения: книги, фильмы, музыка. Пользователи могут оставлять отзывы на произведения и ставить ему оценку, а также комментировать отзывы других пользователей.


### Стек технологий

Архитектура проекта - REST API

*Основные фреймворки и библиотеки*:

- Django 3.2
- Django Rest Framework 3.12
- PyJWT 2.1.0
- Simple JWT 5.3.1


### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Randy-Colt/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

Для Linux/macOS:
```
python3 -m venv env

source env/bin/activate
```

Для Windows:
```
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
Для Linux/macOS:
```
python3 -m pip install --upgrade pip
```
Для Windows:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```


### Документация

Документация API доступна по адресу: `http://127.0.0.1:8000/redoc/`


### Примеры запросов

Получение списка всех произведений:

*request:*
```
api/v1/titles/
```

*response:*
```
{
  "count": 1,
  "next": "http://api.example.org/accounts/?offset=400&limit=5",
  "previous": "http://api.example.org/accounts/?offset=200&limit=5",
  "results": [
    {
      "id": 0,
      "name": "Побег из Шоушенка",
      "year": 1994,
      "raiting": 10,
      "description": "Культовый фильм о побеге из тюрьмы.",
      "genre": "драма",
      "category": "movie"
    }
  ]
}
```

Получение всех отзывов к произведению:

*request:*
```
/api/v1/titles/{title_id}/reviews/
```

*response:*
```
{
  "count": 1,
  "next": "http://api.example.org/accounts/?offset=400&limit=5",
  "previous": "http://api.example.org/accounts/?offset=200&limit=5",
  "results": [
    {
      "id": 0,
      "text": "Так себе",
      "author": "Critic",
      "score": 1,
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
```