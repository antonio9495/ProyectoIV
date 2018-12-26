FROM python:3.6

WORKDIR /application

COPY ./src /application/src
COPY ./data /application/data
COPY ./application.py /application/application.py
COPY ./requirements.txt /application/requirements.txt


# install requirements
RUN pip3 install -r requirements.txt

# Run application.py when the container launches
CMD ["gunicorn", "application:app"]