#!/usr/bin/env python3


import sys
from model import Model


class School(Model):
    id = Model.Field(primary=True)
    name = Model.Field()
    description = Model.Field()
    location = Model.Field()
    remark = Model.Field()
    md5sum = Model.Field()

