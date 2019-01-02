from django.shortcuts import render
from .models import CarModel
from .forms import CarModelForm
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
# Create your views here.

def home(request):
    models = CarModel.objects.all()
    form = CarModelForm
    return render(request, 'home.html', context={'models': models, 'form': form})

def get_model(request):
    if request.method == 'GET':
        model_id = int(request.GET.get('model_id'))
        get_model = CarModel.objects.get(id=model_id)
        #model = serializers.serialize('json', get_model)
        #return JsonResponse(model)
        return render(request, 'price-block.html', context={'model': get_model})