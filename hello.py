#!/usr/bin/env python3 #让这个hello.py可以直接在Mac上运行
# -*- coding: utf-8 -*- #表示.py文件本身使用标准UTF-8编码

' a test module ' #是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'Joshua Ren' #使用__author__变量把作者写进去
                          #以上就是Python模块的标准文件模板
import sys #导入sys模块  导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能

def test():
    args = sys.argv #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Toomany arguments!')

if __name__ == '__main__':  #当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
    test()                  #而如果在其他地方导入该hello模块时，if判断将失败，因此，
                            #这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
