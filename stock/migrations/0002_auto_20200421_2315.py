# Generated by Django 2.2 on 2020-04-21 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
        ('basic', '0004_auto_20200421_2254'),
        ('user', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockIn',
            new_name='DeviceIn',
        ),
        migrations.AlterModelOptions(
            name='devicein',
            options={'verbose_name': '设备入库表', 'verbose_name_plural': '设备入库表'},
        ),
        migrations.CreateModel(
            name='MaterialIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(blank=True, null=True, upload_to='attachment/%Y/%m/%d', verbose_name='附件')),
                ('check', models.BooleanField(choices=[(True, '已审核'), (False, '未审核')], default=False, verbose_name='是否审核')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='数量')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserProfile')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.Material')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.Warehouse')),
            ],
            options={
                'verbose_name': '材料入库表',
                'verbose_name_plural': '材料入库表',
            },
        ),
    ]