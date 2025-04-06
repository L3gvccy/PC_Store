from django.test import TestCase
<<<<<<< HEAD
from django.urls import reverse
from .models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case

class ComponentViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cpu = CPU.objects.create(
            name="Intel Core i9-12900K",
            display_name="Intel Core i9-12900K",
            price=589.99,
            quantity=10,
            image="cpu_i9_12900k.jpg",
            brand="Intel",
            socket="LGA 1700",
            cores=16,
            threads=24,
            frequency=3.2,
            TDP=125
        )
        cls.motherboard = Motherboard.objects.create(
            name="ASUS ROG Strix Z690",
            display_name="ASUS ROG Strix Z690",
            price=299.99,
            quantity=20,
            image="motherboard_z690.jpg",
            brand="ASUS",
            socket="LGA 1700",
            chipset="Intel Z690",
            form_factor="ATX",
            RAM_slots=4,
            RAM_type="DDR4",
            M2_slots=2,
            WiFi=True,
            Bluetooth=True
        )
        cls.gpu = GPU.objects.create(
            name="NVIDIA GeForce RTX 3080",
            display_name="MSI NVIDIA GeForce RTX 3080",
            price=699.99,
            quantity=15,
            image="gpu_rtx_3080.jpg",
            brand="MSI",
            gp_brand="Nvidia",
            series="RTX 30",
            memory=10,
            memory_type="GDDR6X",
            TDP=320
        )
        cls.ram = RAM.objects.create(
            name="Corsair Vengeance LPX 16GB",
            display_name="Corsair Vengeance LPX 16GB",
            price=79.99,
            quantity=30,
            image="ram_corsair_16gb.jpg",
            brand="Corsair",
            capacity=16,
            ram_type="DDR4",
            frequency=3200,
            number_of_modules=2
        )
        cls.storage = Storage.objects.create(
            name="Samsung 970 Evo 1TB",
            display_name="Samsung 970 Evo 1TB",
            price=149.99,
            quantity=25,
            image="storage_samsung_970_evo.jpg",
            brand="Samsung",
            capacity="1 TB",
            storage_type="SSD",
            speed=3500
        )
        cls.psu = PSU.objects.create(
            name="Corsair RM750x",
            display_name="Corsair RM750x",
            price=119.99,
            quantity=18,
            image="psu_rm750x.jpg",
            brand="Corsair",
            series="RMx",
            wattage=750,
            certificate="80 Plus Gold",
            modular=True
        )
        cls.cooler = Cooler.objects.create(
            name="Cooler Master Hyper 212",
            display_name="Cooler Master Hyper 212",
            price=35.99,
            quantity=40,
            image="cooler_master_212.jpg",
            brand="Cooler Master",
            heat_tube_number=4,
            height=160,
            argb=True,
            max_tdp=150
        )
        cls.aio = AIO.objects.create(
            name="NZXT Kraken X63",
            display_name="NZXT Kraken X63",
            price=149.99,
            quantity=12,
            image="aio_nzxt_kraken_x63.jpg",
            brand="NZXT",
            size=280,
            argb=True,
            max_tdp=280
        )
        cls.case = Case.objects.create(
            name="NZXT H510",
            display_name="NZXT H510",
            price=69.99,
            quantity=22,
            image="case_nzxt_h510.jpg",
            brand="NZXT",
            form_factor="Mid Tower",
            fans=2,
            max_cooler_height=165,
            max_aio_size=280,
            tempered_glass=True
        )
    
    def test_cpus_view(self):
        response = self.client.get(reverse('cpus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cpu.name)
        self.assertContains(response, str(self.cpu.price))
        self.assertContains(response, self.cpu.display_name)
        self.assertContains(response, self.cpu.image)
    
    def test_motherboards_view(self):
        response = self.client.get(reverse('motherboards'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.motherboard.name)
        self.assertContains(response, str(self.motherboard.price))
        self.assertContains(response, self.motherboard.display_name)
        self.assertContains(response, self.motherboard.image)

    def test_gpus_view(self):
        response = self.client.get(reverse('gpus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gpu.name)
        self.assertContains(response, str(self.gpu.price))
        self.assertContains(response, self.gpu.display_name)
        self.assertContains(response, self.gpu.image)

    def test_rams_view(self):
        response = self.client.get(reverse('rams'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ram.name)
        self.assertContains(response, str(self.ram.price))
        self.assertContains(response, self.ram.display_name)
        self.assertContains(response, self.ram.image)

    def test_storages_view(self):
        response = self.client.get(reverse('storages'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.storage.name)
        self.assertContains(response, str(self.storage.price))
        self.assertContains(response, self.storage.display_name)
        self.assertContains(response, self.storage.image)

    def test_psus_view(self):
        response = self.client.get(reverse('psus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.psu.name)
        self.assertContains(response, str(self.psu.price))
        self.assertContains(response, self.psu.display_name)
        self.assertContains(response, self.psu.image)

    def test_coolers_view(self):
        response = self.client.get(reverse('coolers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cooler.name)
        self.assertContains(response, str(self.cooler.price))
        self.assertContains(response, self.cooler.display_name)
        self.assertContains(response, self.cooler.image)

    def test_aios_view(self):   
        response = self.client.get(reverse('aios'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.aio.name)
        self.assertContains(response, str(self.aio.price))
        self.assertContains(response, self.aio.display_name)
        self.assertContains(response, self.aio.image)

    def test_cases_view(self):
        response = self.client.get(reverse('cases'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.case.name)
        self.assertContains(response, str(self.case.price))
        self.assertContains(response, self.case.display_name)
        self.assertContains(response, self.case.image)
    
    def test_cpu_detail_view(self):
        response = self.client.get(reverse('cpu_detail', args=[self.cpu.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cpu.name)
        self.assertContains(response, str(self.cpu.price))
        self.assertContains(response, self.cpu.display_name)
        self.assertContains(response, self.cpu.image)
        self.assertContains(response, self.cpu.brand)
        self.assertContains(response, self.cpu.socket)
        self.assertContains(response, self.cpu.cores)
        self.assertContains(response, self.cpu.threads)
        self.assertContains(response, self.cpu.frequency)
        self.assertContains(response, self.cpu.TDP)

    def test_motherboard_detail_view(self):
        response = self.client.get(reverse('motherboard_detail', args=[self.motherboard.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.motherboard.name)
        self.assertContains(response, str(self.motherboard.price))
        self.assertContains(response, self.motherboard.display_name)
        self.assertContains(response, self.motherboard.image)
        self.assertContains(response, self.motherboard.brand)
        self.assertContains(response, self.motherboard.socket)
        self.assertContains(response, self.motherboard.chipset)
        self.assertContains(response, self.motherboard.form_factor)
        self.assertContains(response, self.motherboard.RAM_slots)
        self.assertContains(response, self.motherboard.RAM_type)
        self.assertContains(response, self.motherboard.M2_slots)

    def test_gpu_detail_view(self):
        response = self.client.get(reverse('gpu_detail', args=[self.gpu.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gpu.name)
        self.assertContains(response, str(self.gpu.price))
        self.assertContains(response, self.gpu.display_name)
        self.assertContains(response, self.gpu.image)
        self.assertContains(response, self.gpu.brand)
        self.assertContains(response, self.gpu.gp_brand)
        self.assertContains(response, self.gpu.series)
        self.assertContains(response, self.gpu.memory)
        self.assertContains(response, self.gpu.memory_type)
        self.assertContains(response, self.gpu.TDP)

    def test_ram_detail_view(self):
        response = self.client.get(reverse('ram_detail', args=[self.ram.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ram.name)
        self.assertContains(response, str(self.ram.price))
        self.assertContains(response, self.ram.display_name)
        self.assertContains(response, self.ram.image)
        self.assertContains(response, self.ram.brand)
        self.assertContains(response, self.ram.capacity)
        self.assertContains(response, self.ram.ram_type)
        self.assertContains(response, self.ram.frequency)
        self.assertContains(response, self.ram.number_of_modules)

    def test_storage_detail_view(self):
        response = self.client.get(reverse('storage_detail', args=[self.storage.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.storage.name)
        self.assertContains(response, str(self.storage.price))
        self.assertContains(response, self.storage.display_name)
        self.assertContains(response, self.storage.image)
        self.assertContains(response, self.storage.brand)
        self.assertContains(response, self.storage.capacity)
        self.assertContains(response, self.storage.storage_type)
        self.assertContains(response, self.storage.speed)

    def test_psu_detail_view(self):
        response = self.client.get(reverse('psu_detail', args=[self.psu.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.psu.name)
        self.assertContains(response, str(self.psu.price))
        self.assertContains(response, self.psu.display_name)
        self.assertContains(response, self.psu.image)
        self.assertContains(response, self.psu.brand)
        self.assertContains(response, self.psu.series)
        self.assertContains(response, self.psu.wattage)
        self.assertContains(response, self.psu.certificate)

    def test_cooler_detail_view(self):
        response = self.client.get(reverse('cooler_detail', args=[self.cooler.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cooler.name)
        self.assertContains(response, str(self.cooler.price))
        self.assertContains(response, self.cooler.display_name)
        self.assertContains(response, self.cooler.image)
        self.assertContains(response, self.cooler.brand)
        self.assertContains(response, self.cooler.heat_tube_number)
        self.assertContains(response, self.cooler.height)
        self.assertContains(response, str(self.cooler.max_tdp))

    def test_aio_detail_view(self):
        response = self.client.get(reverse('aio_detail', args=[self.aio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.aio.name)
        self.assertContains(response, str(self.aio.price))
        self.assertContains(response, self.aio.display_name)
        self.assertContains(response, self.aio.image)
        self.assertContains(response, self.aio.brand)
        self.assertContains(response, self.aio.size)
        self.assertContains(response, str(self.aio.max_tdp))

    def test_case_detail_view(self):
        response = self.client.get(reverse('case_detail', args=[self.case.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.case.name)
        self.assertContains(response, str(self.case.price))
        self.assertContains(response, self.case.display_name)
        self.assertContains(response, self.case.image)
        self.assertContains(response, self.case.brand)
        self.assertContains(response, self.case.form_factor)
        self.assertContains(response, self.case.fans)
        self.assertContains(response, self.case.max_cooler_height)
        self.assertContains(response, self.case.max_aio_size)

    def test_cpu_filtering(self):
        response = self.client.get(reverse('cpus'), {'cores': '16'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cpu.name)
        
    def test_motherboard_filtering(self):
        response = self.client.get(reverse('motherboards'), {'brand': 'ASUS'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.motherboard.name)

    def test_gpu_filtering(self):
        response = self.client.get(reverse('gpus'), {'gp_brand': 'Nvidia'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gpu.name)

    def test_ram_filtering(self):
        response = self.client.get(reverse('rams'), {'capacity': '32'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.ram.name)

    def test_storage_filtering(self):
        response = self.client.get(reverse('storages'), {'capacity': '2 TB'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.storage.name)

    def test_psu_filtering(self):
        response = self.client.get(reverse('psus'), {'brand': 'Corsair'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.psu.name)

    def test_cooler_filtering(self):
        response = self.client.get(reverse('coolers'), {'height': '150-200'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cooler.name)

    def test_aio_filtering(self):
        response = self.client.get(reverse('aios'), {'size': '280'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.aio.name)

    def test_case_filtering(self):  
        response = self.client.get(reverse('cases'), {'brand': 'MSI'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.case.name)
=======

# Create your tests here.
>>>>>>> 67d780e (add header)
