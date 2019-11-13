# --coding:utf-8--
'''
    筛选出特定后缀的文件，并给这些文件设置执行属性

    筛选特定后缀可以通过，str的startwith（），ends with（）方法来取得

    设置文件属性，需要导入OS，Stat库


>>> import os
>>> print os.stat("/root/python/zip.py")
(33188, 2033080, 26626L, 1, 0, 0, 864, 1297653596, 1275528102, 1292892895)
>>> print os.stat("/root/python/zip.py").st_mode   #权限模式
33188
>>> print os.stat("/root/python/zip.py").st_ino   #inode number
2033080
>>> print os.stat("/root/python/zip.py").st_dev    #device
26626
>>> print os.stat("/root/python/zip.py").st_nlink  #number of hard links
1
>>> print os.stat("/root/python/zip.py").st_uid    #所有用户的user id
0
>>> print os.stat("/root/python/zip.py").st_gid    #所有用户的group id
0
>>> print os.stat("/root/python/zip.py").st_size  #文件的大小，以位为单位
864
>>> print os.stat("/root/python/zip.py").st_atime  #文件最后访问时间
1297653596
>>> print os.stat("/root/python/zip.py").st_mtime  #文件最后修改时间
1275528102
>>> print os.stat("/root/python/zip.py").st_ctime  #文件创建时间
1292892895


--------------------------------------

#!/usr/bin/env python
#-*- encoding:UTF-8 -*-

import os,time,stat

fileStats = os.stat ( 'test.txt' )                         #获取文件/目录的状态
fileInfo = {
'Size':fileStats [ stat.ST_SIZE ],                         #获取文件大小
'LastModified':time.ctime( fileStats [ stat.ST_MTIME ] ),  #获取文件最后修改时间
'LastAccessed':time.ctime( fileStats [ stat.ST_ATIME ] ),  #获取文件最后访问时间
'CreationTime':time.ctime( fileStats [ stat.ST_CTIME ] ),  #获取文件创建时间
'Mode':fileStats [ stat.ST_MODE ]                          #获取文件的模式
}
#print fileInfo

for field in fileInfo:                                     #显示对象内容
  print '%s:%s' % (field,fileInfo[field])

for infoField,infoValue in fileInfo:
  print '%s:%s' % (infoField,infoValue)
if stat.S_ISDIR ( fileStats [ stat.ST_MODE ] ):           #判断是否路径
  print 'Directory. '
else:
  print 'Non-directory.'

if stat.S_ISREG( fileStats [ stat.ST_MODE ] ):           #判断是否一般文件
   print 'Regular file.'
elif stat.S_ISLNK ( fileStats [ stat.ST_MODE ] ):         #判断是否链接文件
   print 'Shortcut.'
elif stat.S_ISSOCK ( fileStats [ stat.ST_MODE ] ):        #判断是否套接字文件
   print 'Socket.'
elif stat.S_ISFIFO ( fileStats [ stat.ST_MODE ] ):        #判断是否命名管道
   print 'Named pipe.'
elif stat.S_ISBLK ( fileStats [ stat.ST_MODE ] ):         #判断是否块设备
   print 'Block special device.'
elif stat.S_ISCHR ( fileStats [ stat.ST_MODE ] ):         #判断是否字符设置
   print 'Character special device.'

--------------------------------------------
'''

import os, stat

# 获取当前目录文件清单
files = os.listdir('.')
print(files)

# 获取单个文件的属性信息
s1 = os.stat('his').st_file_attributes
print(s1)

# 设置文件属性值
# print(stat.FILE_ATTRIBUTE_READONLY)
print(stat.FILE_ATTRIBUTE_HIDDEN)

# print(os.stat('his').st_file_attributes | stat.FILE_ATTRIBUTE_HIDDEN)
# mod = os.stat('his').st_file_attributes | stat.FILE_ATTRIBUTE_HIDDEN
# print(mod)
os.chmod('his', s1 | stat.FILE_ATTRIBUTE_HIDDEN)
s2 = os.stat('his').st_file_attributes
print(oct(s2))
