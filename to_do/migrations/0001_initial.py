# Generated by Django 4.2.3 on 2023-07-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('deadline_datetime', models.DateTimeField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(to='to_do.tag')),
            ],
        ),
    ]
