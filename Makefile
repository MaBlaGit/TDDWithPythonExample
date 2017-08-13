deps:
	pip install pylint
test:
	python3 -m unittest discover

pylint_tests:
	pylint tests

pylint_app:
	pylint calculator_app
