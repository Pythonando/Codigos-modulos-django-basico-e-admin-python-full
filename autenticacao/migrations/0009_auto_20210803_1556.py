# Generated by Django 3.2.5 on 2021-08-03 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0008_auto_20210803_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='pedidos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='pessoa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.pessoa'),
            preserve_default=False,
        ),
    ]