# Generated by Django 3.2.5 on 2021-08-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0010_pessoa_sobrenome'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(default=1, upload_to='foto'),
            preserve_default=False,
        ),
    ]