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
