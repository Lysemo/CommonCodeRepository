'''
func:batch rename file or fold
author:Lele Wu
method:Place the file in the directory where the file or folder is located, then double tap
hint:avoid same name already exist | file(have suffix) and file(no suffix) not same time exist
'''
import os

def batchRename(rootPath,include=False):
    # include为True时，包含原文件名；为False时，不包含
    prefix = '' #前缀
    suffix = '' #后缀
    fill = 0    #填充位数
    i = 1    #起始数
    mode = 1    #模式，可选1，2，3，1为有后缀文件；2为无后缀文件；3为文件夹
    for sub in os.listdir(rootPath):
        if(sub=='batchRename.py'):
            continue
        if(mode==1):
            if os.path.isfile(os.path.join(rootPath, sub)):  #file(have suffix)
                self_suffix = sub.split('.')[-1]
                self_sub = sub.split('.')[:-1]
                if(include):
                    newName = prefix + self_sub[0] + suffix + '.' + self_suffix # 包含原文件名 
                else:
                    newName = prefix + str(i).zfill(fill) + suffix + '.' + self_suffix  # 重新数字索引
                os.rename(sub, newName)
                i = i + 1
        if(mode==2):
            if os.path.isfile(os.path.join(rootPath, sub)):  #file(no suffix)
                newName = prefix + sub + suffix
                newName = prefix + str(i).zfill(fill) + suffix
                os.rename(sub, newName)
                i = i + 1
        if (mode == 3):
            if os.path.isdir(os.path.join(rootPath,sub)):   #fold
                newName = prefix + sub + suffix
                newName = prefix + str(i).zfill(fill) + suffix
                os.rename(sub,newName)
                i = i+1
    print('finished!!!')

if __name__ == '__main__':
    root = './'
    batchRename(root)
