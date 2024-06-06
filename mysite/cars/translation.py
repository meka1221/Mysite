from .models import Car
from modeltranslation.translator import register, TranslationOptions


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('title_car', 'description')

