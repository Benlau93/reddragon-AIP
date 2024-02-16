# Use the official Python image from the Docker Hub
FROM python:3.12-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
RUN pip install --upgrade pip
COPY ./requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the current directory contents into the container at /app
COPY . .