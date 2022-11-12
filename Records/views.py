from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def add_farmer_info(request):
    if request.method == "GET":
        return HttpResponse("Method not allowed")
    else:
        name = request.POST["name"]
        farm_name = request.POST["farm_name"]
        farm = Farmer.objects.filter(name=name)
        if farm.exists():
            return render(request, 'index.html', {'message': "Farmer name already exist"})
        farm = Farmer.objects.create(name=name, farm_name=farm_name)
        farm.save()
        return HttpResponseRedirect('/tractor-info')


def tractor_info(request):
    if request.method == "GET":
        return render(request, 'create-tractor.html')
    if request.method == "POST":
        farmer_name = request.POST["name"]
        tractor_name = request.POST["tractor_name"]
        harrow = False
        cultivator = False
        dumping_trailer = False
        paddy_trasher = False
        rotavator = False
        plough = False
        wheel = False
        try:
            request.POST["harrow"]
            harrow = True
        except:
            harrow = False
        try:
            request.POST["rotavator"]
            rotavator = True
        except:
            harrow = False
        try:
            request.POST["cultivator"]
            cultivator = True
        except:
            cultivator = False
        try:
            request.POST["paddy trasher"]
            paddy_trasher = True
        except:
            paddy_trasher = False
        try:
            request.POST["dumping trailer"]
            dumping_trailer = True
        except:
            paddy_trasher = False
        try:
            request.POST["wheel"]
            wheel = True
        except:
            wheel = False
        try:
            request.POST["plough"]
            plough = True
        except:
            plough = False
        print(harrow, rotavator, cultivator, paddy_trasher,
              dumping_trailer, wheel, plough)

        farmer = Farmer.objects.filter(name=farmer_name)
        if farmer.exists():
            farmer = farmer[0]
            tractor = Tractor.objects.create(name=tractor_name, owner=farmer, harrow=harrow, cultivator=cultivator, rotavator=rotavator,
                                             plough=plough, paddy_trasher=paddy_trasher, dumping_trailer=dumping_trailer, four_wheel_trailer=wheel)
            tractor.save()
            return HttpResponseRedirect('/all-tractors')
        return render(request, 'create-tractor.html', {'message': 'Farmer does not exist'})


def tractors(request):
    return render(request, 'tractors.html', {'tractors': Tractor.objects.all()})


def tractor_details(request, id):
    tractor = Tractor.objects.filter(id=id)
    if tractor.exists():
        return render(request, 'tractor-details.html', {'tractor': tractor[0]})
