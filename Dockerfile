FROM python:3.9.23-trixie
LABEL authors="yunhwan"

RUN  apt update &&\
     apt install -y --no-install-recommends bash-completion vim &&\
     mkdir /data_analysis &&\
     rm -rf /var/lib/apt/lists/* /var/cache/apt/*

WORKDIR /data_analysis

RUN python3 -m venv venv

VOLUME ["/data_analysis"]

CMD ["sleep", "infinity"]