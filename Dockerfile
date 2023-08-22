FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .
#COPY . /code/
#COPY android /code/
#COPY main /code/
#COPY media /code/
#COPY myworld /code/
#COPY staticfiles /code/
#COPY users /code/
#COPY yayb2 /code/
#COPY manage.py /code/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"] 