# Generated by Django 4.1.6 on 2023-02-05 03:25

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('web_link', models.CharField(max_length=150)),
                ('description', django_quill.fields.QuillField()),
                ('technology', models.CharField(max_length=150)),
                ('featured_image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
