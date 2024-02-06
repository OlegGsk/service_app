from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )
    plan_type = models.CharField(max_length=10, choices=PLAN_TYPES)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[MaxValueValidator(100)])

    def __str__(self):
        return f'{self.get_plan_type_display()} plan'


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT,
                               related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.PROTECT,
                                related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT,
                             related_name='subscriptions')

    def __str__(self):
        return f'{self.client} - {self.service} - {self.plan}'
