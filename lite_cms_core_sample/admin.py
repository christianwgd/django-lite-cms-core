from django.contrib import admin

from lite_cms_core_sample.models import SluggedItem


@admin.register(SluggedItem)
class SluggedItemAdmin(admin.ModelAdmin):
    pass
