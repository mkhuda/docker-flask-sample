# Use an official Python runtime as a parent image
FROM python:2.7-slim

RUN pip install Flask
RUN pip install pyyaml
RUN pip install ua-parser
RUN pip install user-agents

# Copy the current directory contents into the container at /app
ADD . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
