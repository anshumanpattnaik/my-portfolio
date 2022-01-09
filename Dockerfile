FROM python:3.9.6-alpine

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME=/home/app
ENV APP_HOME=$HOME/web

# create non-root user
RUN addgroup -S app && adduser -S app -G app

# create work directory
RUN mkdir -p $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN chown -R 755 $APP_HOME/staticfiles
WORKDIR $APP_HOME

# copy project
COPY . $APP_HOME

# change all files ownership to the app user
RUN chown -R app:app $APP_HOME

# Install dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install --upgrade pip
RUN pip3 install wheel
RUN pip3 install -r requirements.txt

RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

ENTRYPOINT ["/home/app/web/entrypoint.sh"]

USER app