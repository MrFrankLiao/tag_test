# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.db.models import Q, Count
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="user")
    msg = RichTextField('message', default='')
    create_time = models.DateTimeField('create_time', auto_now_add=True, default=datetime.date.today())
    tags = TaggableManager()

    def __unicode__(self):
        return u"%s" % self.msg

    class Meta:
        verbose_name = u'留言'
