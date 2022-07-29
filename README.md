# Fast api project starter 


<p>Install all required packages</p>

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

