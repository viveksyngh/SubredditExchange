# Use official Python3 parent image
FROM python:3-alpine

ADD . .

# Install any needed packages specified in requirements
RUN pip install flask
RUN pip install requests
RUN pip install pyyaml

# Make port 80 available to the world outside this container
EXPOSE 80

# Run SubredditExchange.py to start the servers
CMD ["python", "SubredditExchange.py"]
