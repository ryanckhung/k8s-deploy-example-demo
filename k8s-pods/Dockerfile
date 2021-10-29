FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./main.py .
EXPOSE 80
ENTRYPOINT [ "python", "main.py" ]
CMD [ "HELLO WORLD" ]
