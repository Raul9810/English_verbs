# Generated by Django 2.2.6 on 2020-03-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20200317_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='practice',
            field=models.IntegerField(null=True),
        ),
    ]
