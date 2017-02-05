from django.contrib import admin

from model_app.models import Kisi, Sanatci

#@ -> annotation tanimi
@admin.register(Kisi)
class KisiAdmin(admin.ModelAdmin):
    pass

@admin.register(Sanatci)
class SanatciAdmin(admin.ModelAdmin):
    list_display = ('ilgilendigi_bolum', "kisi")