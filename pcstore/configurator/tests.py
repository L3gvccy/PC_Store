from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from components.models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case
from .models import Configuration

class ConfiguratorViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            id=1,
            username='testuser',
            password='testpassword'
        )
        cls.user.save()
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
        cls.configuration = Configuration.objects.create(
            user=User.objects.get(id=1),
            cpu=cls.cpu,
            motherboard=cls.motherboard,
            gpu=cls.gpu,
            ram=cls.ram,
            storage=cls.storage,
            psu=cls.psu,
            cooler=cls.cooler,
            aio=cls.aio,
            case=cls.case
        )
    
    def test_select_cpu(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('select_cpu', args=[self.cpu.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('configurator'))

    def test_remove_cpu(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('remove_cpu'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('configurator'))

    def test_configurator_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('configurator'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('configuration', response.context)

    def test_incompatible_ram_and_motherboard(self):
        self.client.login(username='testuser', password='testpassword')

        incompatible_ram = RAM.objects.create(
            name="Corsair Vengeance LPX 32GB",
            display_name="Corsair Vengeance LPX 32GB",
            price=159.99,
            quantity=10,
            image="ram_corsair_32gb.jpg",
            brand="Corsair",
            capacity=32,
            ram_type="DDR5",
            frequency=3600,
            number_of_modules=2
        )

        self.configuration.ram = incompatible_ram
        self.configuration.save()

        response = self.client.get(reverse('configurator'))

        self.assertEqual(response.status_code, 200)
        self.assertIn("Обрана оперативна пам'ять не підходить до материнської плати!", response.context['ram_msg'])

    def test_configuration_update(self):
        self.client.login(username='testuser', password='testpassword')

        self.configuration.cpu = self.cpu
        self.configuration.motherboard = self.motherboard
        self.configuration.gpu = self.gpu
        self.configuration.save()

        response = self.client.get(reverse('configurator'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['configuration'].cpu, self.cpu)
        self.assertEqual(response.context['configuration'].motherboard, self.motherboard)
        self.assertEqual(response.context['configuration'].gpu, self.gpu)

    def test_inadequate_psu(self):
        self.client.login(username='testuser', password='testpassword')

        inadequate_psu = PSU.objects.create(
            name="Corsair RM550x",
            display_name="Corsair RM550x",
            price=89.99,
            quantity=10,
            image="psu_rm550x.jpg",
            brand="Corsair",
            series="RMx",
            wattage=550,
            certificate="80 Plus Gold",
            modular=True
        )

        self.configuration.psu = inadequate_psu
        self.configuration.save()

        response = self.client.get(reverse('configurator'))

        self.assertEqual(response.status_code, 200)
        self.assertIn("Блок живлення недостатньої потужності!", response.context['psu_msg'])