VERSION = latest

lint:	date.py
	flake8 date.py

build:	Dockerfile date.py
	docker build -t datetimeweb/date:$(VERSION) .

run:	build
	docker run --rm -i -t -p 7001:7001 datetimeweb/date:$(VERSION)
