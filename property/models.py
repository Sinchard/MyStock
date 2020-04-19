from django.db import models

from base.models import CommonInfo, Wordbook
from stock.models import Warehouse


class Device(CommonInfo):
    status_choice = (
        (1, '在库中'),
        (2, '已出库'),
    )
    good_choice = (
        (1, '故障'),
        (5, '良好'),
    )
    brand = models.ForeignKey(Wordbook, blank=True, on_delete=models.SET_NULL, related_name='device_brands',
                              null=True, verbose_name="名称")
    model = models.ForeignKey(Wordbook, blank=True, on_delete=models.SET_NULL, related_name='device_models',
                              null=True, verbose_name="型号")
    sn = models.CharField(max_length=100, verbose_name="设备编码", db_index=True)
    classification = models.ForeignKey(Wordbook, blank=True, on_delete=models.SET_NULL, related_name='device_classifications',
                                       null=True, verbose_name="类型")
    good = models.IntegerField(default=5, choices=good_choice, verbose_name="设备状态")
    value = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, verbose_name="价格")
    asset = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name="资产编码")
    sap = models.CharField(max_length=100, blank=True,
                           null=True, verbose_name="SAP")
    status = models.IntegerField(
        default=1, choices=status_choice, verbose_name="状态")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL,
                                  blank=True, null=True, verbose_name="所在库房")
    location = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="位置")

    def __str__(self):
        return self.brand.name + '/' + self.model.name + '/' + self.sn  # + ' ' + self.category.name

    def get_device_display(self):
        return u'{0}/{1}/{2}'.format(self.brand.name, self.model.name, self.sn)

    def get_type_display(self):
        if self.type:
            return self.type.get_type_display()
        else:
            return ""

    def autocomplateFormate(self):
        return {'label': self.name.name + '/' + self.model.name + '/' + self.sn, 'value': self.id}

    def dict(self):
        if self.warehouse is None:
            self.warehouse = Warehouse(id=0, name='')

        d = {'id': self.id,
             'sn': self.sn,
             'name': self.name.name, 'nameId': self.name.id,
             'model': self.model.name, 'modelId': self.model.id,
             'type': self.type.name, 'typeId': self.type.id,
             'good': str(self.good),
             'asset': self.asset,
             'sap': self.sap,
             'status': self.status,
             'warehouse': self.warehouse.name, 'warehouseId': self.warehouse.id,
             'location': self.location}
        d.update(super(Device, self).dict())
        return d

    def get_absolute_url(self):
        return reverse('property:edit_device', args=[str(self.id)])

    class Meta:
        verbose_name = '设备表'
        verbose_name_plural = '设备表'


class Material(CommonInfo):
    classification = models.ForeignKey(Wordbook, blank=True, on_delete=models.SET_NULL, related_name='material_classifications',
                                       null=True, verbose_name="类型")
    name = models.ForeignKey(Wordbook, blank=True, on_delete=models.SET_NULL, related_name='material_names',
                             null=True, verbose_name="名称")
    amount = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, verbose_name="数量")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL,
                                  blank=True, null=True, verbose_name="所在库房")

    def get_absolute_url(self):
        return reverse('property:edit_material', args=[str(self.id)])

    class Meta:
        verbose_name = '材料表'
        verbose_name_plural = '材料表'
