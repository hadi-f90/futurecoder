# Generated by Django 2.2.7 on 2020-01-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191117_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codeentry',
            name='step',
        ),
        migrations.RemoveField(
            model_name='user',
            name='step',
        ),
        migrations.AddField(
            model_name='codeentry',
            name='page_slug',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codeentry',
            name='step_name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='page_slug',
            field=models.CharField(default='IntroducingTheShell', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='step_name',
            field=models.CharField(default='first_expression', max_length=128),
        ),
    ]
