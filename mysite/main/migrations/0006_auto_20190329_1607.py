# Generated by Django 2.1.7 on 2019-03-29 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190329_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 29, 16, 7, 36, 435915), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='image',
            field=models.ImageField(default='cimage.png', upload_to='img'),
        ),
    ]