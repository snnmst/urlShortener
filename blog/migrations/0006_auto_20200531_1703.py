# Generated by Django 3.0.6 on 2020-05-31 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_short_urls_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='short_urls',
            old_name='clickedDate',
            new_name='createdDate',
        ),
    ]