FROM python:3.9.5
WORKDIR /opt/sde/src/loader
ENV PYTHONPATH=/opt/sde
COPY ./containers/loader/requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["tail", "-f", "/dev/null"]