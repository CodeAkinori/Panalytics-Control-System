# Generated by Django 5.0.3 on 2024-03-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_feita', models.IntegerField(default=0)),
                ('quantidade_vendida', models.IntegerField(default=0)),
                ('preco_unitario', models.DecimalField(decimal_places=2, default=0.4, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Bread',
        ),
    ]