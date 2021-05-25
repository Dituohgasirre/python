#!/usr/bin/env python3


import sys
from model import Model


class Class(Model):
    id = Model.Field(primary=True)
    sid = Model.Field()
    name = Model.Field()
    remark = Model.Field()
    md5sum = Model.Field()

