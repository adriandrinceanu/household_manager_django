# Generated by Django 5.0.3 on 2024-03-21 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_member_family_family_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='core.member'),
        ),
    ]
