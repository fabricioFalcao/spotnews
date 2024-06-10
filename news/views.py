from django.shortcuts import render
from news.models import News

# Create your views here.
def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)

def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)
