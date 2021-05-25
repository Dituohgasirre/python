#!/usr/bin/env python3


import sys
from model import Model


class View_Student(Model):
    id = Model.Field()
    sname = Model.Field()
    cname = Model.Field()
    oname = Model.Field()


class Student(Model):
    id = Model.Field(primary=True)
    sid = Model.Field()
    cid = Model.Field()
    name = Model.Field()
    gender = Model.Field()
    phone = Model.Field()
    remark = Model.Field()
    md5sum = Model.Field()

