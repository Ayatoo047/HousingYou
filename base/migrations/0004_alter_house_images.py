# Generated by Django 4.1.5 on 2023-04-22 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_houseimages_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.houseimages'),
        ),
    ]
