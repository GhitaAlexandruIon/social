# Generated by Django 3.0.2 on 2020-02-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
    ]
