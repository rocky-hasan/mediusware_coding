# mediusware_coding
coding test

-Here first create repo: div.0.0.1 </br>
-then clone it.
-then create venv: python -m venv env
and run the env. Inte env install django,pillow , rest_framework,psychopg2
-all are same wait : pip install django/pillow/rest_framework/psychopg2.
-create project
-django-admin createproject Task_Manager
and create app: python manage.py startapp tasks
-tasks app install on project setting, also install rest_framework.
-url connect  from main project.
-connect postgresql in the setting
-in the app models fild create. then migrate it.
-first: python manage.py makemigrations
-then migrate: python manage.py migrate
-create superuser: python manage.py createsuperuser
-then CRUD which is class Based 
-create API 
run the project : python manage.py runserver

