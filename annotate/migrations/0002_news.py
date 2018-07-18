# Generated by Django 2.0.5 on 2018-07-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.PositiveIntegerField(max_length=6, primary_key=True, serialize=False, verbose_name='编号')),
                ('title', models.CharField(blank=True, max_length=70, null=True, verbose_name='标题')),
                ('link', models.URLField(blank=True, null=True, verbose_name='链接')),
                ('company', models.ManyToManyField(to='annotate.Company', verbose_name='企业')),
            ],
        ),
    ]