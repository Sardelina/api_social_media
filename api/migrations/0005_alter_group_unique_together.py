# Generated by Django 4.1 on 2022-08-29 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_post_group_alter_group_title_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set(),
        ),
    ]
