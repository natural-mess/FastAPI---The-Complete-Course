# Lesson notes

Create new Python venv:
```bash
python -m venv <venv_name>
```

Change Interpreter and Virtual Environment to `<venv_name>`.

Activate venv:
```bash
<venv_name>\Scripts\activate
```

Deactivate venv:
```bash
deactivate
```

Run FastAPI
```bash
uvicorn <python_filename>:<fastapi_instance> --reload
```

or

```bash
fastapi run <python_filename>.py
```

or

```bash
fastapi dev <python_filename>.py
```
