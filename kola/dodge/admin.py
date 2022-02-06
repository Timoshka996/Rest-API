from django.contrib import admin
from .models import Car

admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    readonly_fields = ['Preview']

    def preview(self, obj):
        return "Hello!"
