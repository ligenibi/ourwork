# Generated by Django 2.1.7 on 2019-04-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_name', models.CharField(max_length=50, verbose_name='用户名')),
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户排名')),
                ('user_phone', models.CharField(max_length=50, verbose_name='邮箱')),
                ('user_password', models.CharField(max_length=50, verbose_name='密码')),
            ],
        ),
    ]
