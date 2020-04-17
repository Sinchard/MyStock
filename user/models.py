from django.db import models
from django.contrib.auth.models import User

from base.models import Wordbook


class UserProfile(models.Model):
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
    phone = models.CharField('固定电话', max_length=50, blank=True, null=True)
    mobile = models.CharField('电话', max_length=50, blank=True, null=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = '用户信息'

    def __str__(self):
        return self.user.__str__()
