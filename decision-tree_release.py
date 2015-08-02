# -*- coding: utf-8 -*-
# find-s算法

import sys

def printInfo():
    print  '#---------------------------------------------------------------#'
    print u'|                                                               |'
    print u'|《机器学习》（机械工业出版社）第2章 find-s算法实现（第二版）， |'
    print u'| 修改了假设的内部数据结构。                                    |'
    print u'| 包括一个名为fsd1.txt的数据文件。                              |'
    print u'|                                                               |'
    print u'|                                          by minvacai@sina.com |'
    print u'|                                               2014/2/24       |'
    print u'|                                                               |'
    print  '#---------------------------------------------------------------#'
    print ''
    return

# 概念学习(Concept Learning)数据结构
# 应用于find-s、变型空间及候选消除(candidate-elimination)算法等
# 假设数据结构(举例): h=<Sunny, Warm, ?, Strong, ?, ?>
# 样例数据结构(举例): d=<Sunny, Warm, Normal, Strong, Warm, Same>
class ConceptLearning:
    def __init__(self):
        self.new_H()
        return

    def destroyData(self):
        del self.h
        del self.x
        return

    #样例
    def new_X(self):
        self.x=[{},False]
        return True

    #假设
    def new_H(self):
        self.h = {}
        return True
    

    #假设中各单元值结构
    def new_HValue(self):
        r = ''
        return r

    # 样例及假设的一般性比较
    # d比h更一般：记为d>h，返回1
    # d<h: 返回2
    # 出错： 返回-255
    # replace: 更新当前假设标志
    def more_general(self,d,replace):
        ERROR=-255
        d1MGTd2=1
        d2MGTd1=2
        rValue = d2MGTd1

        for key in d:
            if key in self.h:
                if d[key] != self.h[key] and self.h[key]!='?':
                    rValue = d1MGTd2
                    if replace == True:#更新当前假设标志为真
                        if self.h[key]=='':
                            self.h[key] = d[key]
                        else:
                            self.h[key]='?'
                    else:
                        return rValue
            else:
                return ERROR
            #print ''
        return rValue

# 从文件中读取数据
# 文件格式如下：
# 第一行：width=Number 数据宽度
def getDataFromTxt(filenm):
    index=0
    textlen=0
    d = []
    data = []
    width = 0

    try:
        f = file(filenm)
    except:
        print u'文件 %s 不存在！'%(filenm)
        sys.exit()
        
    for line in f.readlines():
        crntline = line #.readline()
        if len(crntline)>0:
            tStr1 = crntline.decode('utf8')
            if tStr1[0:6]==u'width=':   # width of data
                width = int(tStr1[6:len(tStr1)])
            else:
                if tStr1[0:6]==u'title=':#
                    titleRaw = tStr1[6:len(tStr1)]
                    title = titleRaw.split(u',')
                else:   #数据行
                    titleRaw = tStr1
                    tmpData = titleRaw.split(u',')
                    d.append(tmpData)
            index=index+1

    for i in range(0,len(d)):
        data.append([])
        data[i].append({})
        dlen = len(d[i])-1
        for j in range(0,dlen):
            data[i][0][title[j]]=d[i][j]
        data[i].append( int(d[i][dlen]) )
    f.close()
    return (data,title)

printInfo()

try:
    datafile = sys.argv[1] #os.system(sys.argv[1])
except:
    print 'Usage: %s <datafile>'%(sys.argv[0])
    #exit(0)
    sys.exit()

(data,Title) = getDataFromTxt(datafile)

cl = ConceptLearning()
for t in Title:
    cl.h[t] = cl.new_HValue()

for i in range(0,len(data)):
    if data[i][1]==1:
        n = cl.more_general(data[i][0],True)

print u'输入的数据：'
print  '--------------------------------------------------------------'

for i in data[0][0]:
    print i[0:4],'\t',
print 'True/False'

for i in range(0,len(data)):
    for j in data[i][0]:
        print data[i][0][j],'\t',
    print data[i][1]
    
print  '--------------------------------------------------------------'
print u'输出：'
for i in cl.h:
    print '<',i,':',cl.h[i],'>',
print ''
