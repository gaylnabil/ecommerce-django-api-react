# base image 
FROM python:3.10 as development

# set environment variables  
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# setup environment variable  
# ENV DockerHOME=./ecommerce_django_api

# set work directory  
# RUN mkdir -p $DockerHOME 

# Working directory 
WORKDIR /ecommerce_django_api

# install dependencies  
RUN pip install --upgrade pip 


# RUN apt install python-is-python3
COPY ./ ./
# run this command to install all dependencies  
RUN pip install -r requirements.txt

# port where the Django app runs  
EXPOSE 8000  

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
# CMD ["python3","manage.py","runserver"]