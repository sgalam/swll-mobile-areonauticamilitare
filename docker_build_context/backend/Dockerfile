FROM python:3

LABEL maintainer="Matteo Sgalaberni <sgala@sgala.com>"

#RUN cd /app/ && ls -la


WORKDIR /app/backend/

COPY dummy.py /

COPY init.sh /
COPY init_dev.sh /

COPY requirements.txt ./

RUN chmod u+x /init*.sh && pip install --no-cache-dir -r requirements.txt

CMD [ "/init.sh" ]
