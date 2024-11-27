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
    The ``AdminOrderMixin`` is based on django-admin-sortable2. If you
    don't use the ordering, you can remove the dependency.

4. django-filebrowser-no-grappelli
    The django-filebrowser-no-grappelli library provides the media
    management for the tinymce HTML field.

5. Pillow
    Pillow is a dependency of django-filebrowser-no-grappelli
