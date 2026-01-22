# CURSO DJANGO

```cmd
python -m venv .venv
pip install django
django-admin startproject myproject .
python manage.py runserver 3000
python manage.py --help
```

Un proyecto de Django está conformado por varias aplicaciones y middlewares

Cada app puede tener varias funcionalidades diferentes

Crear aplicaciones con cualquier nombre
`python manage.py startapp cualquier_nombre`

## Migraciones

```cmd
python manage.py makemigrations
python manage.py migrate
```

## CRUD desde shell de manage.py

`py manage.py shell`

```py
from myapp.models import Project, Task
# Crear instancia
p = Project(name="aplicacion movil")
p.save()
Project.objects.all()
Project.objects.get(id=1)
p = Project.objects.get(name="aplicacion movil")

# Consultar tareas vinculadas a un proyecto
p.task_set.all()

# Crear tarea con foreignkey
p.task_set.create(title="nueva tarea", description="tarea creada")
# Obtener una sola
p.task_set.get(id=1)

# Filtrar
Project.objects.filter(name__startswith="aplicacion")
p = Project.objects
p.filter(name__starswith="aplicacion")
```
