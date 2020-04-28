from django.db import models
from django.urls import reverse

from basic.utils import time2str, str2time


class CommonInfo(models.Model):
    check_choice = (
        (True, u'已审核'),
        (False, u'未审核'),
    )
    #history = AuditlogHistoryField()

    attach = models.FileField(upload_to='attachment/%Y/%m/%d',
                              verbose_name='附件',
                              blank=True,
                              null=True)
    check = models.BooleanField(default=False,
                                choices=check_choice,
                                verbose_name=u"是否审核")
    create_date = models.DateTimeField(blank=True,
                                       null=True,
                                       auto_now_add=True,
                                       verbose_name=u"创建时间")
    modify_date = models.DateTimeField(blank=True,
                                       null=True,
                                       auto_now=True,
                                       verbose_name=u"修改时间")
    description = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   verbose_name=u"备注")

    def dict(self):
        return {
            'create_date': time2str(self.create_date),
            'check': self.check,
            'description': self.description
        }

    @property
    def created(self):
        return time2str(self.create_date)

    @property
    def modified(self):
        return time2str(self.modify_date)

    def get_create_date_display(self):
        return time2str(self.create_date)

    class Meta:
        app_label = 'stock'
        abstract = True
        ordering = ['-modify_date']


class Category(CommonInfo):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name=u"名称",
                            db_index=True)

    def __str__(self):
        return self.name

    def get_type_display(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic:edit_category', args=[str(self.id)])

    class Meta:
        verbose_name = u'类型表'
        verbose_name_plural = u'类型表'


# 用来存出重复的内容，例如各种分类、品牌型号、部门班组
class Wordbook(CommonInfo):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name=u"名称",
                            db_index=True)

    def __str__(self):
        return self.name

    def get_type_display(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic:edit_wordbook', args=[str(self.id)])

    class Meta:
        verbose_name = u'字典表'
        verbose_name_plural = u'字典表'


# 建立多对多映射关系，例如某个品牌可以同时存在于设备、材料等分类中
class WordbookShip(models.Model):
    item = models.ForeignKey(Wordbook, null=True, blank=True, verbose_name="词典条目", on_delete=models.CASCADE, related_name="items")
    parent = models.ForeignKey(Wordbook, null=True, blank=True, verbose_name="父节点", on_delete=models.SET_NULL, related_name="parents")

    class Meta:
        verbose_name = '字典关系映射表'
        verbose_name_plural = '字典关系映射表'


class Warehouse(CommonInfo):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name=u"名称",
                            db_index=True)
    location = models.CharField(max_length=50, unique=True, verbose_name=u"位置")

    def __str__(self):
        return self.name + ' ' + self.location

    def get_warehouse_dispaly(self):
        return self.name

    def dict(self):
        d = {'id': self.id, 'name': self.name, 'location': self.location}
        d.update(super(Warehouse, self).dict())
        return d

    class Meta:
        verbose_name = u'库房表'
        verbose_name_plural = u'库房表'
