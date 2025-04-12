from django.shortcuts import render
from django.db.models import Q
from .models import CPU, Motherboard, GPU

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
    sockets = ['AM4', 'AM5', '1851', '1700', '1200', '1151']
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

    selected_brands = req.GET.getlist('brand')
    selected_sockets = req.GET.getlist('socket')

    brands = ['AsRock', 'Asus', 'Gigabyte', 'MSI']
    sockets = ['AM4', 'AM5', '1851', '1700', '1200', '1151']

    context = {
        'mbs': motherboards,
        'brands': brands,
        'sockets': sockets,
        'selected_brands': selected_brands,
        'selected_sockets': selected_sockets,
    }
    
    return render(req, 'components/motherboards.html', context)

def motherboard_detail(req, motherboard_id):
    mb = Motherboard.objects.get(id=motherboard_id)
    context = {
        'mb': mb,
    }
    return render(req, 'components/motherboard_detail.html', context)



def GPUs_view(req):
    gpus = GPU.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        gpus = gpus.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        gpus = gpus.filter(brand__in=selected_brands)

    # Фільтрація за виробником графічного процесору
    selected_gp_brands = req.GET.getlist('gp_brand')
    if selected_gp_brands:
        gpus = gpus.filter(gp_brands__in=selected_gp_brands)

    # Фільтрація за серією відеокарти 
    selected_series = req.GET.getlist('series')
    if selected_series:
        gpus = gpus.filter(series__in=selected_series)

    # Фільтрація за памʼяттю
    selected_memory = req.GET.getlist('memory')
    if selected_memory:
        gpus = gpus.filter(memory__in=selected_memory)

    # Фільтрація за памʼяттю
    selected_memory_types = req.GET.getlist('memory_type')
    if selected_memory_types:
        gpus = gpus.filter(memory_type__in=selected_memory_types)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        gpus = gpus.order_by('price')
    elif sort == 'price_desc':
        gpus = gpus.order_by('-price')

    # Варіанти для фільтрів
    brands = ['MSI', 'ASUS', 'Palit', 'Gigabyte']
    gp_brands = ['AMD','Nvidia']
    memory_options = ['6', '8', '10', '12', '16', '24']
    memory_types = ['GDDR6', 'GDDR6X','GDDR7','GDDR7X']


    context = {
        'gpus': gpus,
        'brands': brands,
        'gp_brands': gp_brands,
        'memory_options': memory_options,
        'memory_types': memory_types,
        'selected_brands': selected_brands,
        'selected_gp_brands' : selected_gp_brands,
        'selected_memory': selected_memory,
        'selected_memory_types': selected_memory_types,
    }

    return render(req, 'components/gpus.html', context)

def gpu_detail(req, gpu_id):
    gpu = Motherboard.objects.get(id=gpu_id)
    context = {
        'gpu': gpu,
    }
    return render(req, 'components/gpu_detail.html', context)