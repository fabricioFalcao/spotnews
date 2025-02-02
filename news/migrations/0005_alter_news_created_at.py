# Generated by Django 4.2.3 on 2024-06-10 17:57

from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_alter_news_author_alter_news_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateTimeField(
                validators=[news.validators.validate_empty_field]
            ),
        ),
    ]
