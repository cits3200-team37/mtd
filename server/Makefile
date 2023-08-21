run:
	python3 app.py

docs:
	cd Documentation && mkdocs serve

setup-mac: requirements.txt
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

clean:
	rm -rf venv

.PHONY: docs run