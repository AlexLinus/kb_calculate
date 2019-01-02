from .models import CarModel
from django.forms import ModelForm
from django import forms

class CarModelForm(ModelForm):
    model_title = forms.ChoiceField(choices=[(model.id, model.model_title) for model in CarModel.objects.all()]) #здесь я короче говорю,, что вместо инпута должен быть select, и в choices (значения селекта) я вставляю title всех объектов модели. Зачем ID добавил к тайтул, потому что так требует choices, два аргумента, в частности айди. ID он записывает в VALUE. Получается потом мы можем брать это value и брать выбранный объект по id. Круто!
    class Meta:
        model = CarModel
        fields = ['model_title']
