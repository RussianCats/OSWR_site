# Generated by Django 5.1.1 on 2024-11-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='discout',
            new_name='discount',
        ),
    ]
