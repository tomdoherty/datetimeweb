VERSION = latest

lint:	web.py
	flake8 web.py

build:	Dockerfile web.py
	docker build -t datetimeweb/web:$(VERSION) .

run:	build
	docker run --rm -i -t -p 7000:7000 datetimeweb/web:$(VERSION)
