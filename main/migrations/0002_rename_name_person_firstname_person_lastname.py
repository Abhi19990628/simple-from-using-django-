# Generated by Django 5.0.4 on 2024-04-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='person',
            name='lastname',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
