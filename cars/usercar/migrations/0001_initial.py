# Generated by Django 4.0.2 on 2022-02-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=60)),
                ('car_brand', models.CharField(max_length=60)),
                ('car_model', models.CharField(max_length=60)),
                ('first_reg', models.DateField()),
                ('odometer', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
    ]