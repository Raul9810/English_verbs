# Generated by Django 2.2.6 on 2020-03-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_word_practice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='practice',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
