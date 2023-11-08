#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pk.py
@Describe :  
@Contact :   mrbingzhao@qq.com
@License :   (C)Copyright 2023/11/8, Liugroup-NLPR-CASIA

@Modify Time        @Author       @Version    @Desciption
----------------   -----------   ---------    -----------
2023/11/8 上午9:17   liubingzhao      1.0           ml
'''
import os
import shutil

# 要清理的目录列表
directories_to_clean = ['dist', 'build', 'bzutil.egg-info']

def clean_directories(directories):
    for directory in directories:
        if os.path.exists(directory):
            if os.path.isfile(directory):
                os.remove(directory)
            elif os.path.isdir(directory):
                shutil.rmtree(directory)
            print(f"清理目录: {directory}")

if __name__ == "__main__":
    clean_directories(directories_to_clean)
    # 运行命令以生成新的包
    os.system('python setup.py sdist bdist_wheel')
    clean_directories(['build', 'bzutil.egg-info'])