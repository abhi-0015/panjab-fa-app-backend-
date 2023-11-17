# Generated by Django 4.2.4 on 2023-10-31 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend_apis', '0007_userprofile_referral_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReferralCode',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('referrals_count', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]