# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app/

# RUN python App/manage.py collectstatic --noinput

# CMD ["gunicorn", "--chdir", "App", "app.wsgi:application", "--bind", ":8000"]

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python App/manage.py collectstatic --noinput

CMD ["gunicorn", "--chdir", "App", "app.wsgi:application", "--bind", "0.0.0.0:8000"]

