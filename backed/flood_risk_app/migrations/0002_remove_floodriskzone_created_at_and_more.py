# Generated by Django 5.0.6 on 2024-06-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood_risk_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floodriskzone',
            name='created_at',
        ),
        migrations.AddField(
            model_name='floodriskzone',
            name='max_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='floodriskzone',
            name='min_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='floodriskzone',
            name='classified_raster',
            field=models.FileField(upload_to='vector_data/'),
        ),
        migrations.AlterField(
            model_name='floodriskzone',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
