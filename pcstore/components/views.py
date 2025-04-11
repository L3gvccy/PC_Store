from django.shortcuts import render
from .models import CPU
from .forms import CPUFilterForm

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
        cpus = cpus.filter(frequency__in=selected_frequencies)

    sort = req.GET.get('sort')
    
    if sort == 'price_asc':
        cpus = cpus.order_by('price')
    elif sort == 'price_desc':
        cpus = cpus.order_by('-price')

    selected_brands = req.GET.getlist('brand')
    selected_sockets = req.GET.getlist('socket')
    selected_cores = req.GET.getlist('cores')
    selected_threads = req.GET.getlist('cores')
    selected_freqs = req.GET.getlist('cores')

    brands = ['Intel', 'AMD']
    sockets = ['AM4', 'AM5', '1851', '1700', '1200', '1151']
    cores = ['6', '8', '10', '12', '14', '16', '24']
    threads = ['8', '12', '16', '20', '32']
    frequencies = ['2-2.5', '2.6-3', '3.1-3.6', '3.7-4.2', '4.3+']

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