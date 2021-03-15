FROM python:3

LABEL maintainer="Matteo Sgalaberni <sgala@sgala.com>"

VOLUME /app/

#RUN cd /app/ && ls -la

COPY dummy.py .

ADD resources_dist/icon.png /dist/


WORKDIR /app/backend/

COPY requirements.txt ./

RUN mkdir -p /dist/am_charts/ && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
