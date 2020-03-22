# Generated by Django 3.0.4 on 2020-03-22 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dormitory_number', models.IntegerField(max_length=2)),
                ('Floor_amount', models.IntegerField(max_length=1)),
                ('address', models.CharField(max_length=200)),
                ('Amount_of_rooms', models.IntegerField(max_length=5)),
            ],
            options={
                'verbose_name': 'Гуртожиток',
                'verbose_name_plural': 'Гуртожитки',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Floor_number', models.IntegerField(max_length=2)),
                ('Number_of_rooms', models.IntegerField(max_length=5)),
                ('Dormitory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DormitoryManagement.Dormitory')),
            ],
            options={
                'verbose_name': 'Поверх',
                'verbose_name_plural': 'Поверхи',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_number', models.IntegerField(max_length=5)),
                ('Amount_of_places', models.IntegerField(max_length=1)),
                ('Floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DormitoryManagement.Floor')),
            ],
            options={
                'verbose_name': 'Кімната',
                'verbose_name_plural': 'Кімнати',
            },
        ),
    ]
