FROM python:3.11

RUN apt-get update

# UID,GIDは`id`コマンドで確認したものを使うべきらしい
ARG USERNAME=pyuser
ARG GROUPNAME=pyuser
ARG UID=1001
ARG GID=1001
ARG WORKDIR=/usr/src/app

ENV TZ Asia/Tokyo
ENV PYTHONPATH ${WORKDIR}

RUN groupadd -g ${GID} ${GROUPNAME} && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} ${USERNAME}

RUN mkdir -p ${WORKDIR}
RUN chown -R ${UID}:${GID} ${WORKDIR}

ENV PATH /home/${USERNAME}/.local/bin:$PATH

USER ${USERNAME}
WORKDIR ${WORKDIR}

RUN pip install --upgrade --user pip

COPY pyproject.toml ./

RUN pip install --user poetry
RUN poetry config virtualenvs.create false
RUN alias poetry="sudo /root/.local/bin/poetry"
RUN poetry install --no-root

EXPOSE 8888