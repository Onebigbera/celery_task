# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 08:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('a_info', models.CharField(max_length=200, verbose_name='文章描述')),
                ('a_content', models.TextField(verbose_name='文章内容')),
                ('a_img', models.ImageField(blank=True, max_length=150, null=True, upload_to='media/arts_ups/%Y/%m', verbose_name='封面')),
                ('a_createtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加时间')),
                ('a_price', models.IntegerField(default=0, verbose_name='单价')),
                ('a_flag', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='控制字段')),
            ],
            options={
                'verbose_name': '小说',
                'verbose_name_plural': '小说',
                'db_table': 'art',
                'ordering': ['-a_createtime'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='章节标题')),
                ('content', models.TextField(verbose_name='小说章节内容')),
                ('create_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加时间')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Art', verbose_name='小说')),
            ],
            options={
                'verbose_name': '小说章节',
                'verbose_name_plural': '小说章节',
                'db_table': 'art_chapter',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=20, verbose_name='文章标签')),
                ('t_info', models.CharField(max_length=50, verbose_name='标签描述')),
                ('t_createtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='创建时间')),
                ('t_flag', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='控制字段')),
                ('operator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='api操作者')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'tag',
                'ordering': ['-t_createtime'],
            },
        ),
        migrations.AddField(
            model_name='art',
            name='a_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Tag', verbose_name='关联文章标签'),
        ),
        migrations.AddField(
            model_name='art',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='api操作者'),
        ),
    ]
