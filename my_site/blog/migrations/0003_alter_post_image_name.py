# Generated by Django 4.1.6 on 2023-03-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_tags_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.FileField(upload_to='images'),
        ),
    ]
