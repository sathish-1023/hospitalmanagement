# Generated by Django 4.0 on 2022-12-02 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='made_by',
        ),
    ]
