# Generated by Django 2.2 on 2020-04-20 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(blank=True, null=True, upload_to='attachment/%Y/%m/%d', verbose_name='附件')),
                ('check', models.BooleanField(choices=[(True, '已审核'), (False, '未审核')], default=False, verbose_name='是否审核')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '类型表',
                'verbose_name_plural': '类型表',
            },
        ),
        migrations.CreateModel(
            name='CategoryShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(blank=True, null=True, upload_to='attachment/%Y/%m/%d', verbose_name='附件')),
                ('check', models.BooleanField(choices=[(True, '已审核'), (False, '未审核')], default=False, verbose_name='是否审核')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.Category')),
            ],
            options={
                'verbose_name': '分类字典映射表',
                'verbose_name_plural': '分类字典映射表',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(blank=True, null=True, upload_to='attachment/%Y/%m/%d', verbose_name='附件')),
                ('check', models.BooleanField(choices=[(True, '已审核'), (False, '未审核')], default=False, verbose_name='是否审核')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='名称')),
                ('location', models.CharField(max_length=50, unique=True, verbose_name='位置')),
            ],
            options={
                'verbose_name': '库房表',
                'verbose_name_plural': '库房表',
            },
        ),
        migrations.CreateModel(
            name='Wordbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(blank=True, null=True, upload_to='attachment/%Y/%m/%d', verbose_name='附件')),
                ('check', models.BooleanField(choices=[(True, '已审核'), (False, '未审核')], default=False, verbose_name='是否审核')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='名称')),
                ('categories', models.ManyToManyField(through='basic.CategoryShip', to='basic.Category', verbose_name='分类')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.Wordbook', verbose_name='上一级')),
            ],
            options={
                'verbose_name': '字典表',
                'verbose_name_plural': '字典表',
            },
        ),
        migrations.AddField(
            model_name='categoryship',
            name='wordbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.Wordbook'),
        ),
    ]