# Django Rest Framework Client SDK Generator

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

(Note: This does not work... yet)
```bash
$ pip install drf-client-generator
```

## Example

To get started making your own SDK, you can do one of two things.

You can try the quickstart (below) or run it against your own code. Your
choice!

## Quickstart

If you want to try the quickstart, which is based upon the DRF quickstart
(http://www.django-rest-framework.org/tutorial/quickstart/), do the following:

```
$ git clone https://github.com/kevinlondon/django-rest-framework-quickstart.git
$ cd rest-framework-quickstart
$ pip install -r requirements.txt
$ python manage.py makesdk
```

...and follow the prompts. Once it's done, you should have a new folder 
with everything you'd need for the client SDK.

## Using it in your own SDK

First, be sure to install the library first (as above). Then, in your
`settings.py` file, add `drf_client_generator` to your installed apps, like so:

```
INSTALLED_APPS = (
    . . .
    'drf_client_generator',
)
```

Then, as above, to create the SDK:

`$ ./manage.py makesdk`

.. and follow the prompts.


## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ py.test
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
