# Generated by Django 2.1.7 on 2019-03-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='endedor',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='vendedor',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
