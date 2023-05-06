FROM python:3.8.2

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

RUN apt-get update && apt-get install -y netcat nano

ENV APP=/app

#Choose the workdir
WORKDIR $APP

COPY requirements.txt .
COPY entrypoint.sh .
COPY README.md .
COPY LICENSE .

#Install the requirements
RUN pip3 install -r requirements.txt && python -m pip install -U pip --user

# Copy the rest of the file
COPY . APP

EXPOSE 5000

RUN chmod +x /app/entrypoint.sh

# Create bin folder in your app ?
#ENTRYPOINT["/bin/bash","/app/entrypoint.sh"]

CMD python APP/server/manage.py runserver 5000

# if you use this "djangobackend.wsgi"], throws module not found error | Failed to parse 'server.manage' as an attribute name or function call.  
#["gunicorn", "APP:server.manage", "--preload", "--bind", "127.0.0.1:5000", "--workers", "3"] 
#CMD ["gunicorn", "app:application", "--preload", "--bind", "127.0.0.1:5000", "--workers", "3", "--threads", "3"]
