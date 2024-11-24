from modeltranslation.translator import register, TranslationOptions
from cms_core_classes.models import BaseEntity, ContentFieldMixin


@register(BaseEntity)
class TranslatedBaseEntity(TranslationOptions):
    fields = ('title', )


@register(ContentFieldMixin)
class TranslatedContentFieldMixin(TranslationOptions):
    fields = ('content', )
