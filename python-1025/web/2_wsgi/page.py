#!/usr/bin/env python3

import math

class Page:
    def __init__(self, qs, total=0, size=15, roll=11, **kwargs):
        """
        qs      URL查询字符串的字典
        total   数据列表总数
        size    每页显示多少条
        roll    给用户显示多少页
        """
        self.now = int(qs.get('page', '1'))
        self.total = total
        self.size = size
        self.roll = roll
        self.rollMid = roll // 2 + 1

        #  前5页显示:   1 2 3 4 5 6 7 8 9 10 11 >> 100 总记录数: 100条
        #  超过5页显示: 1 << 2 3 4 5 6 7 8 9 10 11 12 >> 100 总记录数: 100条
        #  超过10页显示: 1 << 6 7 8 9 10 11 12 13 14 15 16 >> 100 总记录数: 100条
        #  倒数5页显示: 1 << 90 91 92 93 94 95 96 97 98 99 100  总记录数: 100条

    def limit(self):
        return "limit %s, %s" % ((self.now - 1) * self.size, self.size)

    def url(self, page):
        """
        组合url
        """
        return '?page=%s' % page

    def first(self):
        """
        首页
        """
        if self.now > self.rollMid and self.totalPage > self.roll:
            return '<li><a href="%s">1</a></li>' % (self.url(1))
        return ''

    def up(self):
        """
        上一页
        """
        if self.now > self.rollMid and self.totalPage > self.roll:
            return """<li><a href="%s" aria-label="Previous">
                          <span aria-hidden="true">&laquo;</span>
                      </a></li>""" % self.url(self.now - 1)
        return ''

    def down(self):
        """
        下一页
        """
        if (self.totalPage > self.roll
                and self.now <= self.totalPage - self.rollMid):
            return """<li><a href="%s" aria-label="Next">
                          <span aria-hidden="true">&raquo;</span>
                      </a></li>""" % self.url(self.now + 1)
        return ''

    def last(self):
        """
        尾页显示
        """
        if (self.totalPage > self.roll
                and self.now <= self.totalPage - self.rollMid):
            return ('<li><a href="%s">%s</a></li>'
                        % (self.url(self.totalPage), self.totalPage))
        return ''

    def num(self):
        """
        中间数字链接
        """
        loopNum = self.roll if self.totalPage >= self.roll else self.totalPage
        start = 1
        if self.totalPage > self.roll:
            if self.now > self.rollMid:
                start = self.now - self.rollMid + 1
            if self.now > self.totalPage - self.rollMid:
                start = self.totalPage - self.roll + 1

        html = ""
        for i in range(loopNum):
            i = i + start
            active = 'class="active"' if self.now == i else ''
            html += '<li %s><a href="%s">%s</a></li>' % (active, self.url(i), i)

        return html

    def fetch(self):
        """
        返回页码显示的html代码
        """
        self.totalPage = math.ceil(self.total / self.size)

        html = '<nav aria-label="Page navigation" class="row text-center">'
        html += '<ul class="pagination">'
        html += self.first()
        html += self.up()
        html += self.num()
        html += self.down()
        html += self.last()
        html += """<li><a href="#">总记录数:
                     <span style="color:red">%s</span> 条
                   </a></li>""" % self.total
        html += '</ul></nav>'

        return html

if __name__ == '__main__':
    print(Page({'page': 2}, 995).fetch())

