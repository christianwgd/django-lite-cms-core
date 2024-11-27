django-lite-cms-core
====================

Django-lite-cms-core provides some base classes to add CMS functionality to
any Django app and is inspired by Mezzanine_ CMS. While Mezzanine_ is a full
featured CMS django-lite-cms is a more modular approach.

.. _Mezzanine: http://mezzanine.jupo.org/

Installation
------------

``django-lite-cms-core`` can be found on pypi. Run::

    pip install django-lite-cms-core

to install the package on your machine or in your virtual environment.

Getting Started
---------------

To integrate ``django-lite-cms-core`` with your site, follow the steps as listed:

1.  Add this application in the ``INSTALLED_APPS`` portion of your settings
    file. Your settings file will look something like::

        INSTALLED_APPS = (
            # ...
            'lite_cms_core',
        )

2.  Add the lite_cms_core urls to the end of your root urlconf. Your urlconf
    will look something like::

        urlpatterns = [
            # ...
            path('lite_cms_core/', include('lite_cms_core.urls')),
        ]

