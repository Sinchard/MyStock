from django.db import models

from stock.models import CommonInfo


class Wordbook(CommonInfo):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name=u"名称",
                            db_index=True)
    parent = models.ForeignKey("self",
                               null=True,
                               verbose_name=u"父类",
                               on_delete=models.SET_NULL)

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
