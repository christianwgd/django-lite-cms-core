django-lite-cms-core
====================

.. warning::
    The docs is work inprogress, so it is not completed by now.

Django-lite-cms-core provides some base classes to add CMS functionality to
any Django app and is inspired by Mezzanine_ CMS. While Mezzanine_ is a full
featured CMS django-lite-cms is a more modular approach.

.. _Mezzanine: http://mezzanine.jupo.org/

Installation
------------

``django-lite-cms-core`` can be found on pypi. Run::

    pip install django-lite-cms-core

to install the package on your machine or in your virtual environment.


Dependencies
------------

If you install ``django-lite-cms-core`` the following modules will be
installed, because ``django-lite-cms-core`` depends on them:

1. django-bootstrap5
    Currently the templates used in ``django-lite-cms-core`` use
    django-bootstrap5. You can avoid this dependency by overriding
    the templates to use none or another css framework.

2. django-tinymce
    django-tinymce provides the HTML field for the ``ContentFieldMixin``.

3. django-admin-sortable2
    The ``AdminOrderMixin``is based on django-admin-sortable2. If you
    don't use the ordering, you can remove the dependency.

4. django-filebrowser-no-grappelli
    The django-filebrowser-no-grappelli library provides the media
    management for the tinymce HTML field.

5. Pillow
    Pillow is a dependency of django-filebrowser-no-grappelli

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

.. note::
    You need to include the url patterns ony if you want to use the search functionality.


.. toctree::
   :maxdepth: 4

   modelclasses