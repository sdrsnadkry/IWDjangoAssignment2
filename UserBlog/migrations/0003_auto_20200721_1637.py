# Generated by Django 3.0.7 on 2020-07-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserBlog', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog'),
        ),
    ]
