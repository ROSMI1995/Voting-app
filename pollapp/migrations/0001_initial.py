# Generated by Django 4.0.6 on 2023-02-03 06:04

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
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=30)),
                ('option_two', models.CharField(max_length=30)),
                ('option_three', models.CharField(max_length=30)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
