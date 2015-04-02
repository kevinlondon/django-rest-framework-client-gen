===============================
{{ name }}
===============================

This is an automatically generated README for the SDK.


Overview
========

This is a helper library to interact with the SDK. 

* Free software: BSD license
* Documentation: https://{{ name }}.readthedocs.org.


Getting Started
===============

1. First, install this package via `$ pip install -e .`
2. If you don't already have the `drf_client` package installed, please do so
   now. It's not on pypi yet (sorry).

Let's access a resource from the API. In order to log in to the API, you'll
want to do something like the following::

    import {{ name }}
    from {{ name }} import {{ collections[0] }}

    {{ name }}.configure({{ login }})
    print({{ collections[0] }}.get())


Available Resources
===================

The following resources are available:

{% for collection in collections %}
* {{ collection }}
{% endfor %}

In each case, the resource may be imported as above. If you'd like to create an
instance of your resource, you can call `.create()` on the resource type and, if
successful, it will return an instance of the resource.


Creating Resources
==================
If, for example, we had a `User` object that took a `first_name` and
`last_name` parameter, we would make one by doing this::

    import thissdk
    from thissdk import users

    thissdk.configure({{ login }})
    my_user = users.create(first_name="Mark", last_name="EMark")
    print(my_user)

*Again, please do not try this. This is an example. I'll make this better.*


Logging In
==========

If something went wrong above and we didn't capture your login type, there's
two main ways to log in. You can either provide a username and password when
configuring the SDK or you can provide a token. For example::

    import {{ name }}
    {{ name }}.configure(first_name="admin", password="password")

Or::

    import {{ name }}
    {{ name }}.configure(token="mytoken")


Features
--------

* TODO
