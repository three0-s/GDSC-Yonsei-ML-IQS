FROM python:3.6-slim
COPY . /gdsc-yonsei
RUN pip3 install -r requirements.txt
WORKDIR /gdsc-yonsei

CMD ["python3", "manage.py", "db", "init", \
     "python3", "manage.py", "db", "migrate", "--message", "init", \
     "python3", "manage.py", "db", "upgrade", \
     "python3", "manage.py", "run"]


