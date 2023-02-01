# Generated by Django 4.1.5 on 2023-02-01 12:25

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('phone', models.CharField(max_length=12, verbose_name='phone')),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='lat login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.models.MyUserManager()),
            ],
        ),
    ]
