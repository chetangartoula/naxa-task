# Generated by Django 4.1.5 on 2023-01-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naxa', '0002_district_municipality_province_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name_district',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='name_municipality',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='province',
            name='name_province',
            field=models.CharField(max_length=255),
        ),
    ]