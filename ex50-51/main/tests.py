from django.test import TestCase
from django.core.urlresolvers import reverse


class StaticViewTests(TestCase):

    def test_404(self):
        response = self.client.get(reverse('home') + 'doesnt_exist/')
        self.assertEqual(response.status_code, 404)

    def test_index_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "I just wanted")

    def test_change_exists(self):
        response = self.client.get(reverse('change'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fill Out This Form")

    def test_form_submit(self):
        response = self.client.post(reverse('form_handle'), {'greeting': "Hello", 'name': "World"})
        self.assertEqual(response.status_code, 302)
