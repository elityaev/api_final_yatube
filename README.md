<h1 align="center">Yatube</h1>

<h2 align="center">
  
  ![logo](https://github.com/elityaev/api_final_yatube/raw/master/yatube_api/static/YT.png)
  
</h2>

<h3 align="center">Описание</h3>

**Yatube**  - это социальная сеть для публикации личных дневников, работающая через API. 
Аутентифицированный пользователь может:
* просматривать все имеющиеся посты, создавать, редактировать и удалять свои посты 

http://127.0.0.1:8000/api/v1/posts/

http://127.0.0.1:8000/api/v1/posts/{id}

* просматривать комментарии к постам, создавать новые, редактировать и удалять свои комментарии

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

* просматривать список сообществ и информацию о конкретном сообществе

http://127.0.0.1:8000/api/v1/groups/

http://127.0.0.1:8000/api/v1/groups/{id}/

* подписаться на других авторов и просматривать их список

http://127.0.0.1:8000/api/v1/follow/

Анонимным пользователям информация доступна только для чтения. Подписка на авторов постов 
анонимам не доступна.

<h3 align="center">Аутентификация</h3>

Аутентификация происходит по JWT-токену.

Доступные эндпоинты:
- Получение JWT-токена - http://127.0.0.1:8000/api/v1/jwt/create/
- Обновление JWT-токена - http://127.0.0.1:8000/api/v1/jwt/refresh/
- Проверка JWT-токена - http://127.0.0.1:8000/api/v1/jwt/verify/


<h3 align="center">Как запустить проект</h3>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/elityaev/api_final_yatube.git
api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
.\venv\Scripts\activate
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

<h3 align="center">Пример запроса</h3>

Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены
http://127.0.0.1:8000/api/v1/posts/
Запрос:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Ответ:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
<h3 align="center">**Подробная документация по проекту - http://127.0.0.1:8000/redoc/**

