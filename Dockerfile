FROM python:3.6-slim
COPY . /gdsc-yonsei
RUN pip install --upgrade pip
WORKDIR /gdsc-yonsei
RUN pip3 install -r requirements.txt
RUN sudo apt-get install nginx
RUN pip3 install gunicorn
RUN sudo cp manage /etc/nginx/sites-available/manage
CMD [ "/bin/bash", "docker-entry.sh"]



