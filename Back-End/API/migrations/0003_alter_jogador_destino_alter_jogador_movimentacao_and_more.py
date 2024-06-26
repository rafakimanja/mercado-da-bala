# Generated by Django 5.0.6 on 2024-05-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_jogador_movimentacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='destino',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='movimentacao',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='origem',
            field=models.CharField(max_length=30),
        ),
    ]
