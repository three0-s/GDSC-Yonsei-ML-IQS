FROM python:3.6-slim
COPY . /gdsc-yonsei
RUN pip install --upgrade pip
WORKDIR /gdsc-yonsei
RUN pip3 install -r requirements.txt
# RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install build-essential python3.6-dev
RUN pip3 install uwsgi 
# RUN apt-get install -y nginx
# RUN apt install -y uwsgi
# RUN apt install -y uwsgi-plugin-python3
# RUN cp manage /etc/nginx/sites-available/manage
CMD [ "/bin/bash", "docker-entry.sh"]



