VERSION = latest

lint:	time.py
	flake8 time.py

build:	Dockerfile time.py
	docker build -t datetimeweb/time:$(VERSION) .

run:	build
	docker run --rm -i -t -p 7002:7002 datetimeweb/time:$(VERSION)
