# Generated by Django 5.0.4 on 2024-04-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
