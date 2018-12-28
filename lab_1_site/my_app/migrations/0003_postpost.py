# Generated by Django 2.1.2 on 2018-12-28 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20181228_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_status', models.BooleanField(default=False)),
            ],
        ),
    ]
