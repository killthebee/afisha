# Generated by Django 3.0.4 on 2020-06-04 17:57

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20200604_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='test_field',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
