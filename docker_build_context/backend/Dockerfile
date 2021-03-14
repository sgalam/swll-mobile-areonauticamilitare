FROM python:3

LABEL maintainer="Matteo Sgalaberni <sgala@sgala.com>"

VOLUME /app/
VOLUME /dist/

WORKDIR /usr/src/app

MKDIR /disk/am_charts/

COPY requirements.txt ./

COPY dummy.py .

RUN mkdir -p /disk/am_charts/ && pip install --no-cache-dir -r requirements.txt

 
CMD [ "python", "./dummy.py" ]
