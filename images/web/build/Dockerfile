FROM python:3

EXPOSE 7000
ENV PORT=7000
ENV DATEENDPOINT=date
ENV TIMEENDPOINT=time

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec python ./web.py --port $PORT --dateendpoint $DATEENDPOINT --timeendpoint $TIMEENDPOINT
