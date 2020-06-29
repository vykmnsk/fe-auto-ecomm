pytest-seleniumbase
===================
Browser UI test automation framework

setup
----- 

seup virtual environment

	python3 -m venv ./venv
	chmod +x venv/bin/activate
	source venv/bin/activate


install python libs

	pip install --upgrade pip
	pip install -r requirements.txt


install selenium web drivers

	seleniumbase install chromedriver latest
	seleniumbase install firefoxdriver

run
---
Set SuT environment

	source env/prod.sh

	(optionally create .sh files for dev, test, staging, prod in ./env)

Quick Demo (in Chrome)

	pytest tests/search.py --demo

Run all (in Chrome)

	pytest

Run all in FF
	
	pytest --browser=firefox

Run all fast (no UI, same session)

	pytest --headless --reuse-session

debug

	pytest -vv --browser=firefox --last-failed -s --pdb

