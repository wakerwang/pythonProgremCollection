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
    instr=input(showstr) #showstrΪ������ʾ����
    if len(instr) != 0:
        #�ֳ�������֤��ʽ��1 ����  2 ��ĸ  3 ��������λ��Ҫ��
        if showorder==1:
            if str.isdigit(instr): #��֤�Ƿ�Ϊ����
                if instr==0:
                    print("\033[1;31;40m ����Ϊ�㣬����������!! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m ����Ƿ�������������!! \033[0m")
                return "0"
        if showorder==2:
            if str.isalpha(instr):#�ж��Ƿ�Ϊ��ĸ
                if len(instr) !=length:
                    print("\033[1;31;40m��������"+str(length)+"����ĸ�����������룡��\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m����Ƿ������������룡��\033[0m")
                return "0"
        if showorder==3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print("\033[1;31;40m��������"+str(length)+"�����֣����������룡��\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m����Ƿ������������룡��\033[0m")
                return "0"
    else:
        print("\033[1;31;40m����Ϊ�գ����������룡��\033[0m")
        return "0"

def wfile():
    pass


