from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.forms import CarForm, CarModelForm

from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
# versão 1 (view na mão)
def cars_view(request):
    filter=request.GET.get('search') or ''
    print(request.GET)
    cars = Car.objects.filter(model__contains=f'{filter}').order_by('model')
    context = {
        'cars': cars
    }
    return render(request, 'cars.html', context)

# versão 2 (herda de view base)
class CarsView(View):
    def get(self, request):
        filter=request.GET.get('search') or ''
        print(request.GET)
        cars = Car.objects.filter(model__contains=f'{filter}').order_by('model')
        context = {
            'cars': cars
        }
        return render(request, 'cars.html', context)

# versão 3 (herda de view generica)
class CarsListView(ListView):
    model=Car
    template_name='cars.html'
    context_object_name = 'cars'

    def get_queryset(self) -> QuerySet[Any]:
        cars = super().get_queryset().order_by('model')
        filter = self.request.GET.get('search') or ''
        return cars.filter(model__icontains=f'{filter}')


#versão 1
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    context={
        'new_car_form':new_car_form
    }
    return render(request, 'new_car.html', context)

    
#versão 2
class NewCarsView(View):
    def get(self,request):
        new_car_form = CarModelForm()
        context={
            'new_car_form':new_car_form
        }
        return render(request, 'new_car.html', context)
    
    def post(self,request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        context={
            'new_car_form':new_car_form
        }
        return render(request, 'new_car.html', context)
        
    
#versão 3
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'
    

class CarDetailsView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    # success_url = f'/cars/{test}/'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk':self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

