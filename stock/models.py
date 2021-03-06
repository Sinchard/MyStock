from django.db import models
from django.urls import reverse

from basic.models import CommonInfo, Warehouse
from asset.models import Device, Material
from user.models import UserProfile


class DeviceOperate(CommonInfo):
    operate_choice = (
        (1, '入库'),
        (2, '出库'),
    )
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="设备")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="所在仓库")
    employee = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="入库人")
    operate = models.IntegerField(default=1, choices=operate_choice, verbose_name="操作")
    location = models.CharField(max_length=50, blank=True,null=True, verbose_name="安装地点")

    def get_absolute_url(self):
        return reverse('stock:edit_devicein', args=[str(self.id)])

    def __str__(self):
        return self.device.sn + ' ' + self.employee.name

    class Meta:
        verbose_name = '设备入库表'
        verbose_name_plural = '设备入库表'


class MaterialIn(CommonInfo):
    material = models.ForeignKey(
        Material,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    amount = models.DecimalField(default=0,
                                 max_digits=10,
                                 decimal_places=2,
                                 verbose_name="数量")
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    employee = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.material.name.name + ' ' + self.employee.name

    def get_warehouse_display(self):
        if self.warehouse:
            return self.warehouse.name
        else:
            return ''

    def get_employee_display(self):
        if self.employee:
            return self.employee.name
        else:
            return ''

    class Meta:
        verbose_name = '材料入库表'
        verbose_name_plural = '材料入库表'



class Application(CommonInfo):
    status_choice = (
        (1, u'已提交'),
        (2, u'已审批'),
        (3, u'已出库'),
        (4, u'已确认'),
    )
    name = models.CharField(max_length=50, blank=True,null=True, db_index=True)
    applicant = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,blank=True,null=True,related_name='applicants')
    status = models.IntegerField(default=1, choices=status_choice)
    approver = models.ManyToManyField(UserProfile)
    approve_content = models.CharField(max_length=50, blank=True,null=True,)
    approve_date = models.DateTimeField(blank=True,null=True,)
    confirmed = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,blank=True,null=True, related_name='confirmeds')
    confirm_content = models.CharField(max_length=50, blank=True,null=True,)
    confirm_date = models.DateTimeField(blank=True,null=True,)

    def __str__(self):
        return self.name

    def get_employee_display(self):
        if self.employee:
            return self.employee.name
        else:
            return ""

    def get_approve_date_display(self):
        return time2str(self.approve_date)

    def get_confirm_date_display(self):
        return time2str(self.confirm_date)

    def dict(self):
        d = {'id': self.id,
             'name': self.name,
             'employee': self.employee.name, 'employeeId': self.employee.id,
             'status': self.status}
        approve = self.approve.all()
        if self.approve_content != '':
            for tmp in approve:
                d.update({'approveId': tmp.id, 'approveName': tmp.name,
                          'approveContent': self.approve_content, 'approve_date': time2str(self.approve_date)})
        d.update(super(Application, self).dict())
        return d

    class Meta:
        verbose_name = u'设备申请表'
        verbose_name_plural = u'设备申请表'
        ordering = ['-modify_date', '-approve_date', '-confirm_date']


class ApplicationDetail(CommonInfo):
    application = models.ForeignKey(Application, on_delete=models.CASCADE,blank=True,null=True, related_name='details')
    name = models.CharField(max_length=50, blank=True,null=True, db_index=True)
    number = models.IntegerField(blank=True,null=True,)
    location = models.CharField(max_length=50, blank=True,null=True,)
    is_device = models.BooleanField(default=True)
    devices = models.ManyToManyField(Device)

    def __str__(self):
        # return self.name+'-'+str(self.number)+'-'+self.location
        return self.get_display()

    def get_display(self):
        return u'{0}/{1}/{2}'.format(self.name, self.number, self.location)

    def dict(self):
        d = {'id': self.id,
             'application': self.application.name, 'applicationId': self.application.id,
             'name': self.name, 'number': self.number,
             'location': self.location}
        d.update(super(ApplicationDetail, self).dict())
        return d

    class Meta:
        verbose_name = u'申请详情表'
        verbose_name_plural = u'申请详情表'

'''
# device manager is the employee who's role = 4
class StockOut(CommonInfo):
    device = models.ForeignKey(Device, null=True)
    applicationdetail = models.ForeignKey(ApplicationDetail)
    location = models.CharField(max_length=50, db_index=True)
    operator = models.ForeignKey(Employee, related_name='operators_set', null=True)
    operate_date = models.DateTimeField(blank=True, null=True)
    confirm = models.ForeignKey(Employee, related_name='confirms_set', null=True)
    confirm_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.applicationdetail.application.name + ' ' + self.applicationdetail.device

    def get_applicationdetail_display(self):
        if self.applicationdetail:
            return str(self.applicationdetail)
        else:
            return ""

    def get_employee_display(self):
        if self.applicationdetail:
            return self.applicationdetail.application.employee.name
        else:
            return ""

    def get_device_display(self):
        if self.device:
            return self.device.get_device_display()
        else:
            return ''

    def get_operator_display(self):
        if self.operator:
            return self.operator.name
        else:
            return ""

    def get_operate_date_display(self):
        return time2str(self.operate_date)

    def records(self):
        d = {'id': self.id,
             'deviceId': self.device.id, 'device': self.device.name.name + '/' + self.device.model.name + '/' + self.device.sn,
             'op': 'OUT', 'employee': self.applicationdetail.application.employee.name,
             'location': self.location}
        d.update(super(StockOut, self).dict())
        return d

    def dict(self):
        d = {'id': self.id,
             'application': self.applicationdetail.application.name, 'applicationId': self.applicationdetail.application.id,
             'detailId': self.applicationdetail.id, 'requiredDevice': self.applicationdetail.device,
             'location': self.location}
        if self.device:
            d.update({'device': self.device.name.name + ' ' + self.device.model.name + ' ' + self.device.sn,
                      'deviceId': self.device.id})
        else:
            d.update({'device': '', 'deviceId': 0})

        if self.operator:
            d.update({'operator': self.operator.name, 'operatorId': self.operator.id,
                      'operate_date': time2str(self.operate_date), })
        else:
            d.update({'operator': '', 'operatorId': 0,
                      'operate_date': time2str(self.operate_date), })

        if self.confirm:
            d.update({'confirm': self.confirm.name, 'confirmId': self.confirm.id,
                      'confirm_date': time2str(self.confirm_date)})
        else:
            d.update({'confirm': '', 'confirmId': 0,
                      'confirm_date': time2str(self.confirm_date)})

        d.update(super(StockOut, self).dict())
        return d

    class Meta:
        verbose_name = u'出库表'
        verbose_name_plural = u'出库表'
        ordering = ['-operate_date']
'''
