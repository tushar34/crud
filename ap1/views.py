from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from ap1.forms import CardataForm
from ap1.models import Cardata
import requests
def car(request):
    if request.method == 'POST':
        company = request.POST.get('company', '')
        car = request.POST.get('car', '')
        price = request.POST.get('price', '')
        x = Cardata(c_company=company,c_name=car,c_price=price)
        x.save()

        return redirect('/')
    else:
        return render(request,'car_detail.html')
   # context = {}

    # add the dictionary during initialization
    # form = CardataForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    #
    # context['form'] = form

    # return render(request, 'car_detail.html', context)

import  requests
def view_data(request):
    url = 'http://127.0.0.1:8000/product/'
    #r = requests.get(url).json()
    #context = {'product_data'}

    data = Cardata.objects.all()
    context={
        'detail': data
    }

    return render(request, 'view_car.html',context)

def delete_data(request,id):
    c = Cardata.objects.get(id=id)
    c.delete()
    return redirect('/')
def update_data(request,id):
    if request.method == 'POST':

        company = request.POST.get('cn', '')
        car = request.POST.get('n', '')
        price = request.POST.get('p', '')
        x = Cardata(id=id,c_company=company,c_name=car,c_price=price)
        x.save()
        return redirect('/')
    else:
        c = Cardata.objects.get(id=id)
        return render(request, 'update_car.html', {'dta': c})

