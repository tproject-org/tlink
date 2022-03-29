from django.shortcuts import render, redirect

from rest_framework import viewsets

# Create your views here.

from .models import URL
from .serializers import URLSerializer

# ViewSets define the view behavior.
class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


def url_redirect(request, slugs):
    data = URL.objects.get(short_url=slugs)
    return redirect(data.url)

from .forms import UrlForm

def register_url(request):
  form = UrlForm(request.POST) 
  token = " "
  if request.method == 'POST': 
    if form.is_valid():
      NewUrl = form.save(commit=False) 
      token = short().issue_token() 
      NewUrl.short_url = token 
      NewUrl.save() 
  else:
      form = UrlForm() 
      token = " Invalid Url" 
      return render(request, 'home.html', {'form': form, 'token': token})