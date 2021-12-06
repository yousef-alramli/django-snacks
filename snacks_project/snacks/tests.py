from django.test import SimpleTestCase , TestCase
from django.urls import reverse


class SnacksTest(SimpleTestCase):
    def test_home_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)


    def test_about_us_status(self):
        url = reverse('about-us')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    
    def test_home_temp(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res , "home.html")
        self.assertTemplateUsed(res , "_base.html")


    def test_about_us_temp(self):
        url = reverse('about-us')
        res = self.client.get(url)
        self.assertTemplateUsed(res , "aboutUs.html")
        self.assertTemplateUsed(res , "_base.html")


class SnacksViewsTest(TestCase):
    def test_snacks_list_status(self):
        url = reverse('snack_list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_snacks_list_templete(self):
        url = reverse('snack_list')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'snack_list.html')