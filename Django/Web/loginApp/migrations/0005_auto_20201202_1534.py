# Generated by Django 3.1.3 on 2020-12-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0004_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
