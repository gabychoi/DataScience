# Generated by Django 3.1.3 on 2020-12-02 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0003_auto_20201202_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='time_photo/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.signup')),
            ],
            options={
                'db_table': 'photo_db',
                'ordering': ['-created'],
            },
        ),
    ]
