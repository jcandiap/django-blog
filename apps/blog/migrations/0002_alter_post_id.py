# Generated by Django 4.2.2 on 2023-06-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]