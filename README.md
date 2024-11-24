# django-cms-core-classes

Some lightweight core classes for a cms based on django inspired by 
[Mezzanine](https://github.com/stephenmcd/mezzanine) CMS. 

Mezzanine is a complete CMS System and may be too complex for 
some apps that would only like to add some CMS functionality.

What's in there?

- Base class with
  - Properties: title, publish_date, expiry_date
  - Status model (currently DRAFT and PUBLISHED)
  - Manager with "published" query, based on status and date fields
- Mixins
  - SluggedMixin with unique slugs
  - TimeStampedMixin with created and changed properties
  - AdminOrderMixin based on django-admin-sortable2
  - ContentFieldMixin based on django-tinymce4
- Search functionality
- Admin edit links in frontend

# Todo

- Tests
- Docs
- ...