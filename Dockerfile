FROM python:3.6

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /application/requirements.txt

WORKDIR /application

COPY . /application

# install requirements
RUN pip3 install -r requirements.txt

# Run application.py when the container launches
CMD ["gunicorn", "application:app"]