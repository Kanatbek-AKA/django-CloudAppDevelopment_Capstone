FROM python:3.8.2
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1
RUN apt-get update && apt-get install -y netcat nano
ENV APP=/app
#Choose the workdir
WORKDIR $APP
COPY requirements.txt .
COPY entrypoint.sh .
#Install the requirements
RUN pip3 install -r requirements.txt
RUN python -m pip install -U pip --user
# Copy the rest of the file
COPY . APP
EXPOSE 8000
RUN chmod +x /app/entrypoint.sh
# Create bin folder in your app ?
# ENTRYPOINT["/bin/bash","/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi"]

