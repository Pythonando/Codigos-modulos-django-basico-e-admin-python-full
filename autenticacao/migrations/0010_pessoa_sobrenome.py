# Generated by Django 3.2.5 on 2021-08-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0009_auto_20210803_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='sobrenome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
