FROM python:3.6-slim
COPY . /gdsc-yonsei
RUN pip install --upgrade pip
WORKDIR /gdsc-yonsei
RUN pip3 install -r requirements.txt

CMD [ "/bin/bash", "docker-entry.sh"]



