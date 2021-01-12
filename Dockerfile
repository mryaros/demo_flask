#FROM continuumio/miniconda3
#
#WORKDIR /app
#
## Create the environment:
#COPY environment.yml .
#RUN conda env create -f environment.yml
#
## Make RUN commands use the new environment:
#SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
#
## Make sure the environment is activated:
#RUN echo "Make sure flask is installed:"
#RUN python -c "import flask"
#
## The code to run when container is started:
#COPY app.py .
#COPY logic.py .
##COPY /demo_flask .
#ENV FLASK_APP app.py
##ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "app.py"]
#ENTRYPOINT ["python", "-m", "flask", "run"]
FROM python:3.8-alpine

EXPOSE 5000

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
#CMD ['app.py']