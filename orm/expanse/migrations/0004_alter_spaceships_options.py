# Generated by Django 3.2.4 on 2021-06-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expanse', '0003_spaceships_is_broken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spaceships',
            options={'ordering': ('-name',), 'permissions': (('can_mark_broken', 'Set ship as broken'),)},
        ),
    ]
