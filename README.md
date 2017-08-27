# TDDWithPythonExample.


## Description:
Simple calculator application implemented in TDD concept. 
All tests are synchronized with Travis CI - https://travis-ci.org/MaBlaGit/TDDWithPythonExample

### Tests were implemented and run on:

* System: Linux Ubuntu 16.04 LTS
* Python: 3.5.2
* nose 1.3.7
* rednose 1.2.2
* pylint 1.7.2

### To Run Tests - Linux Ubuntu way:

1.Clone/Download https://github.com/MaBlaGit/TDDWithPythonExample

2.Install __virtualenvwrapper__
```
 $ pip install virtualenvwrapper
```
3.Run virtualenvwrapper and create hermetic virtualenv for the project

```
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv --python=/usr/bin.python3.5 name-of-virtualenv
$ workon name-of-virtualenv
```

4.Go to  __TDDWithPythonExample__ folder and project to the PYTHONPATH of current active virtualenv

```
$ add2virtualenv .
```
5.Install requred modules

```
$ make deps
```
### Running tests

In order to run tests, go to  __TDDWithPythonExample__ folder run command
```
$ python3 -m unittest discover
```
In order to run __docstring__ tests:
```
$ make docstring_test
```
To run __pylint__ code analysis
```
$ make pylint_tests
$ make pylint_app
```
