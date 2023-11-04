FROM python:3.9-slim
COPY . /app
RUN pip3 install flask
WORKDIR /app 
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8888"]


