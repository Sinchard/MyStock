# Generated by Django 2.2 on 2020-04-28 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20200427_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceoperate',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='安装地点'),
        ),
        migrations.AlterField(
            model_name='deviceoperate',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.Device', verbose_name='设备'),
        ),
        migrations.AlterField(
            model_name='deviceoperate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserProfile', verbose_name='入库人'),
        ),
        migrations.AlterField(
            model_name='deviceoperate',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.Warehouse', verbose_name='所在仓库'),
        ),
    ]
