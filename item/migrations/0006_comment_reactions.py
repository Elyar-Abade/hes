# Generated by Django 5.1.6 on 2025-02-23 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_remove_reaction_inferior_remove_reaction_superior_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reactions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='item.reaction'),
        ),
    ]
