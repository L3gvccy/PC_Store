from django.shortcuts import render
from django.db.models import Q
from .models import CPU, Motherboard

# Create your views here.

def landing(req):
    return render(req, 'components/landing.html')

def CPUs_view(req):
    cpus = CPU.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)

    if min_price and max_price:
        cpus = cpus.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        cpus = cpus.filter(brand__in=selected_brands)

    # Фільтрація за сокетом
    selected_sockets = req.GET.getlist('socket')
    if selected_sockets:
        cpus = cpus.filter(socket__in=selected_sockets)

    # Фільтрація за кількістю ядер
    selected_cores = req.GET.getlist('cores')
    if selected_cores:
        cpus = cpus.filter(cores__in=selected_cores)

    # Фільтрація за кількістю потоків
    selected_threads = req.GET.getlist('threads')
    if selected_threads:
        cpus = cpus.filter(threads__in=selected_threads)

    # Фільтрація за частотою
    selected_frequencies = req.GET.getlist('frequency')
    if selected_frequencies:
        freq_filter = Q()
        for freq in selected_frequencies:
            min_freq, max_freq = map(float, freq.split('-'))
            freq_filter |= Q(frequency__gte=min_freq, frequency__lte=max_freq)
        cpus = cpus.filter(freq_filter)

    sort = req.GET.get('sort')
    
    if sort == 'price_asc':
        cpus = cpus.order_by('price')
    elif sort == 'price_desc':
        cpus = cpus.order_by('-price')

    selected_brands = req.GET.getlist('brand')
    selected_sockets = req.GET.getlist('socket')
    selected_cores = req.GET.getlist('cores')
    selected_threads = req.GET.getlist('threads')
    selected_freqs = req.GET.getlist('frequency')

    brands = ['Intel', 'AMD']
    sockets = ['AM4', 'AM5', '1851', '1700', '1200']
    cores = ['6', '8', '10', '12', '14', '16', '24']
    threads = ['8', '12', '16', '20', '32']
    frequencies = ['2-2.5', '2.6-3', '3.1-3.6', '3.7-4.2', '4.3-5']

    context = {
        'processors': cpus,
        'brands': brands,
        'sockets': sockets,
        'cores': cores,
        'threads': threads,
        'frequencies': frequencies,
        'selected_brands': selected_brands,
        'selected_sockets': selected_sockets,
        'selected_cores': selected_cores,
        'selected_threads': selected_threads,
        'selected_freqs': selected_freqs,
    }

    return render(req, 'components/cpus.html', context)

def cpu_detail(req, cpu_id):
    cpu = CPU.objects.get(id=cpu_id)
    context = {
        'cpu': cpu,
    }
    return render(req, 'components/cpu_detail.html', context)

def Motherboards_view(req):
    motherboards = Motherboard.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)

    if min_price and max_price:
        motherboards = motherboards.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        motherboards = motherboards.filter(brand__in=selected_brands)

    # Фільтрація за сокетом
    selected_sockets = req.GET.getlist('socket')
    if selected_sockets:
        motherboards = motherboards.filter(socket__in=selected_sockets)

    # Фільтрація за чіпсетом
    selected_chipsets = req.GET.getlist('chipset')
    if selected_chipsets:
        motherboards = motherboards.filter(chipset__in=selected_chipsets)

    # Фільтрація за форм-фактором
    selected_form_factors = req.GET.getlist('form_factor')
    if selected_form_factors:
        motherboards = motherboards.filter(form_factor__in=selected_form_factors)

    # Фільтрація за типом ОЗП
    selected_ram_types = req.GET.getlist('ram_type')
    if selected_ram_types:
        motherboards = motherboards.filter(RAM_type__in=selected_ram_types)

    brands = ['AsRock', 'Asus', 'Gigabyte', 'MSI']
    sockets = ['AM4', 'AM5', '1851', '1700', '1200']
    chipsets = ['B550', 'B650', 'B850', 'X870', 'B560', 'H510', 'B760', 'Z790', 'B860', 'Z890']
    ram_types = ['DDR4', 'DDR5']
    form_factors = ['ATX', 'Micro-ATX', 'Mini-ITX']

    context = {
        'mbs': motherboards,
        'brands': brands,
        'sockets': sockets,
        'chipsets': chipsets,
        'form_factors': form_factors,
        'ram_types': ram_types,
        'selected_brands': selected_brands,
        'selected_sockets': selected_sockets,
        'selected_chipsets': selected_chipsets,
        'selected_form_factors': selected_form_factors,
        'selected_ram_types': selected_ram_types,
    }
    
    return render(req, 'components/motherboards.html', context)

def motherboard_detail(req, motherboard_id):
    mb = Motherboard.objects.get(id=motherboard_id)
    context = {
        'mb': mb,
    }
    return render(req, 'components/motherboard_detail.html', context)