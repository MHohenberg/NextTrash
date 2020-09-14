install:
	pip3 install ics
	pip3 install pyinstaller
	rm -rf dist

	pyinstaller nexttrash.py --name=nexttrash --onefile --add-data ~/.local/lib/python3.8/site-packages/ics/:ics --add-data ~/.local/lib/python3.8/site-packages/arrow/:arrow

	mkdir -p ~/.nexttrash
	cp dist/nexttrash ~/bin/nexttrash
	cp config.template ~/.nexttrash/config.ini

clean:
	rm -rf build
	rm -rf dist
	rm *spec
	rm -rf  __pycache__
