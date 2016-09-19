# -*- coding:utf-8 -*-
import sys,os
import operator,re,math

def easyCalcs(t,x,y): 
    calculation  = {'+':lambda:operator.add(x,y), 
                    '*':lambda:operator.mul(x,y),
                    '-':lambda:operator.sub(x,y), 
                    '/':lambda:operator.div(x,y), 
                    '%':lambda:operator.mod(x,y) 
                }
    return calculation[t]()


def p(n,k):
    return reduce(operator.mul, range(n - k + 1, n+1))

def f(n):
    return p(n,n)

#也可以使用C(n,r)=C(n-1,r)+C(n-1,r-1), 比较要内存，可以动规
def c(n,k):
    return p(n,k) /reduce(operator.mul, range(1, k +1))

def pow(n):
    return math.pow(int(n[0]),int(n[1]))

def isExit(inputed):
    return inputed.strip()=='q'

def initInputed(inputed):
    num=[]
    ope=[]
    preSplit=0
    inputed=inputed.lower()
    for i in range(0,len(inputed)):
        c=inputed[i]
        if c in ['+','-','*','/','%']:
            ope.append(c)
            num.append(inputed[preSplit:i].strip())
            preSplit=i+1
    num.append(inputed[preSplit:])
    return(num,ope)

def changeToInt(num):
    for i in range(0,len(num)):
        each=num[i]
        if not each.isdigit():
            each=cal(each)
        num[i]=int(each)

def cal(num):
    if('^' in num):
        return pow(num.split('^'))
    if('!' in num):
        return f(int(num[:-1]))

    cmd = num[:1]
    l = re.split("[, ]",num[1:].strip())
    while '' in l:
        l.remove('')

    if cmd=="f":
        return p(int(l[0]),int(l[1]) if len(l)>1 else int(l[0]))

    if len(l)==1:   # 数字<10的时候可以不打空格
        l=list(l[0])# 将数字分为2位
    if cmd=="p" or cmd=="a":
        return p(int(l[0]),int(l[1]))
    if cmd=="c":
        return c(int(l[0]),int(l[1]))
        
    return -9999999

def getAns(num,ope):
    for oType in ope:
        t=easyCalcs(oType, num[0], num[1])
        num=num[2:]
        num.insert(0, t)
    return num[0]

def intWithCommas(x):
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

def do():
    flag=True
    
    print u"\nc=组合 p/a=排列 f/!=阶乘 ^=次方 q=退出 以及加减乘除和%\n没有负数，也没有实现括号\n"

    while flag:
        inputed = raw_input(">>>")
        if isExit(inputed):
            exit()
        (num,ope)=initInputed(inputed)
        changeToInt(num)
        print intWithCommas(getAns(num,ope))
        

if __name__ == "__main__":  
  do()

