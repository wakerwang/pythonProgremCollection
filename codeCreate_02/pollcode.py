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
                scode4(choice)
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
                sys.exit(1)
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


def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()
    for j in range(int(scount)):
        strpro = typestr[0].upper()
        strtype = typestr[1].upper()
        strclass = typestr[2].upper()
        randfir = random.sample(number, 3)
        randsec = sorted(randfir)
        letterone = ""
        for i in range(9):
            letterone = letterone + random.choice(number)
        sim = str(letterone[0:int(randsec[0])]) + strpro + str(letterone[int(randsec[0]):int(randsec[1])]) \
              + strtype + str(letterone[int(randsec[1]):int(randsec[2])]) \
              + strclass + str(letterone[int(randsec[2]):9]) + "\n"
        randstr.append(sim)
    wfile(randstr, typestr + "scode" + str(schoice) + ".txt", ismessage, "生成含数据分析功能的防伪码共计：", "codepath")


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
        ordstart = inputbox("\033[1;32m    请输入系列产品起始号（3位）：\033[0m", 1, 0)  # 起始号  如：123
    ordcount = inputbox("\033[1;32m    请输入系列产品数量：\033[0m", 1, 0)  # 系列产品数量
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
    # 每个系列产品的防伪码数量
    incount = inputbox("\033[1;32m    请输入每个系列产品的防伪码数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m    请输入每个系列产品的防伪码数量：\033[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone = ""  # 保存生成的单条防伪码，不带"-",循环时清空
        for i in range(25):
            strone = strone + random.choice(letter)
        # 将生成的防伪码添加横线
        strtwo = strone[:5] + "-" + strone[5:10] + "-" + strone[10:15] + "-" + strone[15:20] + "-" + strone[20:] + "\n"
        randstr.append(strtwo)
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成25位混合防伪序列码共计：", "codepath")


def scode4(schoice):
    intype = inputbox("\033[1;32m    请输入数据分析编号（3位字母）：\033[0m", 2, 3)
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox("\033[1;32m    请输入数据分析编号（3位字母）：\033[0m", 2, 3)
    incount = inputbox("\033[1;32m    请输入要生成的带数据分析功能的防伪码数量：\033[0m", 1, 0)
    while int(incount) <= 0:
        incount = inputbox("\033[1;32m    请输入要生成的带数据分析功能的防伪码数量：\033[0m", 1, 0)
    ffcode(incount, intype, "", schoice)


def scode5(schoice):
    default_dir = r"codeauto.mri"
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file", "*.mri")], title=u"请选择智能批处理文件",
                                                   initialdir=(os.path.expanduser(default_dir)))

    codelist = openfile(file_path)
    codelist = codelist.split("\n")
    for item in codelist:
        items = item.split(",")
        codea = items[0]
        codeb = items[1]
        ffcode(codeb, codea, "no", schoice)


def scode6(schoice):
    pass


def scode7(schoice):
    mainid = inputbox("\033[1;32m    请输入EN13的国家代码（3位）：\033[0m", 1, 0)
    while int(mainid) < 1 or len(mainid) != 3:
        mainid = inputbox("\033[1;32m    请输入EN13的国家代码（3位）：\033[0m", 1, 0)
    compid = inputbox("\033[1;32m    请输入EN13的企业代码（4位）：\033[0m", 1, 0)
    while int(compid) < 1 or len(compid) != 4:
        compid = inputbox("\033[1;32m    请输入EN13的企业代码（4位）：\033[0m", 1, 0)
    incount = inputbox("\033[1;32m    请输入您要生成的条形码数量：\33[0m", 1, 0)
    mkdir("barcode")
    for j in range(int(incount)):
        strone = ""
        for i in range(5):
            strone = strone + str(random.choice(number))
        barcode = mainid + compid + strone
        evensum = sum(range(1, 12, 2))
        oddsum = sum(range(0, 12, 2))
        checkbit = int((10 - (evensum * 3 + oddsum) % 10) % 10)
        barcode = barcode + str(checkbit)
        encoder = EAN13Encoder(barcode)
        encoder.save("barcode\\" + barcode + ".png")


def scode8(schoice):
    incount = inputbox("\033[1;32m    请输入您要生成的12位二维码数量：\33[0m", 1, 0)
    while int(incount)==0:
        incount = inputbox("\033[1;32m    请输入您要生成的12位二维码数量：\33[0m", 1, 0)
    mkdir("qrcode")
    for j in range(int(incount)):
        strone = ""
        for i in range(12):
            strone = strone + str(random.choice(number))
        encoder = qrcode.make(strone)
        encoder.save("qrcode\\" + strone + ".png")


def scode9(schoice):
    pass


if __name__ == '__main__':
    mainmenu()
