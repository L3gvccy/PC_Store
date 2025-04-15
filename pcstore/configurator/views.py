from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from decimal import Decimal
from components.models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case
from .models import Configuration


# Create your views here.
def configurator_view(request):
    cpus = CPU.objects.all()
    motherboards = Motherboard.objects.all()
    gpus = GPU.objects.all()
    rams = RAM.objects.all()
    storages = Storage.objects.all()
    psus = PSU.objects.all()
    coolers = Cooler.objects.all()
    aios = AIO.objects.all()
    cases = Case.objects.all()
    configuration = None

    ram_msg = None
    storage_msg = None
    psu_msg = None
    cooler_msg = None
    aio_msg = None
    case_msg = None

    if request.user.is_authenticated:
        configuration, created = Configuration.objects.get_or_create(user=request.user)

        if configuration.cpu:
            motherboards = motherboards.filter(socket=configuration.cpu.socket)
            min_cooler_tdp = configuration.cpu.TDP * 1.5
            aios = aios.filter(max_tdp__gte=min_cooler_tdp)
            coolers = coolers.filter(max_tdp__gte=min_cooler_tdp)

        if configuration.motherboard:
            cpus = cpus.filter(socket=configuration.motherboard.socket)
            rams = rams.filter(ram_type=configuration.motherboard.RAM_type)
            if configuration.motherboard.form_factor == 'ATX':
                cases = cases.filter(form_factor='ATX')

        if configuration.gpu and configuration.cpu:
            min_rec_tdp = (configuration.gpu.TDP + configuration.cpu.TDP) * 1.8
            psus = psus.filter(wattage__gte=min_rec_tdp)

        if configuration.case:
            if configuration.case.form_factor == 'Micro-ATX':
                motherboards = motherboards.filter(form_factor='Micro-ATX')
            coolers = coolers.filter(height__lte=configuration.case.max_cooler_height)
            aios = aios.filter(size__lte=configuration.case.max_aio_size)

        if configuration.ram and configuration.motherboard:
            if configuration.ram.ram_type != configuration.motherboard.RAM_type:
                ram_msg = "Обрана оперативна пам'ять не підходить до материнської плати!"

        if configuration.psu and configuration.gpu and configuration.cpu:
            min_rec_tdp = (configuration.gpu.TDP + configuration.cpu.TDP) * 1.8
            if configuration.psu.wattage < min_rec_tdp:
                psu_msg = "Блок живлення недостатньої потужності!"

        if configuration.storage and configuration.motherboard:
            if configuration.storage.storage_type != 'NVMe' and configuration.motherboard.RAM_type == 'DDR5':
                storage_msg = "Обрана материнська плата підтримує M.2 SSD, рекомендуємо вибрати NVMe SSD!"

        if configuration.cpu and configuration.cooler:
            min_cooler_tdp = configuration.cpu.TDP * 1.5
            if configuration.cooler.max_tdp < min_cooler_tdp:
                cooler_msg = "Обраний кулер не підходить до процесора!"

        if configuration.cpu and configuration.aio:
            min_aio_tdp = configuration.cpu.TDP * 1.5
            if configuration.aio.max_tdp < min_aio_tdp:
                aio_msg = "Обрана система рідинного охолодження не підходить до процесора!"

        if configuration.case and configuration.aio:
            if configuration.aio.size > configuration.case.max_aio_size:
                aio_msg = "Обрана система рідинного охолодження не підходить для обраного корпуса!"

        if configuration.case and configuration.cooler:
            if configuration.cooler.height > configuration.case.max_cooler_height:
                cooler_msg = "Обраний кулер не підходить для обраного корпуса!"

        configuration.total_price = calculate_price(configuration)
        configuration.save()

    context = {
        'cpus': cpus,
        'motherboards': motherboards,
        'gpus': gpus,
        'rams': rams,
        'storages': storages,
        'psus': psus,
        'coolers': coolers,
        'aios': aios,
        'cases': cases,
        'configuration': configuration,
        'ram_msg': ram_msg,
        'storage_msg': storage_msg,
        'psu_msg': psu_msg,
        'cooler_msg': cooler_msg,
        'aio_msg': aio_msg,
        'case_msg': case_msg,
    }

    return render(request, 'configurator/configurator.html', context)

def calculate_price(configuration):
    total_price = Decimal(0.00)

    if configuration.cpu:
        total_price += configuration.cpu.price
    if configuration.motherboard:
        total_price += configuration.motherboard.price
    if configuration.ram:
        total_price += configuration.ram.price
    if configuration.gpu:
        total_price += configuration.gpu.price
    if configuration.storage:
        total_price += configuration.storage.price
    if configuration.psu:
        total_price += configuration.psu.price
    if configuration.cooler:
        total_price += configuration.cooler.price
    if configuration.aio:
        total_price += configuration.aio.price
    if configuration.case:
        total_price += configuration.case.price

    return total_price


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

def select_gpu(request, gpu_id):
    gpu = get_object_or_404(GPU, id=gpu_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.gpu = gpu
    configuration.save()

    return redirect('configurator')

def remove_gpu(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.gpu = None
    configuration.save()

    return redirect('configurator')

def select_storage(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.storage = storage
    configuration.save()

    return redirect('configurator')

def remove_storage(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.storage = None
    configuration.save()

    return redirect('configurator')

def select_psu(request, psu_id):
    psu = get_object_or_404(PSU, id=psu_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.psu = psu
    configuration.save()

    return redirect('configurator')

def remove_psu(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.psu = None
    configuration.save()

    return redirect('configurator')

def select_cooler(request, cooler_id):
    cooler = get_object_or_404(Cooler, id=cooler_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.cooler = cooler
    configuration.save()

    return redirect('configurator')

def remove_cooler(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.cooler = None
    configuration.save()

    return redirect('configurator')

def select_aio(request, aio_id):
    aio = get_object_or_404(AIO, id=aio_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.aio = aio
    configuration.save()

    return redirect('configurator')

def remove_aio(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.aio = None
    configuration.save()

    return redirect('configurator')

def select_case(request, case_id):
    case = get_object_or_404(Case, id=case_id)

    configuration, created = Configuration.objects.get_or_create(user=request.user)
    configuration.case = case
    configuration.save()

    return redirect('configurator')

def remove_case(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.case = None
    configuration.save()

    return redirect('configurator')

def clear_configuration(request):
    configuration = Configuration.objects.get(user=request.user)
    configuration.cpu = None
    configuration.motherboard = None
    configuration.ram = None
    configuration.gpu = None
    configuration.storage = None
    configuration.psu = None
    configuration.cooler = None
    configuration.aio = None
    configuration.case = None
    configuration.total_price = 0.00
    configuration.save()

    return redirect('configurator')