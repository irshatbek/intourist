# Generated by Django 4.0 on 2021-12-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_feedback_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='places'),
        ),
    ]
