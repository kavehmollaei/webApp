# Generated by Django 4.0.4 on 2022-05-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/default.jpg', upload_to='blog/'),
        ),
    ]
