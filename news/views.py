from django.shortcuts import render, redirect
from news.forms import CategoryForm
from news.models import News, Category

# Create your views here.
def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)

def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)

def categories(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}
    return render(request, 'categories_form.html', context)