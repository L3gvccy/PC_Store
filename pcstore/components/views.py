from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from django.db.models import Q
<<<<<<< HEAD
<<<<<<< HEAD
from .models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case
=======
>>>>>>> 67d780e (add header)
=======
from .models import CPU
from .forms import CPUFilterForm
>>>>>>> ec58bea (add cpus page)
=======
from django.db.models import Q
<<<<<<< HEAD
from .models import CPU, Motherboard
>>>>>>> 3cce6bf (add motherboards)
=======
from .models import CPU, Motherboard, GPU
>>>>>>> 01cc471 (Add GPU)
=======
from .models import CPU, Motherboard, GPU, RAM
>>>>>>> ef1f7ff (Add RAM)
=======
from .models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case
>>>>>>> 5fc22e5 (Add storages)

# Create your views here.

def landing(req):
<<<<<<< HEAD
<<<<<<< HEAD
    return render(req, 'components/landing.html')

def components(req):
    return render(req, 'components/components.html')

<<<<<<< HEAD
=======
    return render(req, 'components/landing.html')

>>>>>>> ec58bea (add cpus page)
=======
>>>>>>> 218d31d (add components main page)
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cce6bf (add motherboards)
        freq_filter = Q()
        for freq in selected_frequencies:
            min_freq, max_freq = map(float, freq.split('-'))
            freq_filter |= Q(frequency__gte=min_freq, frequency__lte=max_freq)
        cpus = cpus.filter(freq_filter)
<<<<<<< HEAD
=======
        cpus = cpus.filter(frequency__in=selected_frequencies)
>>>>>>> ec58bea (add cpus page)
=======
>>>>>>> 3cce6bf (add motherboards)

    sort = req.GET.get('sort')
    
    if sort == 'price_asc':
        cpus = cpus.order_by('price')
    elif sort == 'price_desc':
        cpus = cpus.order_by('-price')

    selected_brands = req.GET.getlist('brand')
    selected_sockets = req.GET.getlist('socket')
    selected_cores = req.GET.getlist('cores')
<<<<<<< HEAD
<<<<<<< HEAD
    selected_threads = req.GET.getlist('threads')
    selected_freqs = req.GET.getlist('frequency')
=======
    selected_threads = req.GET.getlist('cores')
    selected_freqs = req.GET.getlist('cores')
>>>>>>> ec58bea (add cpus page)
=======
    selected_threads = req.GET.getlist('threads')
    selected_freqs = req.GET.getlist('frequency')
>>>>>>> 3cce6bf (add motherboards)

    brands = ['Intel', 'AMD']
    sockets = ['AM4', 'AM5', '1851', '1700', '1200', '1151']
    cores = ['6', '8', '10', '12', '14', '16', '24']
    threads = ['8', '12', '16', '20', '32']
<<<<<<< HEAD
<<<<<<< HEAD
    frequencies = ['2-2.5', '2.6-3', '3.1-3.6', '3.7-4.2', '4.3-5']

    context = {
        'processors': cpus,
        'selected_sort': sort,
<<<<<<< HEAD
=======
    frequencies = ['2-2.5', '2.6-3', '3.1-3.6', '3.7-4.2', '4.3+']
=======
    frequencies = ['2-2.5', '2.6-3', '3.1-3.6', '3.7-4.2', '4.3-5']
>>>>>>> 3cce6bf (add motherboards)

    context = {
        'processors': cpus,
>>>>>>> ec58bea (add cpus page)
=======
>>>>>>> a8316c4 (add sort)
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

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 31afb41 (update cart, add cpu detail, add cart item cout)
    return render(req, 'components/cpus.html', context)

def cpu_detail(req, cpu_id):
    cpu = CPU.objects.get(id=cpu_id)
    context = {
        'cpu': cpu,
    }
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cce6bf (add motherboards)
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

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    # Фільтрація за чіпсетом
>>>>>>> 246302b (add motherboard details)
=======
>>>>>>> 9d3cf93 (add coolers and aios)
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
<<<<<<< HEAD
<<<<<<< HEAD

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        motherboards = motherboards.order_by('price')
    elif sort == 'price_desc':
        motherboards = motherboards.order_by('-price')

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        motherboards = motherboards.order_by('price')
    elif sort == 'price_desc':
        motherboards = motherboards.order_by('-price')

    brands = ['AsRock', 'Asus', 'Gigabyte', 'MSI']
    sockets = ['AM4', 'AM5', '1851', '1700', '1200']
    chipsets = ['B550', 'B650', 'B850', 'X870', 'Z390', 'B560', 'H510', 'B760', 'Z790', 'B860', 'Z890']
    ram_types = ['DDR4', 'DDR5']
    form_factors = ['ATX', 'Micro-ATX']

    context = {
        'mbs': motherboards,
        'selected_sort': sort,
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
        gpus = gpus.filter(gp_brand__in=selected_gp_brands)

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
    memory_options = ['6', '8', '10', '12', '16', '24', '32']
    memory_types = ['GDDR6', 'GDDR6X','GDDR7','GDDR7X']


    context = {
        'gpus': gpus,
        'selected_sort': sort,
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
    gpu = GPU.objects.get(id=gpu_id)
    context = {
        'gpu': gpu,
    }
    return render(req, 'components/gpu_detail.html', context)

def RAMs_view(req):
    rams = RAM.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        rams = rams.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        rams = rams.filter(brand__in=selected_brands)

    # Фільтрація за обсягом
    selected_capacities = req.GET.getlist('capacity')
    if selected_capacities:
        rams = rams.filter(capacity__in=selected_capacities)

    # Фільтрація за типом пам'яті
    selected_ram_types = req.GET.getlist('ram_type')
    if selected_ram_types:
        rams = rams.filter(ram_type__in=selected_ram_types)

    # Фільтрація за частотою
    selected_frequencies = req.GET.getlist('frequency')
    if selected_frequencies:
        rams = rams.filter(frequency__in=selected_frequencies)

    # Фільтрація за кількістью модулів
    selected_number_of_modules = req.GET.getlist('num')
    if selected_number_of_modules:
        rams = rams.filter(number_of_modules__in=selected_number_of_modules)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        rams = rams.order_by('price')
    elif sort == 'price_desc':
        rams = rams.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Corsair', 'G.Skill', 'Kingston', 'Patriot']
    capacities = ['8','16','32', '64']
<<<<<<< HEAD
    ram_types = ['DDR4', 'DDR5']
    frequencies = ['2400', '2666', '3000', '3200', '4600', '4800', '5200', '5600', '6000']
    number_of_modules = ['1', '2']


    context = {
        'rams': rams,
        'selected_sort': sort,
        'brands': brands,
        'capacities': capacities,
        'ram_types': ram_types,
        'frequencies': frequencies,
        'number_of_modules': number_of_modules,
        'selected_brands': selected_brands,
        'selected_capacities': selected_capacities,
        'selected_ram_types': selected_ram_types,
        'selected_frequencies': selected_frequencies,
        'selected_number_of_modules': selected_number_of_modules,
    }

    return render(req, 'components/rams.html', context)

def ram_detail(req, ram_id):
    ram = RAM.objects.get(id=ram_id)
    context = {
        'ram': ram,
    }
    return render(req, 'components/ram_detail.html', context)

def Storages_view(req):
    storages = Storage.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        storages = storages.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        storages = storages.filter(brand__in=selected_brands)

    # Фільтрація за обсягом
    selected_capacities = req.GET.getlist('capacity')
    if selected_capacities:
        storages = storages.filter(capacity__in=selected_capacities)

    # Фільтрація за типом накопичувача
    selected_storage_types = req.GET.getlist('storage_type')
    if selected_storage_types:
        storages = storages.filter(storage_type__in=selected_storage_types)

    # Фільтрація за швидкістю
    selected_speeds = req.GET.getlist('speed')
    if selected_speeds:
        speed_filter = Q()
        for speed in selected_speeds:
            min_speed, max_speed = map(float, speed.split('-'))
            speed_filter |= Q(speed__gte=min_speed, speed__lte=max_speed)
        storages = storages.filter(speed_filter)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        storages = storages.order_by('price')
    elif sort == 'price_desc':
        storages = storages.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Adata', 'Kingston', 'Samsung', 'Toshiba']
    capacities = ['128 GB','256 GB','512 GB','1 TB','2 TB', '4 TB']
    storage_types = ['HDD', 'SSD', 'NVMe']
    speeds = ['0-1000', '1001-2000', '2001-3000', '3001-4000', '4001-5000', '5001-6000', '6001-7000', '7001-8000', '8001-9000', '9001-10000']

    context = {
        'storages': storages,
        'selected_sort': sort,
        'brands': brands,
        'capacities': capacities,
        'storage_types': storage_types,
        'speeds': speeds,
        'selected_brands': selected_brands,
        'selected_capacities': selected_capacities,
        'selected_storage_types': selected_storage_types,
        'selected_speeds': selected_speeds,
    }

    return render(req, 'components/storages.html', context)

def storage_detail(req, storage_id):
    storage = Storage.objects.get(id=storage_id)
    context = {
        'storage': storage,
    }
    return render(req, 'components/storage_detail.html', context)

def Coolers_view(req):
    coolers = Cooler.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        coolers = coolers.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        coolers = coolers.filter(brand__in=selected_brands)

    # Фільтрація за к-тю теплотрубок
    selected_heat_tube_numbers = req.GET.getlist('heat_tube_number')
    if selected_heat_tube_numbers:
        coolers = coolers.filter(heat_tube_number__in=selected_heat_tube_numbers)

    # Фільтрація за висотою
    selected_heights = req.GET.getlist('height')
    if selected_heights:
        height_filter = Q()
        for height in selected_heights:
            min_height, max_height = map(float, height.split('-'))
            height_filter |= Q(height__gte=min_height, height__lte=max_height)
        coolers = coolers.filter(height_filter)

    # Фільтрація за RGB
    selected_argbs = req.GET.getlist('argb')
    if 'З ARGB підсвіткою' in selected_argbs and 'Без ARGB підсвітки' not in selected_argbs:
        coolers = coolers.filter(argb=True)
    elif 'Без ARGB підсвітки' in selected_argbs and 'З ARGB підсвіткою' not in selected_argbs:
        coolers = coolers.filter(argb=False)

    # Фільтрація за максимальним TDP
    selected_max_tdps = req.GET.getlist('max_tdp')
    if selected_max_tdps:
        max_tdp_filter = Q()
        for max_tdp in selected_max_tdps:
            min_max_tdps, max_max_tdps = map(float, max_tdp.split('-'))
            max_tdp_filter |= Q(max_tdp__gte=min_max_tdps, max_tdp__lte=max_max_tdps)
        coolers = coolers.filter(max_tdp_filter)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        coolers = coolers.order_by('price')
    elif sort == 'price_desc':
        coolers = coolers.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Deepcool', 'Arctic', 'ID Cooling']
    heat_tube_numbers = ['4', '5', '6', '7']
    heights = ['51-100', '101-150', '151-200']
    argbs = ['З ARGB підсвіткою', 'Без ARGB підсвітки']
    max_tdps = ['0-100', '101-150', '151-200', '201-250']

    context = {
        'coolers': coolers,
        'selected_sort': sort,
<<<<<<< HEAD
        'brands': brands,
        'heat_tube_numbers': heat_tube_numbers,
        'heights': heights,
        'argbs': argbs,
        'max_tdps': max_tdps,
        'selected_brands': selected_brands,
        'selected_heat_tube_numbers': selected_heat_tube_numbers,
        'selected_heights': selected_heights,
        'selected_argbs': selected_argbs,
        'selected_max_tdps': selected_max_tdps,
    }

    return render(req, 'components/coolers.html', context)

def cooler_detail(req, cooler_id):
    cooler = Cooler.objects.get(id=cooler_id)
    context = {
        'cooler': cooler,
    }
    return render(req, 'components/cooler_detail.html', context)

def AIOs_view(req):
    aios = AIO.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        aios = aios.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        aios = aios.filter(brand__in=selected_brands)

    # Фільтрація за к-тю теплотрубок
    selected_heat_tube_numbers = req.GET.getlist('heat_tube_number')
    if selected_heat_tube_numbers:
        aios = aios.filter(heat_tube_number__in=selected_heat_tube_numbers)

    # Фільтрація за довжиною
    selected_sizes = req.GET.getlist('size')
    if selected_sizes:
        aios = aios.filter(size__in=selected_sizes)

    # Фільтрація за RGB
    selected_argbs = req.GET.getlist('argb')
    if 'З ARGB підсвіткою' in selected_argbs and 'Без ARGB підсвітки' not in selected_argbs:
        aios = aios.filter(argb=True)
    elif 'Без ARGB підсвітки' in selected_argbs and 'З ARGB підсвіткою' not in selected_argbs:
        aios = aios.filter(argb=False)

    # Фільтрація за максимальним TDP
    selected_max_tdps = req.GET.getlist('max_tdp')
    if selected_max_tdps:
        max_tdp_filter = Q()
        for max_tdp in selected_max_tdps:
            min_max_tdps, max_max_tdps = map(float, max_tdp.split('-'))
            max_tdp_filter |= Q(max_tdp__gte=min_max_tdps, max_tdp__lte=max_max_tdps)
        aios = aios.filter(max_tdp_filter)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        aios = aios.order_by('price')
    elif sort == 'price_desc':
        aios = aios.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Deepcool', 'Arctic', 'MSI']
    sizes = ['120', '240', '360']
    argbs = ['З ARGB підсвіткою', 'Без ARGB підсвітки']
    max_tdps = ['151-250', '251-350']

    context = {
        'aios': aios,
        'selected_sort': sort,
        'brands': brands,
        'sizes': sizes,
        'argbs': argbs,
        'max_tdps': max_tdps,
        'selected_brands': selected_brands,
        'selected_heat_tube_numbers': selected_heat_tube_numbers,
        'selected_sizes': selected_sizes,
        'selected_argbs': selected_argbs,
        'selected_max_tdps': selected_max_tdps,
    }

    return render(req, 'components/aios.html', context)

def aio_detail(req, aio_id):
    aio = AIO.objects.get(id=aio_id)
    context = {
        'aio': aio,
    }
    return render(req, 'components/aio_detail.html', context)

def PSUs_view(req):
    psus = PSU.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        psus = psus.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        psus = psus.filter(brand__in=selected_brands)

    # Фільтрація за ватами
    selected_wattages = req.GET.getlist('wattage')
    if selected_wattages:
        wattage_filter = Q()
        for wattage in selected_wattages:
            min_wattage, max_wattage = map(float, wattage.split('-'))
            wattage_filter |= Q(wattage__gte=min_wattage, wattage__lte=max_wattage)
        psus = psus.filter(wattage_filter)

    # Фільтрація за сертифікатом
    selected_certificates = req.GET.getlist('certificate')
    if selected_certificates:
        psus = psus.filter(certificate__in=selected_certificates)

    # Фільтрація за модульністю
    selected_modularities = req.GET.getlist('modular')
    if 'Модульний' in selected_modularities and 'Немодульний' not in selected_modularities:
        psus = psus.filter(modular=True)
    elif 'Немодульний' in selected_modularities and 'Модульний' not in selected_modularities:
        psus = psus.filter(modular=False)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        psus = psus.order_by('price')
    elif sort == 'price_desc':
        psus = psus.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Be Quiet!','Gigabyte', 'Deepcool', 'MSI']
    wattages = ['1000-1300', '900-1000', '800-850', '700-750', '600-650', '500-550', '400-450']
    certificates = ['80 Plus Titanium', '80 Plus Platinum', '80 Plus Gold', '80 Plus Silver', '80 Plus Bronze', 'Без сертифікату']
    modularities = ['Модульний', 'Немодульний']

    context = {
        'psus': psus,
        'selected_sort': sort,
        'brands': brands,
        'wattages': wattages,
        'certificates': certificates,
        'modularities': modularities,
        'selected_brands': selected_brands,
        'selected_wattages': selected_wattages,
        'selected_certificates': selected_certificates,
        'selected_modularities': selected_modularities,
    }

    return render(req, 'components/psus.html', context)

def psu_detail(req, psu_id):
    psu = PSU.objects.get(id=psu_id)
    context = {
        'psu': psu,
    }
    return render(req, 'components/psu_detail.html', context)

def Cases_view(req):
    cases = Case.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        cases = cases.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        cases = cases.filter(brand__in=selected_brands)

    # Фільтрація за форм фактором
    selected_form_factors = req.GET.getlist('form_factor')
    if selected_form_factors:
        cases = cases.filter(form_factor__in=selected_form_factors)

    # Фільтрація за кількістю вентиляторів
    selected_fans = req.GET.getlist('fans')
    if selected_fans:
        cases = cases.filter(fans__in=selected_fans)

    # Фільтрація за максимальною висотою кулера
    selected_max_cooler_heights = req.GET.getlist('max_cooler_height')
    if selected_max_cooler_heights:
        height_filter = Q()
        for height in selected_max_cooler_heights:
            min_height, max_height = map(float, height.split('-'))
            height_filter |= Q(max_cooler_height__gte=min_height, max_cooler_height__lte=max_height)
        cases = cases.filter(height_filter)

    # Фільтрація за максимальною довжиною СРО
    selected_max_aio_sizes = req.GET.getlist('max_aio_size')
    if selected_max_aio_sizes:
        cases = cases.filter(max_aio_size__in=selected_max_aio_sizes)

    # Фільтрація за наявністю скла
    selected_tempered_glasses = req.GET.getlist('tempered_glass')
    if 'Зі склом' in selected_tempered_glasses and 'Без скла' not in selected_tempered_glasses:
        cases = cases.filter(tempered_glass=True)
    elif 'Без скла' in selected_tempered_glasses and 'Зі склом' not in selected_tempered_glasses:
        cases = cases.filter(tempered_glass=False)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        cases = cases.order_by('price')
    elif sort == 'price_desc':
        cases = cases.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Be Quiet!','Gamemax', 'Deepcool', 'MSI']
    form_factors = ['ATX', 'Micro-ATX']
    fans_ch = ['0', '1', '3', '4']
    max_cooler_heights = ['0-100', '101-150', '151-200']
    max_aio_sizes = ['240', '360']
    tempered_glasses = ['Зі склом', 'Без скла']

    context = {
        'cases': cases,
        'selected_sort': sort,
        'brands': brands,
        'form_factors': form_factors,
        'fans_ch': fans_ch,
        'max_cooler_heights': max_cooler_heights,
        'max_aio_sizes': max_aio_sizes,
        'tempered_glasses': tempered_glasses,
        'selected_brands': selected_brands,
        'selected_form_factors': selected_form_factors,
        'selected_fans': selected_fans,
        'selected_max_cooler_heights': selected_max_cooler_heights,
        'selected_max_aio_sizes': selected_max_aio_sizes,
        'selected_tempered_glasses': selected_tempered_glasses,
    }

    return render(req, 'components/cases.html', context)

def case_detail(req, case_id):
    case = Case.objects.get(id=case_id)
    context = {
        'case': case,
    }
    return render(req, 'components/case_detail.html', context)
=======
    return render(req, 'components/landing.html')
>>>>>>> 67d780e (add header)
=======
    return render(req, 'components/cpus.html', context)
>>>>>>> ec58bea (add cpus page)
=======
    return render(req, 'components/cpu_detail.html', context)
>>>>>>> 31afb41 (update cart, add cpu detail, add cart item cout)
=======
    selected_brands = req.GET.getlist('brand')
    selected_sockets = req.GET.getlist('socket')
=======
>>>>>>> 246302b (add motherboard details)
=======
    selected_brands = req.GET.getlist('brand')
    selected_sockets = req.GET.getlist('socket')
>>>>>>> 01cc471 (Add GPU)
=======
>>>>>>> 9d3cf93 (add coolers and aios)

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
<<<<<<< HEAD
>>>>>>> 3cce6bf (add motherboards)
=======

def motherboard_detail(req, motherboard_id):
    mb = Motherboard.objects.get(id=motherboard_id)
    context = {
        'mb': mb,
    }
    return render(req, 'components/motherboard_detail.html', context)
<<<<<<< HEAD
>>>>>>> 246302b (add motherboard details)
=======

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
        gpus = gpus.filter(gp_brand__in=selected_gp_brands)

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
    memory_options = ['6', '8', '10', '12', '16', '24', '32']
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
    gpu = GPU.objects.get(id=gpu_id)
    context = {
        'gpu': gpu,
    }
    return render(req, 'components/gpu_detail.html', context)
<<<<<<< HEAD
>>>>>>> 01cc471 (Add GPU)
=======

def RAMs_view(req):
    rams = RAM.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        rams = rams.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        rams = rams.filter(brand__in=selected_brands)

    # Фільтрація за обсягом
    selected_capacities = req.GET.getlist('capacity')
    if selected_capacities:
        rams = rams.filter(capacity__in=selected_capacities)

    # Фільтрація за типом пам'яті
    selected_ram_types = req.GET.getlist('ram_type')
    if selected_ram_types:
        rams = rams.filter(ram_type__in=selected_ram_types)

    # Фільтрація за частотою
    selected_frequencies = req.GET.getlist('frequency')
    if selected_frequencies:
        rams = rams.filter(frequency__in=selected_frequencies)

    # Фільтрація за кількістью модулів
    selected_number_of_modules = req.GET.getlist('num')
    if selected_number_of_modules:
        rams = rams.filter(number_of_modules__in=selected_number_of_modules)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        rams = rams.order_by('price')
    elif sort == 'price_desc':
        rams = rams.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Corsair', 'G.Skill', 'Kingston', 'Patriot']
    capacities = ['8','12','16','24','32', '64']
=======
>>>>>>> 0ac5604 (Add Storages to Database)
    ram_types = ['DDR4', 'DDR5']
    frequencies = ['2400', '2666', '3000', '3200', '4600', '4800', '5200', '5600', '6000']
    number_of_modules = ['1', '2']


    context = {
        'rams': rams,
        'brands': brands,
        'capacities': capacities,
        'ram_types': ram_types,
        'frequencies': frequencies,
        'number_of_modules': number_of_modules,
        'selected_brands': selected_brands,
        'selected_capacities': selected_capacities,
        'selected_ram_types': selected_ram_types,
        'selected_frequencies': selected_frequencies,
        'selected_number_of_modules': selected_number_of_modules,
    }

    return render(req, 'components/rams.html', context)

def ram_detail(req, ram_id):
    ram = RAM.objects.get(id=ram_id)
    context = {
        'ram': ram,
    }
    return render(req, 'components/ram_detail.html', context)
<<<<<<< HEAD
>>>>>>> ef1f7ff (Add RAM)
=======

def Storages_view(req):
    storages = Storage.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        storages = storages.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        storages = storages.filter(brand__in=selected_brands)

    # Фільтрація за обсягом
    selected_capacities = req.GET.getlist('capacity')
    if selected_capacities:
        storages = storages.filter(capacity__in=selected_capacities)

    # Фільтрація за типом накопичувача
    selected_storage_types = req.GET.getlist('storage_type')
    if selected_storage_types:
        storages = storages.filter(storage_type__in=selected_storage_types)

    # Фільтрація за швидкістю
    selected_speeds = req.GET.getlist('speed')
    if selected_speeds:
        speed_filter = Q()
        for speed in selected_speeds:
            min_speed, max_speed = map(float, speed.split('-'))
            speed_filter |= Q(speed__gte=min_speed, speed__lte=max_speed)
        storages = storages.filter(speed_filter)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        storages = storages.order_by('price')
    elif sort == 'price_desc':
        storages = storages.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Adata', 'Kingston', 'Samsung', 'Toshiba']
    capacities = ['128 GB','256 GB','512 GB','1 TB','2 TB', '4 TB']
    storage_types = ['HDD', 'SSD', 'NVMe']
    speeds = ['0-1000', '1001-2000', '2001-3000', '3001-4000', '4001-5000', '5001-6000', '6001-7000', '7001-8000', '8001-9000', '9001-10000']

    context = {
        'storages': storages,
        'brands': brands,
        'capacities': capacities,
        'storage_types': storage_types,
        'speeds': speeds,
        'selected_brands': selected_brands,
        'selected_capacities': selected_capacities,
        'selected_storage_types': selected_storage_types,
        'selected_speeds': selected_speeds,
    }

    return render(req, 'components/storages.html', context)

def storage_detail(req, storage_id):
    storage = Storage.objects.get(id=storage_id)
    context = {
        'storage': storage,
    }
    return render(req, 'components/storage_detail.html', context)
<<<<<<< HEAD
>>>>>>> 5fc22e5 (Add storages)
=======

def Coolers_view(req):
    coolers = Cooler.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        coolers = coolers.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        coolers = coolers.filter(brand__in=selected_brands)

    # Фільтрація за к-тю теплотрубок
    selected_heat_tube_numbers = req.GET.getlist('heat_tube_number')
    if selected_heat_tube_numbers:
        coolers = coolers.filter(heat_tube_number__in=selected_heat_tube_numbers)

    # Фільтрація за висотою
    selected_heights = req.GET.getlist('height')
    if selected_heights:
        height_filter = Q()
        for height in selected_heights:
            min_height, max_height = map(float, height.split('-'))
            height_filter |= Q(height__gte=min_height, height__lte=max_height)
        coolers = coolers.filter(height_filter)

    # Фільтрація за RGB
    selected_argbs = req.GET.getlist('argb')
    if 'З ARGB підсвіткою' in selected_argbs and 'Без ARGB підсвітки' not in selected_argbs:
        coolers = coolers.filter(argb=True)
    elif 'Без ARGB підсвітки' in selected_argbs and 'З ARGB підсвіткою' not in selected_argbs:
        coolers = coolers.filter(argb=False)

    # Фільтрація за максимальним TDP
    selected_max_tdps = req.GET.getlist('max_tdp')
    if selected_max_tdps:
        max_tdp_filter = Q()
        for max_tdp in selected_max_tdps:
            min_max_tdps, max_max_tdps = map(float, max_tdp.split('-'))
            max_tdp_filter |= Q(max_tdp__gte=min_max_tdps, max_tdp__lte=max_max_tdps)
        coolers = coolers.filter(max_tdp_filter)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        coolers = coolers.order_by('price')
    elif sort == 'price_desc':
        coolers = coolers.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Deepcool', 'Arctic', 'ID Cooling']
    heat_tube_numbers = ['4', '5', '6', '7']
    heights = ['51-100', '101-150', '151-200']
    argbs = ['З ARGB підсвіткою', 'Без ARGB підсвітки']
    max_tdps = ['0-100', '101-150', '151-200', '201-250']

    context = {
        'coolers': coolers,
=======
>>>>>>> a8316c4 (add sort)
        'brands': brands,
        'heat_tube_numbers': heat_tube_numbers,
        'heights': heights,
        'argbs': argbs,
        'max_tdps': max_tdps,
        'selected_brands': selected_brands,
        'selected_heat_tube_numbers': selected_heat_tube_numbers,
        'selected_heights': selected_heights,
        'selected_argbs': selected_argbs,
        'selected_max_tdps': selected_max_tdps,
    }

    return render(req, 'components/coolers.html', context)

def cooler_detail(req, cooler_id):
    cooler = Cooler.objects.get(id=cooler_id)
    context = {
        'cooler': cooler,
    }
    return render(req, 'components/cooler_detail.html', context)

def AIOs_view(req):
    aios = AIO.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        aios = aios.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        aios = aios.filter(brand__in=selected_brands)

    # Фільтрація за к-тю теплотрубок
    selected_heat_tube_numbers = req.GET.getlist('heat_tube_number')
    if selected_heat_tube_numbers:
        aios = aios.filter(heat_tube_number__in=selected_heat_tube_numbers)

    # Фільтрація за довжиною
    selected_sizes = req.GET.getlist('size')
    if selected_sizes:
        aios = aios.filter(size__in=selected_sizes)

    # Фільтрація за RGB
    selected_argbs = req.GET.getlist('argb')
    if 'З ARGB підсвіткою' in selected_argbs and 'Без ARGB підсвітки' not in selected_argbs:
        aios = aios.filter(argb=True)
    elif 'Без ARGB підсвітки' in selected_argbs and 'З ARGB підсвіткою' not in selected_argbs:
        aios = aios.filter(argb=False)

    # Фільтрація за максимальним TDP
    selected_max_tdps = req.GET.getlist('max_tdp')
    if selected_max_tdps:
        max_tdp_filter = Q()
        for max_tdp in selected_max_tdps:
            min_max_tdps, max_max_tdps = map(float, max_tdp.split('-'))
            max_tdp_filter |= Q(max_tdp__gte=min_max_tdps, max_tdp__lte=max_max_tdps)
        aios = aios.filter(max_tdp_filter)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        aios = aios.order_by('price')
    elif sort == 'price_desc':
        aios = aios.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Deepcool', 'Arctic', 'MSI']
    sizes = ['120', '240', '360']
    argbs = ['З ARGB підсвіткою', 'Без ARGB підсвітки']
    max_tdps = ['151-250', '251-350']

    context = {
        'aios': aios,
        'selected_sort': sort,
        'brands': brands,
        'sizes': sizes,
        'argbs': argbs,
        'max_tdps': max_tdps,
        'selected_brands': selected_brands,
        'selected_heat_tube_numbers': selected_heat_tube_numbers,
        'selected_sizes': selected_sizes,
        'selected_argbs': selected_argbs,
        'selected_max_tdps': selected_max_tdps,
    }

    return render(req, 'components/aios.html', context)

def aio_detail(req, aio_id):
    aio = AIO.objects.get(id=aio_id)
    context = {
        'aio': aio,
    }
    return render(req, 'components/aio_detail.html', context)
<<<<<<< HEAD
>>>>>>> 9d3cf93 (add coolers and aios)
=======

def PSUs_view(req):
    psus = PSU.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        psus = psus.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        psus = psus.filter(brand__in=selected_brands)

    # Фільтрація за ватами
    selected_wattages = req.GET.getlist('wattage')
    if selected_wattages:
        wattage_filter = Q()
        for wattage in selected_wattages:
            min_wattage, max_wattage = map(float, wattage.split('-'))
            wattage_filter |= Q(wattage__gte=min_wattage, wattage__lte=max_wattage)
        psus = psus.filter(wattage_filter)

    # Фільтрація за сертифікатом
    selected_certificates = req.GET.getlist('certificate')
    if selected_certificates:
        psus = psus.filter(certificate__in=selected_certificates)

    # Фільтрація за модульністю
    selected_modularities = req.GET.getlist('modular')
    if 'Модульний' in selected_modularities and 'Немодульний' not in selected_modularities:
        psus = psus.filter(modular=True)
    elif 'Немодульний' in selected_modularities and 'Модульний' not in selected_modularities:
        psus = psus.filter(modular=False)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        psus = psus.order_by('price')
    elif sort == 'price_desc':
        psus = psus.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Be Quiet!','Gigabyte', 'Deepcool', 'MSI']
    wattages = ['1000-1300', '900-1000', '800-850', '700-750', '600-650', '500-550', '400-450']
    certificates = ['80 Plus Titanium', '80 Plus Platinum', '80 Plus Gold', '80 Plus Silver', '80 Plus Bronze', 'Без сертифікату']
    modularities = ['Модульний', 'Немодульний']

    context = {
        'psus': psus,
        'selected_sort': sort,
        'brands': brands,
        'wattages': wattages,
        'certificates': certificates,
        'modularities': modularities,
        'selected_brands': selected_brands,
        'selected_wattages': selected_wattages,
        'selected_certificates': selected_certificates,
        'selected_modularities': selected_modularities,
    }

    return render(req, 'components/psus.html', context)

def psu_detail(req, psu_id):
    psu = PSU.objects.get(id=psu_id)
    context = {
        'psu': psu,
    }
    return render(req, 'components/psu_detail.html', context)
<<<<<<< HEAD
>>>>>>> 99cc666 (add PSUs)
=======

def Cases_view(req):
    cases = Case.objects.all()

    # Фільтрація за ціною
    min_price = req.GET.get('min_price', None)
    max_price = req.GET.get('max_price', None)
    if min_price and max_price:
        cases = cases.filter(price__gte=min_price, price__lte=max_price)

    # Фільтрація за брендом
    selected_brands = req.GET.getlist('brand')
    if selected_brands:
        cases = cases.filter(brand__in=selected_brands)

    # Фільтрація за форм фактором
    selected_form_factors = req.GET.getlist('form_factor')
    if selected_form_factors:
        cases = cases.filter(form_factor__in=selected_form_factors)

    # Фільтрація за кількістю вентиляторів
    selected_fans = req.GET.getlist('fans')
    if selected_fans:
        cases = cases.filter(fans__in=selected_fans)

    # Фільтрація за максимальною висотою кулера
    selected_max_cooler_heights = req.GET.getlist('max_cooler_height')
    if selected_max_cooler_heights:
        height_filter = Q()
        for height in selected_max_cooler_heights:
            min_height, max_height = map(float, height.split('-'))
            height_filter |= Q(max_cooler_height__gte=min_height, max_cooler_height__lte=max_height)
        cases = cases.filter(height_filter)

    # Фільтрація за максимальною довжиною СРО
    selected_max_aio_sizes = req.GET.getlist('max_aio_size')
    if selected_max_aio_sizes:
        cases = cases.filter(max_aio_size__in=selected_max_aio_sizes)

    # Фільтрація за наявністю скла
    selected_tempered_glasses = req.GET.getlist('tempered_glass')
    if 'Зі склом' in selected_tempered_glasses and 'Без скла' not in selected_tempered_glasses:
        cases = cases.filter(tempered_glass=True)
    elif 'Без скла' in selected_tempered_glasses and 'Зі склом' not in selected_tempered_glasses:
        cases = cases.filter(tempered_glass=False)

    # Сортування
    sort = req.GET.get('sort')
    if sort == 'price_asc':
        cases = cases.order_by('price')
    elif sort == 'price_desc':
        cases = cases.order_by('-price')

    # Варіанти для фільтрів
    brands = ['Be Quiet!','Gamemax', 'Deepcool', 'MSI']
    form_factors = ['ATX', 'Micro-ATX']
    fans_ch = ['0', '1', '3', '4']
    max_cooler_heights = ['0-100', '101-150', '151-200']
    max_aio_sizes = ['240', '360']
    tempered_glasses = ['Зі склом', 'Без скла']

    context = {
        'cases': cases,
        'selected_sort': sort,
        'brands': brands,
        'form_factors': form_factors,
        'fans_ch': fans_ch,
        'max_cooler_heights': max_cooler_heights,
        'max_aio_sizes': max_aio_sizes,
        'tempered_glasses': tempered_glasses,
        'selected_brands': selected_brands,
        'selected_form_factors': selected_form_factors,
        'selected_fans': selected_fans,
        'selected_max_cooler_heights': selected_max_cooler_heights,
        'selected_max_aio_sizes': selected_max_aio_sizes,
        'selected_tempered_glasses': selected_tempered_glasses,
    }

    return render(req, 'components/cases.html', context)

def case_detail(req, case_id):
    case = Case.objects.get(id=case_id)
    context = {
        'case': case,
    }
    return render(req, 'components/case_detail.html', context)
>>>>>>> 5b57886 (add cases)
