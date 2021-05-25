from django.db import models


# 1. 创建一个名叫Contact的模型，有四个字段: name, gender, age, phone
# 2. 把应用注册到项目中
# 3. 为模型的变动创建migration
# 4. 查看migration对应的SQL
# 5. 把migration应用到数据库

class Contact(models.Model):
    name = models.CharField(max_length=64)
    gender = models.IntegerField(default=1)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return '%s [%s]' % (self.name, self.age)


class Book(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(default=0)
    pubtime = models.DateTimeField(auto_now_add=True, null=True)
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=11)

    def __str__(self):
        return '%s [%s,%s,%s]' % (self.name, self.year, self.price, self.author)


class Author(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    gender = models.IntegerField(default=1)

    def __str__(self):
        return '%s [%s,%s,%s]' % (self.name, self.year, self.price, self.author)
