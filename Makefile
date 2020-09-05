install:
	pip3 install ics
	mkdir -p ~/.nexttrash
	cp nexttrash.py ~/bin/nexttrash
	cp config.template ~/.nexttrash/config.ini
