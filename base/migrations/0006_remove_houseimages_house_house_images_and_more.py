# Generated by Django 4.1.5 on 2023-04-24 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_house_options_remove_house_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseimages',
            name='house',
        ),
        migrations.AddField(
            model_name='house',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.houseimages'),
        ),
        migrations.AddField(
            model_name='houseimages',
            name='for_house',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
