# Generated by Django 4.2 on 2023-05-18 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunbak_crawler', '0014_sunbak_crawl_datamodel_tons_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sunbak_crawl_datamodel',
            name='tons',
        ),
    ]
