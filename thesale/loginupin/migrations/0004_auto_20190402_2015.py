# Generated by Django 2.1.7 on 2019-04-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginupin', '0003_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.EmailField(max_length=254),
        ),
    ]
