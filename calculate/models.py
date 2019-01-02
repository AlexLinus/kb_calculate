from django.db import models

# Create your models here.
class CarBrand(models.Model):
    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'

    car_title = models.CharField(max_length=150, default=None, blank=False, null=False)

    def __str__(self):
        return self.car_title


class CarModel(models.Model):
    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'
        ordering = ['-brand_title']

    brand_title = models.ForeignKey(CarBrand, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Марка автомобиля')
    model_title = models.CharField(max_length=200, default=None, blank=False, null=False, verbose_name='Модель автомобиля*')
    notes = models.TextField(blank=True, null=True, default='Нет заметок', verbose_name='Дополнительная информация')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edit_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return self.model_title

class Services(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-service_title']

    car = models.ForeignKey(CarModel, verbose_name='Марка автомобиля', blank=False, null=False, related_name='model_services', on_delete=models.CASCADE)
    service_title = models.CharField(max_length=250, default=None, blank=False, null=False, verbose_name='Название услуги')
    service_price = models.PositiveIntegerField(default=0, verbose_name='Стоимость услуги')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edit_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return self.service_title