FROM python:3
MAINTAINER Ajith Kattil

# Creating Application Source Code Directory
RUN mkdir -p /jfrog_sample_demo/src

# Setting Home Directory for containers
WORKDIR /jfrog_sample_demo/src

# Installing python dependencies
COPY requirements.txt /jfrog_sample_demo/src
RUN pip install --no-cache-dir -r requirements.txt

# Copying src code to Container
COPY . /jfrog_sample_demo/src

# Application Environment variables
ENV APP_ENV development

# Exposing Ports
EXPOSE 5035

# Running Python Application
CMD ["python", "artifact_query.py"]
