from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from components.models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case
from .models import Configuration


# Create your views here.
def configurator_view(request):
    cpus = CPU.objects.all()
    motherboards = Motherboard.objects.all()
    rams = RAM.objects.all()
    configuration = None

    ram_msg = None

    if request.user.is_authenticated:
        configuration, created = Configuration.objects.get_or_create(user=request.user)

        if configuration.cpu:
            motherboards = motherboards.filter(socket=configuration.cpu.socket)

        if configuration.motherboard:
            cpus = cpus.filter(socket=configuration.motherboard.socket)
            rams = rams.filter(ram_type=configuration.motherboard.RAM_type)

        if configuration.ram and configuration.motherboard:
            if configuration.ram.ram_type != configuration.motherboard.RAM_type:
                ram_msg = "Обрана оперативна пам'ять не підходить до материнської плати!"

    context = {
        'cpus': cpus,
        'motherboards': motherboards,
        'rams': rams,
        'configuration': configuration,
        'ram_msg': ram_msg,
    }

    return render(request, 'configurator/configurator.html', context)

def select_cpu(request, cpu_id):
    cpu = get_object_or_404(CPU, id=cpu_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.cpu = cpu
    configuration.save()

    return redirect('configurator')

def remove_cpu(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.cpu = None
    configuration.save()

    return redirect('configurator')

def select_mb(request, mb_id):
    mb = get_object_or_404(Motherboard, id=mb_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.motherboard = mb
    configuration.save()

    return redirect('configurator')

def remove_mb(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.motherboard = None
    configuration.save()

    return redirect('configurator')

def select_ram(request, ram_id):
    ram = get_object_or_404(RAM, id=ram_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.ram = ram
    configuration.save()

    return redirect('configurator')

def remove_ram(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.ram = None
    configuration.save()

    return redirect('configurator')