# Generated by Django 3.2 on 2021-05-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_rename_tag_tag_name'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='unique-tag',
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('name',), name='unique-tag'),
        ),
    ]
