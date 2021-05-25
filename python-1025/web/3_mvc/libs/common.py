#!/usr/bin/env python3


import os


def imp(module, method=None, package=None):
    """
    导入包/模块里的对象
    """
    if package is None:
        m = __import__("%s" % (module))
    else:
        m = __import__("%s.%s" % (package, module))
        m = getattr(m, module)

    if method is None:
        return m

    return getattr(m, method)

def upload_save(files, savepath, cover=False, chunk_size=1024):
    """
    文件上传保存函数
    """
    def buffer():
        while True:
            chunk = files.file.read(chunk_size)
            if not chunk:
                break
            yield chunk

    if not cover and os.path.exists(savepath):
        return 0

    filesize = 0
    with open(savepath, "wb", chunk_size) as ofile:
        for chunk in buffer():
            filesize += len(chunk)
            ofile.write(chunk)

    return filesize

