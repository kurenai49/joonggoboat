# Generated by Django 4.2 on 2023-05-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunbak_crawler', '0015_remove_sunbak_crawl_datamodel_tons'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunbak_crawl_datamodel',
            name='tons',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
