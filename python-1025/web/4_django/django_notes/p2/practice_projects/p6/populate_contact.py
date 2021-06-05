import os
import random

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'p6.settings')
django.setup()
from app1.models import Contact

def populate(name_list):
    for name, gender in name_list:
        age = random.randrange(18, 26)
        char8 = random.randrange(10000000, 99999999)
        phone = '138%s' % char8
        contact = Contact(name=name, gender=gender, age=age, phone=phone)
        contact.save()


name_list = [
    ['张柱', 1],
    ['金士坤', 1],
    ['何小伟', 1],
    ['李林青', 1],
    ['温利娜', 0],
    ['谢昌兴', 1],
    ['曾召杰', 1],
    ['陈靖', 1],
    ['郭志鹏', 1],
    ['陈志煌', 1],
    ['吴焕彬', 1],
    ['简玉龙', 1],
    ['张鹏', 1],
    ['曾祥明', 1],
    ['何大伟', 1],
    ['方正', 1],
    ['彭振健', 1],
    ['司徒春添', 1],
    ['陈志', 1],
    ['凌兴华', 1],
    ['瞿杨', 1],
    ['张鼎华', 1],
    ['刘波', 1],
    ['冯家业', 1],
    ['黄启健', 1],
    ['蔡庆祥', 1],
    ['杨甫成', 1],
    ['陈俊安', 1],
    ['廖海山', 1],
    ['高泽潮', 1],
    ['吴玉辉', 1],
    ['莫海滩', 1],
    ['银涛', 1],
    ['刘嘉伟', 1],
    ['占子炜', 1],
    ['李泽文', 1],
    ['李伟枫', 1],
    ['黎运云', 1],
    ['杜再强', 1]
]

populate(name_list)
