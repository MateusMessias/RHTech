from django.contrib import admin

# Register your models here.

from rh.models import *


admin.site.register(Colaboradores)
admin.site.register(Area)
admin.site.register(Contabilidade)
admin.site.register(Empresa)
admin.site.register(Ponto)
admin.site.register(Notas)


