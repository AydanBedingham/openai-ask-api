FROM python:3.9

COPY ./docker/docker-requirements.txt /docker-requirements.txt
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN pip install -r /docker-requirements.txt

COPY ./openai-ask-api /openai-ask-api
RUN pip install -r /openai-ask-api/requirements.txt

WORKDIR /
EXPOSE 5000

ENTRYPOINT ["sh", "./entrypoint.sh"]
