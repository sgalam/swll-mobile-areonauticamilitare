FROM python:3

LABEL maintainer="Matteo Sgalaberni <sgala@sgala.com>"

VOLUME /app/

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY dummy.py .

RUN pip install --no-cache-dir -r requirements.txt

 
CMD [ "python", "./dummy.py" ]
