FROM python:latest

USER root

RUN adduser workshop

RUN python -m ensurepip --upgrade --user && \
    python -m pip install --upgrade pip --user && \
    python -m pip install --upgrade virtualenv --user && \
    apt-get update && \
    apt install nodejs npm golang -y && \
    npm install -g aws-cdk && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

USER workshop
