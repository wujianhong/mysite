# Generated by Django 2.0.4 on 2018-05-02 04:03

from django.db import migrations, models


class Migration(migrations.Migration):


    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
