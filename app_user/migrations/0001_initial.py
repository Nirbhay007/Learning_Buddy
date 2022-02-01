# Generated by Django 3.1.7 on 2021-03-14 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(
                    blank=True, default='resource/default.jpeg', upload_to='resource/profile_images')),
                ('full_name', models.CharField(default='none', max_length=500)),
                ('phone', models.CharField(default='none', max_length=500)),
                ('email', models.CharField(default='none', max_length=500)),
                ('bio', models.TextField(default='none')),
                ('account_type', models.CharField(default='none', max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]