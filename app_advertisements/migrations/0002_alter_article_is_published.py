# Generated by Django 5.0.2 on 2024-03-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликована'),
        ),
    ]