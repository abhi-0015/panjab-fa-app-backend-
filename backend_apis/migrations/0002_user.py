# Generated by Django 4.2.4 on 2023-10-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]