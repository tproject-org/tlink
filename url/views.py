from django.shortcuts import render, redirect

from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.

from .models import URL
from .serializers import URLSerializer
from .shorten import short

# ViewSets define the view behavior.
class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


def url_redirect(request, slugs):
    data = URL.objects.get(short_url=slugs)
    data.number_of_view += 1
    return redirect(data.url)


from .forms import UrlForm

from .models import URL
def register_url(request):
    form = UrlForm(request.POST)
    token = " "
    if request.method == "POST":
        if form.is_valid():
            print("FORM IS VALID ?")
            new_url = form.cleaned_data
            token = short().issue_token()
            if new_url["short_url"] == "":
                print("EMPTY")
                print("no short url")
                new_url["short_url"] = token
            else:
                print("SLUG IS HERE")
                token = new_url["short_url"]
            if URL.objects.filter(short_url=token).exists():
                print("ALREADY EXIST")
                message = "Slug already exist"
                token = short().issue_token()
                new_url["short_url"] = token
                success = False
            else:
                print("SUCCESS")
                success = True
                message = "Url registered"
            print("RETURN")
            new_url["owner"] = request.user
            URL.objects.create(**new_url)
            return render(request, "url/success.html", {"token": token, "success": success, "message": message})
    else:
        form = UrlForm()
        token = " Invalid Url"
        return render(request, "url/register_url.html", {"form": form, "token": token})
