import os
import random

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'p6.settings')
django.setup()
from app1.models import Book

def populate(book_list):
    for name, author in book_list:
        year = random.randrange(1981, 2017)
        price = random.randrange(10, 100)
        book = Book(name=name, author=author, year=year, price=price)
        book.save()


book_list = [
    ['Python is good', 'Guido van Rossum'],
    ['Python is powerful', 'Guido van Rossum'],
    ['Linux essential', 'Linux Torwarld'],
    ['Shell programming', 'Richard M. Stallman'],
    ['Shell programming II', 'David MacKenzie'],
    ['Advanced Django Developing', 'Django Team'],
    ['Learning Python', 'Mark Lutz'],
    ['Programming Python', 'Mark Lutz'],
    ['Operatiing System', 'Andrew S. Tanenbaum'],
    ['Operatiing System II', 'Andrew S. Tanenbaum'],
]

populate(book_list)
