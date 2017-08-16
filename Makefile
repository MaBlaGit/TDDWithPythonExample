deps:
	pip install pylint
docstring_test:
	python3 calculator_app/calculator_app.py -v
test:
	python3 -m unittest discover -v

pylint_tests:
	pylint tests

pylint_app:
	pylint calculator_app
