# Generated by Django 3.1.1 on 2020-12-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('adhaarNo', models.CharField(blank=True, max_length=20)),
                ('contactNo', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('village', models.CharField(blank=True, max_length=30)),
                ('mandal', models.CharField(blank=True, max_length=30)),
                ('district', models.CharField(blank=True, max_length=30)),
                ('pincode', models.CharField(blank=True, max_length=10)),
                ('poNo', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=10)),
                ('latitude', models.CharField(blank=True, max_length=10)),
                ('devNo', models.CharField(blank=True, max_length=20)),
                ('conMake', models.CharField(blank=True, max_length=30)),
                ('sNo', models.CharField(blank=True, max_length=20)),
                ('stages', models.CharField(blank=True, max_length=10)),
                ('dateInst', models.DateField()),
                ('InstName', models.CharField(blank=True, max_length=50)),
                ('pumpMfg', models.CharField(blank=True, max_length=30)),
                ('pvMake', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
