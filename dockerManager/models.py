# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Instance(models.Model):
    domain = models.CharField(max_length=256)
    docker_id = models.CharField(max_length=128)
    ip = models.GenericIPAddressField(protocol='IPv4')
    port = models.IntegerField()
