# Generated by Django 2.0.5 on 2018-07-05 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=10, null=True, verbose_name='级别')),
                ('company_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='capital', to='annotate.Company', verbose_name='资方')),
                ('company_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipient', to='annotate.Company', verbose_name='受方')),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='专利编号')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='专利名')),
                ('author', models.CharField(blank=True, max_length=20, null=True, verbose_name='著作人')),
                ('status', models.CharField(choices=[('PUBLIC', '公开'), ('PRIVATE', '私有保护'), ('EXPIRED', '过期')], max_length=10, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='TechSynonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='词条名')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotate.Tech', verbose_name='技术通名')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AddField(
            model_name='patent',
            name='tech',
            field=models.ManyToManyField(to='annotate.Tech', verbose_name='技术关键词'),
        ),
        migrations.AddField(
            model_name='news',
            name='finance',
            field=models.ManyToManyField(to='annotate.Finance', verbose_name='投融资关系'),
        ),
        migrations.AddField(
            model_name='news',
            name='tech',
            field=models.ManyToManyField(to='annotate.Tech', verbose_name='技术关键词'),
        ),
    ]