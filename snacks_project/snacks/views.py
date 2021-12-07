from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView,
    DetailView, DeleteView,
    CreateView, UpdateView
)
from .models import Snacks
from django.urls import reverse_lazy


class SnacksViews(TemplateView):
    template_name = 'home.html'


class AboutUs(TemplateView):
    template_name = 'aboutUs.html'


class SnackListViews(ListView):
    template_name = 'snack_list.html'
    model = Snacks


class SnackDetail(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks


class UpdateSnack(UpdateView):
    template_name = 'update_snack.html'
    model = Snacks
    fields = ['title', 'description']


class CreateSnack(CreateView):
    template_name = 'create_snack.html'
    model = Snacks
    fields = ['title', 'description', 'purchaser']

class DeleteSnack(DeleteView):
    template_name = 'delete_snack.html'
    model = Snacks
    success_url = reverse_lazy('snack_list')
