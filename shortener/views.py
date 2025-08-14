from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import URL

def home(request):
    short_url = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_instance = form.save()
            short_url = request.build_absolute_uri('/') + url_instance.short_code
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url})

def redirect_url(request, code):
    url_instance = get_object_or_404(URL, short_code=code)
    return redirect(url_instance.original_url)
