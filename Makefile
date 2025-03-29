
install:
	pip install -r requirements.txt

lint:
	pylint main.py

run:
	python main.python

test:

clean:
	rm -rf __pycache__
	rm -rf *.pyc