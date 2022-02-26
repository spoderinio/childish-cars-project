# Generated by Django 4.0.2 on 2022-02-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carmodel', '0003_alter_carmodel_car_brand'),
        ('carbrand', '0002_alter_carbrand_created_at_alter_carbrand_deleted_at'),
        ('usercar', '0002_alter_usercar_created_at_alter_usercar_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercar',
            name='car_brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carbrand.carbrand'),
        ),
        migrations.AlterField(
            model_name='usercar',
            name='car_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carmodel.carmodel'),
        ),
        migrations.AlterField(
            model_name='usercar',
            name='user',
            field=models.CharField(max_length=60, verbose_name='User Name'),
        ),
    ]