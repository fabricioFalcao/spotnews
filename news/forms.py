from django import forms
from news.models import News

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nome")

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem",
        }
        widgets = {
            "author": forms.Select(),
            "created_at": forms.DateInput(attrs={"type": "date"}),
            "image": forms.FileInput(attrs={"class": "input-file"}),
            "categories": forms.CheckboxSelectMultiple(),
        }