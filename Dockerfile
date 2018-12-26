FROM python:3.6

WORKDIR /application

COPY . /application

# install requirements
RUN pip3 install -r requirements.txt

# Run application.py when the container launches
CMD ["gunicorn", "application:app"]