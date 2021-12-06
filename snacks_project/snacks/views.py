from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from .models import Snacks


class SnacksViews(TemplateView):
    template_name = 'home.html'

class SnackListViews(ListView):
    template_name = 'snack_list.html'
    model = Snacks

class SnackDetail(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks

class AboutUs(TemplateView):
    template_name = 'aboutUs.html'
