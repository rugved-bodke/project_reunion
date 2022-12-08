FROM ubuntu:20.04
ENV TZ=Asia/Kolkata
ENV PGDATA=/var/lib/postgresql/
ENV DB_USER=admin_user
ENV DB_PASSWORD=W7zIklRbeldjFDlmkPOwL3OHZ4m8ltk3
ENV DB_HOST=dpg-ce8udqpa6gdhr71lkrj0-a
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update -y
RUN apt-get upgrade -y
# installing system dependancies
RUN apt-get install -y python3.8 python3.8-dev build-essential python3-setuptools vim postgresql postgresql-contrib python3-pip libpq-dev python3-psycopg2
# updating pip to latest vesion
RUN python3 -m pip install --upgrade pip
COPY . /.project_reunion
WORKDIR /.project_reunion
EXPOSE 8000
EXPOSE 5432
RUN python3.8 -m pip install -r /.project_reunion/requirements.txt
RUN pytest -s
ENTRYPOINT [ "/.project_reunion/start_server.sh"]
