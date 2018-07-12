FROM python:3

LABEL maintainer="Alfred See <alfred.see@intellihr.com.au>"

ARG BUILD_ENV=development
ARG WORKDIR="/var/task"
ARG VENVDIR="/var/venv"
ARG DOCKERDIR="./.docker"

WORKDIR ${WORKDIR}

RUN python3 -m venv ${VENVDIR}

ADD . .

RUN /bin/bash -c "source ${VENVDIR}/bin/activate && \
    pip install --upgrade pip && \
    pip install -r ${DOCKERDIR}/requirements/${BUILD_ENV}.txt && \
    python -m nltk.downloader punkt stopwords wordnet averaged_perceptron_tagger && \
    deactivate"

ENTRYPOINT [ "./.docker/scripts/entrypoint.sh" ]
