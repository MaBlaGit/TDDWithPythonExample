deps:
	pip install --upgrade -r requirements.txt
docstring_test:
	nosetests --rednose --with-doctest -v
pylint_tests:
	pylint tests

pylint_app:
	pylint calculator_app
