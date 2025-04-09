from django.db import models
from django.contrib.auth.models import User


class Schema(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Схема данных'
        verbose_name_plural = 'Схемы данных'

    def __str__(self):
        return self.name


class Column(models.Model):
    TYPES = [
        ('full_name', 'Full Name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('domain', 'Domain'),
        ('phone', 'Phone Number'),
        ('company', 'Company'),
        ('text', 'Text'),
        ('integer', 'Integer'),
        ('address', 'Address'),
    ]

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns')
    name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=50, choices=TYPES)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Столбец'
        verbose_name_plural = 'Столбцы'
        ordering = ['order']

    def __str__(self):
        return self.name
