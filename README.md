# Запуск
1. Склонировать проект:

```
git clone https://github.com/youngwishes/history.git
```
2. Убедиться, что на машине есть Python (в случае, если его нет - скачать с https://www.python.org/downloads/)
3. Установить зависимости проекта:

```
pip install -r requirements.txt
```
P.S. в проекте находится файл с названием requirements.txt - он хранит нужные библиотеки для работы, перед запуском команды убедитесь, что вы находитесь в директории, которая содержит этот файл
4. Далее - проведение миграци в БД:

```
python manage.py migrate
```

5. Далее - создание супер-пользователя для заполнения БД тестовыми данными:

```
python manage.py createsuperuser
```
6. Последнее - запуск сервера

```
python manage.py runserver
```

- Чтобы посмотреть на сайт - нужно перейти по адресу http://127.0.0.1:8000/
- Чтобы зайти в админку - http://127.0.0.1:8000/admin
