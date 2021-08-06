# Generated by Django 3.2.5 on 2021-08-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_auto_20210806_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
