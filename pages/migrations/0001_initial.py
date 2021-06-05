# Generated by Django 3.2 on 2021-06-03 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='character_Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='name')),
                ('clas', models.CharField(default=None, max_length=255, verbose_name='class')),
                ('race', models.CharField(default=None, max_length=255, verbose_name='race')),
                ('level', models.IntegerField(default=None, verbose_name='level')),
                ('sheet', models.JSONField(verbose_name='character sheet')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
