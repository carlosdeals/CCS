from django.shortcuts import render

from django.views.generic import ListView
from .models import Media


class media_page_view(ListView):
    model = Media
    template_name = 'product_detail.html'