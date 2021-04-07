FROM python:3
WORKDIR /usr/src/app
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile
COPY app .
CMD python3 main.py $APIKEY 
