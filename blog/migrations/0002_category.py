# Generated by Django 3.2.16 on 2023-01-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('slug', models.SlugField()),
                ('posts', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]
