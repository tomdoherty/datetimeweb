FROM python:3

EXPOSE 7000

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./web.py", "--port", "7000", "--dateendpoint", "date:7001", "--timeendpoint", "time:7002" ]
