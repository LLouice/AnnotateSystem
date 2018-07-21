# Generated by Django 2.0.5 on 2018-07-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0004_finance_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='关键词')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='来源'),
        ),
        migrations.AddField(
            model_name='keywords',
            name='news',
            field=models.ManyToManyField(to='annotate.News', verbose_name='新闻'),
        ),
        migrations.AddField(
            model_name='keywords',
            name='patent',
            field=models.ManyToManyField(to='annotate.Patent', verbose_name='专利'),
        ),
    ]
