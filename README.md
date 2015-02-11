# djangorestframework-client-gen

[![build-status-image]][travis]
[![pypi-version]][pypi]

## Overview

Automatically generate Python client SDK skeleton using your existing Django Rest Framework logic.

## Requirements

* Python (2.7, 3.3, 3.4)
* Django (1.6, 1.7)
* Django REST Framework (2.4.3, 2.4.4, 3.0-beta)

## Installation

Install using `pip`...

```bash
$ pip install djangorestframework-client-gen
```

## Example

To get started making your own SDK, you can do one of two things.

```
$ ./manage.py generatesdk
```

Follow the prompts.

## Tutorial

If you want to try the tutorial, which is based upon the DRF tutorial
(https://github.com/tomchristie/rest-framework-tutorial), do the following:

```
$ git clone https://github.com/tomchristie/rest-framework-tutorial.git
$ cd rest-framework-tutorial
$ 
```

Add 

TODO: Write example.

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```


[build-status-image]: https://secure.travis-ci.org/kevinlondon/django-rest-framework-client-gen.png?branch=master
[travis]: http://travis-ci.org/kevinlondon/django-rest-framework-client-gen?branch=master
[pypi-version]: https://pypip.in/version/djangorestframework-client-gen/badge.svg
[pypi]: https://pypi.python.org/pypi/djangorestframework-client-gen