# Generated by Django 2.2.6 on 2020-03-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20200317_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='attempts',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]