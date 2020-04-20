from django.db import models
from django.contrib.auth.models import User

from basic.models import Wordbook, CommonInfo


class Role(CommonInfo):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name=u"名称",
                            db_index=True)

    def __unicode__(self):
        return self.name

    def dict(self):
        d = {'id': self.id, 'name': self.name}
        d.update(super(Role, self).dict())
        return d

    class Meta:
        verbose_name = u'角色表'
        verbose_name_plural = u'角色表'


class UserProfile(CommonInfo):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    name = models.CharField('姓名', max_length=50, blank=True, null=True)
    department = models.ForeignKey(Wordbook,
                                   on_delete=models.SET_NULL,
                                   related_name='dep_users',
                                   blank=True,
                                   null=True)
    team = models.ForeignKey(Wordbook,
                             on_delete=models.SET_NULL,
                             related_name='team_users',
                             blank=True,
                             null=True)
    role = models.ForeignKey(Role,
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True,
                             verbose_name=u"角色")
    phone = models.CharField('固定电话', max_length=50, blank=True, null=True)
    mobile = models.CharField('电话', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = '用户信息'

    def __str__(self):
        return self.user.__str__()
