FROM python:3.6-slim
COPY . /gdsc-yonsei
RUN pip install --upgrade pip
WORKDIR /gdsc-yonsei
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y nginx
RUN pip3 install gunicorn
RUN cp manage /etc/nginx/sites-available/manage
CMD [ "/bin/bash", "docker-entry.sh"]



