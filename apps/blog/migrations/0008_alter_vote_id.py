# Generated by Django 4.2.2 on 2023-06-14 02:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_vote_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
