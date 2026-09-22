# SQLAlchemy `database.py` Explained

This file configures SQLAlchemy for the application. It does not create tables or run queries yet.

```python
from sqlalchemy import create_engine
```

Imports `create_engine`, which creates an **engine**.

An engine knows how to connect to the selected database and send SQL to it.

```python
from sqlalchemy.orm import sessionmaker, declarative_base
```

- `sessionmaker`: creates a factory for database sessions.
- `declarative_base`: creates a base class for database-table models.

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
```

This specifies the database:

- `sqlite` means SQLite database.
- `./todos.db` means it is stored in a file named `todos.db`.

```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
```

Creates the engine.

`check_same_thread=False` is a setting commonly needed when using SQLite with FastAPI, since FastAPI can handle requests on different threads.

```python
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

Creates a **session factory**.

`SessionLocal` is not a session yet. It is a reusable recipe for creating sessions:

```python
db = SessionLocal()
```

Here, `db` is an actual session. It uses the engine because of:

```python
bind=engine
```

A session is where you do database work:

```python
db.add(todo)
db.commit()
db.query(Todo).all()
db.close()
```

```python
Base = declarative_base()
```

Creates a special parent class for every database-table model.

In `models.py`, this project has:

```python
class Todos(Base):
    __tablename__ = "todos"
```

Inheriting from `Base` tells SQLAlchemy:

> This Python class represents a database table.

```text
Base
  ^
  |
Todos model
  ^
  |
todos table
```

`Base` collects definitions from all model classes. Later, this can create their tables:

```python
Base.metadata.create_all(bind=engine)
```

That means:

> Create all tables described by classes that inherit from `Base`, using this engine.

## Relationship Between Them

```text
SQLite file: todos.db
        ^
        |
      engine
        ^
        |
 SessionLocal factory
        ^
        |
 db = SessionLocal()
        ^
        |
 Query, add, update, commit
```

```text
Base
  ^
  |
Todos model
  ^
  |
todos table
```

The overall pattern is reusable, but some details, especially the SQLite-specific `check_same_thread=False`, change depending on the database you use.