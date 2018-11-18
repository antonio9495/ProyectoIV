FROM python:3.6

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /application/requirements.txt

WORKDIR /application

COPY . /application

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

# Run app.py when the container launches
CMD ["python3", "app.py"]