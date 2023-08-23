FROM python:3.11.4-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /code/

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

# Create a non-root user
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Change ownership and permissions
RUN chown -R django-user:django-user /code/
RUN chmod -R 755 /code/

USER django-user