from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import PanelView
from .forms import PanelForm


class TestUrl(SimpleTestCase):
    def test_panel_url(self):
        url = reverse('home:panel')
        self.assertEqual(resolve(url).func.view_class, PanelView)


class TestPanelForm(SimpleTestCase):
    def test_valid_data(self):
        form = PanelForm(data={'username': 'demo', 'password': 'demo'})
        self.assertTrue(form.is_valid())

    def test_wrong_password(self):
        form = PanelForm(data={'username': 'demo', 'password': 'aaa'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_wrong_username(self):
        form = PanelForm(data={'username': 'aaa', 'password': 'demo'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_empty_data(self):
        form = PanelForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


