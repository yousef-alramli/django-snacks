from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

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
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res , "aboutUs.html")
        self.assertTemplateUsed(res , "_base.html")