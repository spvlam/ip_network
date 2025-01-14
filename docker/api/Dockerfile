FROM amazon/aws-lambda-python:3.12
RUN dnf install -y shadow-utils tar gzip

RUN pip install --upgrade pip
RUN pip install poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN curl -fsSL https://rpm.nodesource.com/setup_20.x | bash - && dnf install -y nodejs-2:20.11.1-1nodesource.x86_64

RUN npm install -g serverless@3
RUN npm install -g serverless-plugin-warmup@6.2.0
RUN npm install -g serverless-python-requirements@5.3.0
RUN npm install -g serverless-domain-manager@5.6.0
RUN npm install -g @otani.sg/serverless-ssm-helper
RUN npm install -g serverless-scriptable-plugin
RUN npm install -g serverless-build-client
RUN npm install -g serverless-finch@2