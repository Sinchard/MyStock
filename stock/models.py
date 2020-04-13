from django.db import models

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

    def get_create_date_display(self):
        return time2str(self.create_date)

    class Meta:
        app_label = 'stock'
        abstract = True
        ordering = ['-modify_date']


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
