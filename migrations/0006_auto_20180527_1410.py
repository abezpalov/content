# Generated by Django 2.0.5 on 2018-05-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20180527_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
    ]
