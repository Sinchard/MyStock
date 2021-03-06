# Generated by Django 2.2 on 2020-04-21 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20200421_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordbook',
            name='parents',
        ),
        migrations.CreateModel(
            name='WorkbookShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='basic.Wordbook', verbose_name='词典条目')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parents', to='basic.Wordbook', verbose_name='父节点')),
            ],
            options={
                'verbose_name': '字典关系映射表',
                'verbose_name_plural': '字典关系映射表',
            },
        ),
    ]
