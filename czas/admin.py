from django.contrib import admin
from .models import KontaktModel
from .models import CzasModel

# Register your models here.





class AdminKontaktModel(admin.ModelAdmin):
    list_display = ('tytuł', 'email', 'data_wpisu')


class CzasModelAdmin(admin.ModelAdmin):
    list_display = ('imie', 'data_dodania')
    search_fields = ('imie', 'data_dodania')


admin.site.register(KontaktModel, AdminKontaktModel)
admin.site.register(CzasModel, CzasModelAdmin)

# Register your models here.

