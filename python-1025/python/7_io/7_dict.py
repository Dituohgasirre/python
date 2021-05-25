#!/usr/bin/env python3


import hashlib
import os
import pickle


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

class Dict:

    def __init__(self, dictfile):
        tmpdata = "/tmp/dict.data"

        if os.path.exists(tmpdata):
            f = open(tmpdata, "rb")
            self.data = pickle.load(f)
        else:
            self.data = self.load(dictfile)
            f = open(tmpdata, "wb")
            pickle.dump(self.data, f)

        f.close()

    def show(self):
        for k in self.data:
            print("en: ", self.data[k][0], ", cn: ", self.data[k][1])

    def load(self, dictfile):
        f = open(dictfile)
        flag = True
        data = {'word': []}

        for w in f:
            w = w.rstrip("\n")
            if flag:
                en = w
            else:
                word = [en, w]
                data[md5(w)] = word
                data[md5(en)] = word

            data['word'].append(w)
            flag = not flag

        f.close()

        return data

    def run(self):
        while True:
            key = input("请输入查询关键词: ")
            if key in ['q', 'quit']:
                break
            m = md5(key)
            if m in self.data:
                print("\t英文: ", self.data[m][0])
                print("\t中文: ", self.data[m][1])
            else:
                for w in self.data['word']:
                    if key in w:
                        m = md5(w)
                        print("\t英文: ", self.data[m][0])
                        print("\t中文: ", self.data[m][1])


if __name__ == "__main__":
    c = Dict("./ciku.dict")
    #  c.show()
    c.run()
