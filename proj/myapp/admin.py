from django.contrib import admin
from .models import Controller, Module, Slot, ControllerModule

# Register your models here.
admin.site.register(Controller)
admin.site.register(Module)
admin.site.register(ControllerModule)
admin.site.register(Slot)


