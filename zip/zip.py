# -*- coding: utf-8 -*-

import os
import zipfile


def create_zip(path):
    '''创建一个压缩文件'''
    # 创建一个zip文件对象
    zip_file = zipfile.ZipFile(os.path.basename(path) + '.zip', 'w')
    # 将文件写入zip文件中，即将文件压缩
    print('开始压缩文件......')
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            print('正在压缩文件:' + os.path.join(root, name))
            zip_file.write(os.path.join(root, name))
        for name in files:
            print('正在压缩文件:' + os.path.join(root, name))
            zip_file.write(os.path.join(root, name))
    # 关闭zip文件对象
    zip_file.close()


def uncompress_zip(path):
    '''解压文件'''
    print('正在解压文件中......')
    zfile = zipfile.ZipFile(path, 'r')
    zfile.extractall()


if __name__ == '__main__':
    path_info = 'test.zip'
    if os.path.isdir(path_info):
        # 打包
        create_zip(path_info)
        print('压缩完成')
    elif os.path.isfile(path_info):
        pass
    else:
        print('文件类型错误，请重度！')