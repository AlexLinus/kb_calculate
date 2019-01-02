from django.contrib import admin
from .models import Services, CarModel, CarBrand
# Register your models here.

class ServicesInline(admin.TabularInline):
    model = Services
    extra = 0

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['model_title', 'create_date', 'is_active']
    inlines = [ServicesInline]

    class Meta:
        model = CarModel

admin.site.register(CarModel, CarModelAdmin)


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['car_title']

    class Meta:
        model = CarBrand

admin.site.register(CarBrand, CarBrandAdmin)