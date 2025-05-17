from django.test import TestCase, Client
from menus.models import MenuItem


class MenuTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.home = MenuItem.objects.create(
            title='Главная', url='/', menu_name='main_menu')
        self.about = MenuItem.objects.create(
            title='О нас', url='/about/', menu_name='main_menu')
        self.team = MenuItem.objects.create(
            title='Команда', url='/team/', menu_name='main_menu',
            parent=self.about)

    def test_menu_item_str(self):
        self.assertEqual(str(self.home), 'Главная')

    def test_menu_visible_on_page(self):
        response = self.client.get('/team/')
        self.assertContains(response, 'Главная')
        self.assertContains(response, 'О нас')
        self.assertContains(response, 'Команда')
        self.assertContains(response, 'active')
