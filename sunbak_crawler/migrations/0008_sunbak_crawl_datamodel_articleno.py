# Generated by Django 4.2 on 2023-05-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunbak_crawler', '0007_sunbak_crawl_datamodel_price_int'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunbak_crawl_datamodel',
            name='articleNo',
            field=models.IntegerField(default=0),
        ),
    ]
