#!/usr/bin/env python3


import pickle


class PacketError(Exception):
    pass

class Packet:
    ALL  = 0
    GET  = 1
    POST = 2
    QUIT = 3
    ERROR = 4
    DATA = 5
    ACK = 6
    CONN = 7
    CONN_ACK = 8
    SIZE = 1024

    def __init__(self, sd, magic="Kyo", **kargs):
        self.sd = sd
        self.magic = magic
        self.__dict__.update(kargs)

    def checkSum(self, data):
        def genSum(data):
            data = pickle.dumps(data)
            #  hashlib.md5/hashlib.sha1
            s = 0
            for i in data:
                s += i
            return s

        if 'sum' in data:
            sumNum = data.pop('sum')
            return bool(sumNum == genSum(data))

        return genSum(data)

    def send(self, data, addr, types=None):
        types = Packet.GET if types is None else types
        sdata = {'magic': self.magic, 'type': types}
        if type(data) == dict:
            sdata.update(data)
        else:
            sdata['data'] = data

        sdata['sum'] = self.checkSum(sdata)

        sdata = pickle.dumps(sdata)
        if len(sdata) > Packet.SIZE:
            return None

        ret = self.sd.sendto(sdata, addr)
        print("send = ", ret)
        return ret

    def recv(self, types=None, timeout=None):
        types = Packet.ALL if types is None else types
        self.sd.settimeout(timeout)
        data, addr = self.sd.recvfrom(Packet.SIZE)
        data = pickle.loads(data)
        #  print("recv: ", data)

        if ('magic' not in data or 'type' not in data
                or data['magic'] != self.magic):
            raise PacketError("接受到非法协议包!")

        if not self.checkSum(data):
            raise PacketError("接受数据包检验和验证失败!")

        if types != Packet.ALL and data['type'] != types:
            raise PacketError("接受数据包不是指定类型!")

        self.sd.settimeout(None)

        return data, addr

