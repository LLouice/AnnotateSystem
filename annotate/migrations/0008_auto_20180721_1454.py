# Generated by Django 2.0.5 on 2018-07-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0007_auto_20180721_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='keywordscompany',
            name='news',
            field=models.ManyToManyField(blank=True, to='annotate.News', verbose_name='新闻'),
        ),
        migrations.AlterField(
            model_name='keywordstech',
            name='news',
            field=models.ManyToManyField(blank=True, to='annotate.News', verbose_name='新闻'),
        ),
        migrations.AlterField(
            model_name='keywordstech',
            name='patent',
            field=models.ManyToManyField(blank=True, to='annotate.Patent', verbose_name='专利'),
        ),
    ]