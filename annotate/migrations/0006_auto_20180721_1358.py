# Generated by Django 2.0.5 on 2018-07-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0005_auto_20180721_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeywodsCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='关键词')),
                ('news', models.ManyToManyField(to='annotate.News', verbose_name='新闻')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KeywodsTech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='关键词')),
                ('news', models.ManyToManyField(to='annotate.News', verbose_name='新闻')),
                ('patent', models.ManyToManyField(to='annotate.Patent', verbose_name='专利')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='keywords',
            name='news',
        ),
        migrations.RemoveField(
            model_name='keywords',
            name='patent',
        ),
        migrations.DeleteModel(
            name='Keywords',
        ),
    ]
