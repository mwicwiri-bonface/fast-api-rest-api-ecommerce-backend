# Fast api project starter 

project structure

```tree
├── app
│   ├── __init__.py
│   ├── helpers.py
│   ├── models.py
│   ├── schemas.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── emails.py
│   ├── settings.py
│   └── settings.ini
├── main.py
├── README.md
├── requirements.txt

```

Install all required packages

```commandline
pip install -r requirements.txt
```

initiate alembic
```commandline
alembic init
```

makemigrations
```commandline
alembic revision --autogenerate -m "initial migration"
```

migrate
```commandline
alembic upgrade head
```

runserver
```commandline
uvicorn main:app --reload
```

[]: # Language: python
[]: # Path: main.py

