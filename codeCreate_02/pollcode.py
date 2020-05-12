#!/bin/env python
# coding:utf-8
import os, time, string, random, tkinter, qrcode
from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from string import digits

root = tkinter.Tk()

number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
randstr = []
fourth = []
fifth = []

randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""


def mainmenu():
    i = 0
    print("""\033[1;35m
    ***********************************************************
                         企业编码生成系统
    ***********************************************************
        1.生成6位数字防伪编码(213563型)
        2.生成9位系列产品数字防伪编码(879-335439型)
        3.生成25位混合产品序列号(B2R12-N7TE8-9ET2-FE350-DW2K4型)
        4.生成含数据分析功能的防伪编码(5A61MO583D2)
        5·智能批量生成带数据分析功能的防伪码
        6.后续补加生成防伪码(5A61M0583D2)
        7.EAN-13条形码批量生成
        8.二维码批量输出
        9.企业粉丝防伪码抽奖
        0.退出系统
    ============================================================
    说明：通过数字键选择菜单
    ============================================================
    \033[0m""")
    while i < 9:
        choice = input("\033[1;32m    请输出选项菜单:\33[0m")
        if len(choice) != 0:
            choice = input_validation(choice)
            if choice == 1:
                scode1(str(choice))
            if choice == 2:
                scode2(choice)
            if choice == 3:
                scode3(choice)
            if choice == 4:
                scode4("", choice)
            if choice == 5:
                scode5(choice)
            if choice == 6:
                scode6(choice)
            if choice == 7:
                scode7(choice)
            if choice == 8:
                scode8(choice)
            if choice == 9:
                scode9(choice)
            if choice == 0:
                i = 0
                print("正在退出系统！！")
        else:
            print("\033[1;31;40m    输入非法，请重新输入！！\033[0m")
            time.sleep(2)


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print("\033[1;31;40m    输入非法，请重新输入！！\033[0m")
            return 0
        else:
            return int(insel)
    else:
        print("\033[1;31;40m    输入非法，请重新输入！！\033[0m")
        return 0


def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)


def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist


def inputbox(showstr, showorder, length):
    instr = input(showstr)  # showstr为输入提示文字
    if len(instr) != 0:
        # 分成三种验证方式，1 数字  2 字母  3 数字且有位数要求
        if showorder == 1:
            if str.isdigit(instr):  # 验证是否为数字
                if instr == 0:
                    print("\033[1;31;40m 输入为零，请重新输入!! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入!! \033[0m")
                return "0"
        if showorder == 2:
            if str.isalpha(instr):  # 判断是否为字母
                if len(instr) != length:
                    print("\033[1;31;40m必须输入" + str(length) + "个字母，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print("\033[1;31;40m必须输入" + str(length) + "个数字，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
    else:
        print("\033[1;31;40m输入为空，请重新输入！！\033[0m")
        return "0"


def wfile(sstr, sfile, typeis, smsg, datapath):
    mkdir(datapath)
    datafile = datapath + '\\' + sfile
    file = open(datafile, 'w')
    wrlist = sstr
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']', "")
        wdata = wdata.replace(''''',").replace(''''', '')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    # print("\033[1;31m" + pdata + "\033[0m")
    if typeis != "no":
        tkinter.messagebox.showinfo("提示", smsg + str(len(randstr)) + "\n防伪码文件存放位置" + datafile)
        root.withdraw()


def scode1(schoice):
    incount = inputbox("\033[1;32m    请输入您要生成的防伪码数量：\33[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m    请输入您要生成的防伪码数量：\33[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ""
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + "\n"
        randstr.append(randfir)
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成6位防伪码共计:", "codepath")


def scode2(schoice):
    ordstart = inputbox("\033[1;32m    请输入系列产品起始号（3位）：\033[0m", 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m    请输入系列产品起始号（3位）：\033[0m", 1, 0)
    ordcount = inputbox("\033[1;32m    请输入系列产品数量：\033[0m", 1, 0)
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox("\033[1;32m    请输入系列产品数量：\033[0m", 1, 0)
    incount = inputbox("\033[1;32m    请输入每个系列产品的防伪码数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m    请输入每个系列产品的防伪码数量：\033[0m", 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ""
            for i in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m) + randfir + "\n")
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成9位系列产品防伪码共计：", "codepath")


def scode3(schoice):
    pass


def scode4(schoice):
    pass


def scode5(schoice):
    pass


def scode6(schoice):
    pass


def scode7(schoice):
    pass


def scode8(schoice):
    pass


def scode9(schoice):
    pass


if __name__ == '__main__':
    mainmenu()
