# Generated by Django 4.2.7 on 2023-11-16 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_apis', '0008_userreferralcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReferrals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referralcode', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend_apis.userprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='UserReferralCode',
        ),
    ]
