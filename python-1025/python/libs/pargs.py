#!/usr/bin/env python3

import sys

class Parse:
    def __init__(self, args=None, optlist=None):
        self.optlist = []
        if optlist is not None:
            self.parseList(optlist)
        self.args = sys.argv if args == None else args
        self.len = len(self.args)
        self.index = 0
        self.result = {}

    def parseList(self, optlist):
        """
            "a"            set('a')
            "a||1"         set('a', types=1)
            "a||2"         set('a', types=2)
            "a||2"         set('a', types=2)
            "a|list|2"     set('a', 'list', types=2)
            "a|list|2"     set('a', 'list', types=2)
            "a|list|1"     set('a', 'list', types=1)
            "a|list"       set('a', 'list')
            "|list|1"      set('', 'list', 1)
            "|list"        set(longs='list')

            a1tsw2i        [a||1, t, s, w||2, i]
        """
        if type(optlist) == str:
            o = []
            for c in optlist:
                if c in "012":
                    c = o.pop() + "||" + c
                o.append(c)
            return self.parseList(o)

        for o in optlist:
            o = [int(x) if x and x in "012" else x for x in o.split("|")]
            self.set(*o)

    def set(self, short='', longs='', types=0):
        o = {}
        o['short'] = short
        o['long'] = longs
        o['type'] = types
        o['value'] = None
        self.optlist.append(o)

        return self

    def setValue(self, o, opt):
        o['value'] = True
        if o['type'] == 2 and opt.find('=') != -1:
            o['value'] = opt.split('=')[1]
        elif o['type'] == 1:
            if self.index == len(self.args) - 1:
                raise ValueError("%s: 必须指定参数值" % opt)
            #  print("set index: ", self.index, ", o: ", o, ", opt: ", opt)
            o['value'] = self.args[self.index + 1]
            del self.args[self.index]
            self.len -= 1

        name = o['long'] if o['long'] else o['short']
        self.result[name] = o['value']

    def longHandle(self, opt):
        for o in self.optlist:
            if (o['long'] and (opt.startswith("--" + o['long'] + '=')
                               or opt == '--' + o['long'])):
                #  print("long o = ", o, ", opt = ", opt)
                self.setValue(o, opt)

    def shortHandle(self, opt):
        if len(opt) > 2: #多个短选项 -tls => -t -l -s
            for c in opt:
                if c == '-':
                    continue
                self.shortHandle("-" + c)
        else:
            for o in self.optlist:
                if opt[1] == o['short']:
                    self.setValue(o, opt)

    def handle(self, opt):
        if opt.startswith('--'):
            self.longHandle(opt)
        else:
            self.shortHandle(opt)

    def parse(self):
        while self.index < self.len:
            #  print("index = ", self.index, ", args: ", self.args, ", opt: ", self.args[self.index])
            if self.args[self.index][0] == '-':
                #  print(self.args[self.index])
                self.handle(self.args[self.index])
                del self.args[self.index]
                self.len -= 1
            else:
                self.index += 1

        return self.args, self.result

    def __call__(self):
        return self.parse()

def parse(optlist, args=None):
    return Parse(args, optlist)()

if __name__ == "__main__":
    #  args = cp -r -t -w --list --name --age /kyo/file1 file2 /kyo
    #  args = /kyo/file1 file2 /kyo
    args, opt = Parse(None, ['a|list|1', 'n', '|name|2', 'w||1'])()
    #  args, opt = Parse(args, "a1tsw2i")
    #  g.set('a', 'age').set('n', 'name', 1)
    #  g.set('l', 'list', 2)
    #  g.set('r')
    #  g.set('w', types=1)
    #  g.set('t', types=2)
    #  args, opt = g.parse()
    print(args, opt)
