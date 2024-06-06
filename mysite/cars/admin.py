from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(Marka)
admin.site.register(Model)
admin.site.register(Category)
admin.site.register(CarPhoto)
admin.site.register(Bet)



@admin.register(Car)
class CarAdmin(TranslationAdmin):
    list_display = ("title_car",)
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
