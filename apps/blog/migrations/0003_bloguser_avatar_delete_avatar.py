# Generated by Django 4.2.2 on 2023-06-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230612_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]