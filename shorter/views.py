from django.shortcuts import render, redirect
from .models import Link
import validators
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def url_new(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if validators.url(url):
            link = Link.objects.create(url=url, user=request.user)
            return redirect('url_success', key=link.key)
        else:
            messages.error(request, 'Invalid URL')
            return render(request, 'shorter/url_new.html', {'error_message': 'URL inválida', 'url': url})
    return render(request, 'shorter/url_new.html')


def url_success(request, key):
    link = Link.objects.get(key=key)
    return render(request, 'shorter/url_show.html', {'link': link})


def url_redirect(request, key):
    try:
        link = Link.objects.get(key=key)
        if request.META.get('HTTP_HOST', '') not in link.url:
            return redirect(link.url)

        return redirect("/show/"+link.key)

    except Link.DoesNotExist:
        return redirect("url_new")


@login_required(login_url='login')
def url_list(request):
    urls = Link.objects.filter(user=request.user)
    return render(request, 'shorter/url_list.html', {'urls': urls})
