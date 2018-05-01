# Generated by Django 2.0.1 on 2018-05-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):


    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weight', models.IntegerField(default=1)),
                ('is_select', models.BooleanField(default=True)),
                ('is_trainee', models.BooleanField(default=False)),
                ('is_enabled', models.BooleanField(default=False)),
            ],
        ),
    ]