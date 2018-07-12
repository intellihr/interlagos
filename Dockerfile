FROM python:3-alpine

LABEL maintainer="Alfred See <alfred.see@intellihr.com.au>"

ARG WORKDIR="/var/task"

WORKDIR ${WORKDIR}

RUN apk add --upgrade make && rm -rf /var/cache/apk/*

ADD requirements.txt .
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt stopwords wordnet averaged_perceptron_tagger

ADD . .

ENTRYPOINT make "$@"
