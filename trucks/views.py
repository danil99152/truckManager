from django.shortcuts import render
from .models import TruckModel, Truck


def index(request):
    models = TruckModel.objects.all()
    trucks = Truck.objects.all()

    model_filter = request.GET.get('model')
    if model_filter and model_filter != 'all':
        trucks = trucks.filter(model__name=model_filter)

    context = {
        'models': models,
        'trucks': trucks
    }
    return render(request, 'trucks/index.html', context)
