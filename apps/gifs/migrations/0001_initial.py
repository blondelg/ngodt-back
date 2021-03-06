# Generated by Django 3.2 on 2021-05-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('P', 'pending'), ('A', 'accepted'), ('R', 'rejected')], default='P', max_length=1)),
                ('uid', models.CharField(max_length=32)),
                ('gif', models.ImageField(upload_to='gifs/%Y/%m')),
            ],
        ),
        migrations.AddConstraint(
            model_name='gif',
            constraint=models.UniqueConstraint(fields=('uid',), name='unique-uid'),
        ),
    ]
