# Generated by Django 2.2 on 2019-04-03 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_name', models.CharField(max_length=50)),
                ('movie_title', models.CharField(max_length=100)),
                ('rating', models.IntegerField(max_length=5)),
                ('review', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
