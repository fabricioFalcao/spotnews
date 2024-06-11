from django.shortcuts import render, redirect
from rest_framework import viewsets
from news.forms import CategoryForm, NewsForm
from news.models import News, Category
from news.serializers import CategorySerializer

# Create your views here.
def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)


def categories_form(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}
    return render(request, 'categories_form.html', context)


def news_form(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home-page")
        
    context = {"form": form}
    return render(request, 'news_form.html', context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
