# Generated by Django 3.2.4 on 2021-06-12 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expanse', '0004_alter_spaceships_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spaceships',
            options={'ordering': ('-name',)},
        ),
    ]