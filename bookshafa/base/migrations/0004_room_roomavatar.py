# Generated by Django 4.2.5 on 2023-11-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomavatar',
            field=models.ImageField(default='roomphoto.png', null=True, upload_to=''),
        ),
    ]
