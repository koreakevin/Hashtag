# Generated by Django 2.2.1 on 2019-06-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velvet', '0004_auto_20190602_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
