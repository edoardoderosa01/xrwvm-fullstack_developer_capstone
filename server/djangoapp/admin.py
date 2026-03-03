from django.contrib import admin
from .models import CarMake, CarModel

# Register models here
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # shows 1 empty row for quick inline creation


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']


class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    list_filter = ['car_make', 'type', 'year']


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
