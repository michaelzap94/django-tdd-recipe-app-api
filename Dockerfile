FROM python:3.7-alpine
LABEL Michael Zapata

# Environmen variable: PYTHONUNBUFFERED 1 (Tells python to run in unbufferd mode, so it doesn't buffer the outputs, and prints them directly)
ENV PYTHONUNBUFFERED 1

#copy from our requiresments.txt file anc paste it to the DOCKER image requirements.txt
COPY ./requirements.txt/ requirements.txt

# POSTGRESS-------------------------------------------------------------------------
#Install postgresql client
RUN apk add --update --no-cache postgresql-client
# --virtual: sets up an alias for our dependencies that we can use to remove them later
#.tmp-build-deps: temporal build dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
#-------------------------------------------------------------------------

#Take the requirements file from DOCKERFILE we just copied and install the requirements
RUN pip install -r /requirements.txt

#Create an empty folder /app within the DOCKER image directory
RUN mkdir /app
#Switch to /app in DOCKER image as default-index
WORKDIR /app
#copies from our local machine the /app folder to the /app folder in Docker image
COPY ./app /app

#FOR SECURITY, so we don't run the APP using the ROOT account(Scopes the whole project)
#create a user ("user") that will RUN the app using Docker: a.eg: RUN adduser -D Michael
RUN adduser -D user
#Switch Docker to this user
USER user