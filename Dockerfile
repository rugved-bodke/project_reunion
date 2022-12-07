FROM ubuntu:20.04
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update -y
RUN apt-get upgrade -y
# installing system dependancies
RUN apt-get install -y python3.8 python3.8-dev build-essential python3-setuptools vim postgresql postgresql-contrib python3-pip libpq-dev python3-psycopg2
# updating pip to latest vesion
RUN python3 -m pip install --upgrade pip
COPY . /.project_reunion
WORKDIR /.project_reunion
RUN python3.8 -m pip install -r /.project_reunion/requirements.txt
