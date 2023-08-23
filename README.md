# rick-and-morty
# How to run

### How to rch: 
- Create venv: `python -m venv venv`
- Activate it: `source venv/bin/activate`
- Install requirements: `pip install -r requirements. txt`
- Create new Postgres DB & User
- Copy .env.sample -> .end and populate it with proper variables
- Run migrations: `python manage.py migrate`
- Run Redis Server: `docker run -d -p 6379:6379 redis`
- Run celery worker for tasks handling: `celery -A rick_and_morty worker -1 INFO`
- Run celery beat for task scheduling: `celery -A rick_and_morty beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
- Create schedule for running sync in DB
- Run app: `python manage.py runserver`
- 