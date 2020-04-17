from django.db import models
from django.urls import reverse
from stock.models import CommonInfo


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
        return reverse('base:edit_category', args=[str(self.id)])

    class Meta:
        verbose_name = u'类型表'
        verbose_name_plural = u'类型表'


class Wordbook(CommonInfo):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name=u"名称",
                            db_index=True)
    parent = models.ForeignKey("self",
                               null=True,
                               blank=True,
                               verbose_name=u"上一级",
                               on_delete=models.SET_NULL)
    categories = models.ManyToManyField(
        Category,
        through='CategoryShip',
        through_fields=('wordbook', 'category'),
        verbose_name=u"分类",
    )

    def __str__(self):
        return self.name

    def get_type_display(self):
        return self.name

    def dict(self):
        d = {'id': self.id, 'name': self.name}
        d.update(super(DeviceType, self).dict())
        return d

    class Meta:
        verbose_name = u'字典表'
        verbose_name_plural = u'字典表'


class CategoryShip(CommonInfo):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    wordbook = models.ForeignKey(Wordbook, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'分类字典映射表'
        verbose_name_plural = u'分类字典映射表'