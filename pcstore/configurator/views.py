from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from components.models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case
from .models import Configuration


# Create your views here.
def configurator_view(request):
    cpus = CPU.objects.all()
    configuration = None

    if request.user.is_authenticated:
        configuration, created = Configuration.objects.get_or_create(user=request.user)

    context = {
        'cpus': cpus,

        'configuration': configuration,
    }

    return render(request, 'configurator/configurator.html', context)

def select_cpu(request, cpu_id):
    cpu = get_object_or_404(CPU, id=cpu_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.cpu = cpu
    configuration.save()

    return redirect('configurator')