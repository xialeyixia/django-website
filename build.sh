#!/bin/bash

# 设置所需环境
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export PATH=/usr/local/bin:/usr/bin:/bin

# 切换到应用目录
cd /opt/code/django-website

# 启动应用
exec /usr/bin/python3 manage.py runserver 0:80
