FROM python:3.6-slim

RUN cd /var/www/app && git init \
    && git remote add origin http://housong:pss123546@git.jiankanghao.net/haiwei/chaos.git

RUN cd /var/www/app
COPY . /var/www/app/

# 配置运行环境
RUN pip install -r requirements.txt
CMD python  /var/www/app/main.py

