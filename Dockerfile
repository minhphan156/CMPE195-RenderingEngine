FROM python:3.6-alpine 

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# open the port
EXPOSE 3003

ENTRYPOINT ["python"]

# run the app
CMD ["app.py"]