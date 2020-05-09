#!/bin/env python
import os
def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)

def openfile(filename):
    f=open(filename)
    fllist=f.read()
    f.close()
    return fllist

def inputbox(showstr,showorder,length):
    instr=input(showstr) #showstr为输入提示文字
    if len(instr) != 0:
        #分成三种验证方式，1 数字  2 字母  3 数字且有位数要求
        if showorder==1:
            if str.isdigit(instr): #验证是否为数字
                if instr==0:
                    print("\033[1;31;40m 输入为零，请重新输入!! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入!! \033[0m")
                return "0"
        if showorder==2:
            if str.isalpha(instr):#判断是否为字母
                if len(instr) !=length:
                    print("\033[1;31;40m必须输入"+str(length)+"个字母，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder==3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print("\033[1;31;40m必须输入"+str(length)+"个数字，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
    else:
        print("\033[1;31;40m输入为空，请重新输入！！\033[0m")
        return "0"

def wfile():
    pass


