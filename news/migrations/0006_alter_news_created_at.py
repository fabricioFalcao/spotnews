# Generated by Django 4.2.3 on 2024-06-10 17:58

from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0005_alter_news_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(
                validators=[news.validators.validate_empty_field]
            ),
        ),
    ]
