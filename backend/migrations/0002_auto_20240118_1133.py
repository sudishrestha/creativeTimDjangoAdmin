# Generated by Django 3.2.23 on 2024-01-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(max_length=1),
        ),
    ]
