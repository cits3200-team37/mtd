run:
	python3 app.py

docs:
	cd Documentation && mkdocs serve

setup-mac: requirements.txt
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

clean:
	rm -rf venv

lint:
	flake8  --ignore=E501,E203,W503,W504 --per-file-ignores=__init__.py:F401 $(DIRECTORY)

test:
	pytest


.PHONY: docs run
