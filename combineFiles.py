# -*- coding: utf-8 -*-
# python-3.7.4-32bit, windows 10

import os
import os.path

folders = ['chapter1','chapter2','chapter3','chapter4','chapter5','chapter6','chapter7','chapter8','chapter9','chapter10','appendix_A','appendix_B','appendix_C','appendix_D']
prefix =  #填写你的文件位置，比如 r'C:\Cpp_Concurrency_In_Action-master\content'
newdir = prefix + '\\' + 'cppConcurrencyAllinone'
if not os.path.exists(newdir):
    os.mkdir(newdir)

f = open(newdir+'\\'+'cppConcurrencyAllinone.md','w',encoding='utf8')
for folder in folders:
    path = prefix + '\\' + folder
    filelist = os.listdir(path)
    filelist.sort()
    for doc in filelist:
        print(doc)
        f2 = open(path+'\\'+doc, 'r', encoding='utf8')
        f.write(f2.read())
        f.write('\n')
        f2.close()
f.close()
