# -*- mode: python ; coding: utf-8 -*-
import csv
import json
import numpy
from PIL import Image, ImageTk
import requests
import ttkbootstrap as 界面
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from 物价局计算 import 材料定价计算


def 更新文件():
    global 游戏物品数据, 精英材料编号列表, 精英材料名列表
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
    游戏基建数据源 = 'https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/building_data.json'
    游戏物品数据源 = 'https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/item_table.json'
    游戏关卡数据源 = 'https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/stage_table.json'
    企鹅物流自动数据源 = 'https://penguin-stats.io/PenguinStats/api/v2/result/matrix?server=CN&is_personal=false&show_closed_zones=true&category=automated'
    游戏材料素材文件源 = 'https://raw.githubusercontent.com/yuanyan3060/ArknightsGameResource/main/item/'
    try:
        with open('游戏基建数据.json', 'w', encoding='utf-8') as 保存:   json.dump(requests.get(游戏基建数据源, headers=headers).json(), 保存)
        with open('游戏物品数据.json', 'w', encoding='utf-8') as 保存:   json.dump(requests.get(游戏物品数据源, headers=headers).json(), 保存)
        with open('游戏关卡数据.json', 'w', encoding='utf-8') as 保存:   json.dump(requests.get(游戏关卡数据源, headers=headers).json(), 保存)
        with open('企鹅物流自动掉落数据.json', 'w', encoding='utf-8') as 保存:   json.dump(requests.get(企鹅物流自动数据源, headers=headers).json(), 保存)
        游戏物品数据 = json.load(open('游戏物品数据.json'))
        精英材料编号列表 = [[], [], [], [], []]
        精英材料名列表 = [[], [], [], [], []]
        for 物品 in 游戏物品数据['items']:
            if 100000 < 游戏物品数据['items'][物品]['sortId'] < 200000:
                if 游戏物品数据['items'][物品]['rarity'] == 'TIER_1':
                    精英材料编号列表[0].append(游戏物品数据['items'][物品]['itemId'])
                    精英材料名列表[0].append(游戏物品数据['items'][物品]['name'])
                elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_2':
                    精英材料编号列表[1].append(游戏物品数据['items'][物品]['itemId'])
                    精英材料名列表[1].append(游戏物品数据['items'][物品]['name'])
                elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_3':
                    精英材料编号列表[2].append(游戏物品数据['items'][物品]['itemId'])
                    精英材料名列表[2].append(游戏物品数据['items'][物品]['name'])
                elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_4':
                    精英材料编号列表[3].append(游戏物品数据['items'][物品]['itemId'])
                    精英材料名列表[3].append(游戏物品数据['items'][物品]['name'])
                elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_5':
                    精英材料编号列表[4].append(游戏物品数据['items'][物品]['itemId'])
                    精英材料名列表[4].append(游戏物品数据['items'][物品]['name'])
        for 序号, 材料 in enumerate(精英材料编号列表[0] + 精英材料编号列表[1] + 精英材料编号列表[2] + 精英材料编号列表[3] + 精英材料编号列表[4]):
            response = requests.get(游戏材料素材文件源 + 游戏物品数据['items'][材料]['iconId'] + '.png')
            if response.status_code == 200:
                with open(f"图片/{游戏物品数据['items'][材料]['iconId']}.png", 'wb') as file: file.write(response.content)
        提示.config(text="游戏数据与文件已更新")
    except: 提示.config(text="该功能需要科学上网，请检查网络连接")


def 读取游戏文件(游戏物品数据):
    global 精英材料编号列表, 精英材料名列表, 精英材料图片列表, 其他物品信息列表
    精英材料编号列表 = [[], [], [], [], []]
    精英材料名列表 = [[], [], [], [], []]
    精英材料图片列表 = [[], [], [], [], []]
    其他物品信息列表 = [[],
                    ['龙门币', '基础作战记录', '初级作战记录', '中级作战记录', '高级作战记录', '赤金', '合成玉', '寻访凭证', '中坚寻访凭证',
                     '芯片助剂', '技巧概要·卷1', '技巧概要·卷2', '技巧概要·卷3', '碳', '碳素',
                     '招聘许可', '加急许可', '模组数据块', '家具零件'],
                    [3, 1, 2, 3, 4, 3, 4, 4, 4, 3, 1, 2, 3, 1, 2,3, 3, 4, 2], numpy.zeros(19)]
    # 从解包文件中获取材料种类
    for 物品 in 游戏物品数据['items']:
        if 100000 < 游戏物品数据['items'][物品]['sortId'] < 200000:
            if 游戏物品数据['items'][物品]['rarity'] == 'TIER_1':
                精英材料编号列表[0].append(游戏物品数据['items'][物品]['itemId'])
                精英材料名列表[0].append(游戏物品数据['items'][物品]['name'])
                精英材料图片列表[0].append(ImageTk.PhotoImage(Image.open(f'图片/{游戏物品数据["items"][物品]["iconId"]}.png').resize((40, 40))))
            elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_2':
                精英材料编号列表[1].append(游戏物品数据['items'][物品]['itemId'])
                精英材料名列表[1].append(游戏物品数据['items'][物品]['name'])
                精英材料图片列表[1].append(ImageTk.PhotoImage(Image.open(f'图片/{游戏物品数据["items"][物品]["iconId"]}.png').resize((40, 40))))
            elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_3':
                精英材料编号列表[2].append(游戏物品数据['items'][物品]['itemId'])
                精英材料名列表[2].append(游戏物品数据['items'][物品]['name'])
                精英材料图片列表[2].append(ImageTk.PhotoImage(Image.open(f'图片/{游戏物品数据["items"][物品]["iconId"]}.png').resize((40, 40))))
            elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_4':
                精英材料编号列表[3].append(游戏物品数据['items'][物品]['itemId'])
                精英材料名列表[3].append(游戏物品数据['items'][物品]['name'])
                精英材料图片列表[3].append(ImageTk.PhotoImage(Image.open(f'图片/{游戏物品数据["items"][物品]["iconId"]}.png').resize((40, 40))))
            elif 游戏物品数据['items'][物品]['rarity'] == 'TIER_5':
                精英材料编号列表[4].append(游戏物品数据['items'][物品]['itemId'])
                精英材料名列表[4].append(游戏物品数据['items'][物品]['name'])
                精英材料图片列表[4].append(ImageTk.PhotoImage(Image.open(f'图片/{游戏物品数据["items"][物品]["iconId"]}.png').resize((40, 40))))
    for 物品 in 其他物品信息列表[1]:
        其他物品信息列表[0].append(ImageTk.PhotoImage(Image.open(f'图片/{物品}.png').resize((40, 40))))


def 计算工序():
    龙门币价值输入字符串 = 价值输入[0].get()
    for 字符 in 龙门币价值输入字符串:
        if 字符 not in '0123456789.+-*/()（）[]【】':
            价值输入[0].delete(0, 界面.END)
            价值输入[0].insert(0, '请输入合适的数学计算式！')
            return
    龙门币价值 = eval(龙门币价值输入字符串.replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']'))
    经验价值输入字符串 = 价值输入[1].get()
    for 字符 in 经验价值输入字符串:
        if 字符 not in '0123456789.+-*/()（）[]【】龙门币价值':
            价值输入[1].delete(0, 界面.END)
            价值输入[1].insert(0, '请输入合适的数学计算式！')
            return
    经验价值 = eval(经验价值输入字符串.replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']'))
    赤金价值输入字符串 = 价值输入[2].get()
    for 字符 in 赤金价值输入字符串:
        if 字符 not in '0123456789.+-*/()（）[]【】龙门币经验价值':
            价值输入[0].delete(0, 界面.END)
            价值输入[0].insert(0, '请输入合适的数学计算式！')
            return
    赤金价值 = eval(赤金价值输入字符串.replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']'))
    合成玉价值输入字符串 = 价值输入[3].get()
    for 字符 in 合成玉价值输入字符串:
        if 字符 not in '0123456789.+-*/()（）[]【】龙门币经验赤金价值':
            价值输入[0].delete(0, 界面.END)
            价值输入[0].insert(0, '请输入合适的数学计算式！')
            return
    合成玉价值 = eval(合成玉价值输入字符串.replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']'))
    价值输入字符串 = []
    价值 = []
    for 序号 in range(7):
        价值输入字符串.append(价值输入[序号+4].get())
        for 字符 in 价值输入字符串[序号]:
            if 字符 not in '0123456789.+-*/()（）[]【】龙门币经验赤金合成玉价值':
                价值输入[序号+4].delete(0, 界面.END)
                价值输入[序号+4].insert(0, '请输入合适的数学计算式！')
                return
        价值.append(eval(价值输入字符串[序号].replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']')))
    副产品产出概率字符串 = []
    副产品产出概率 = []
    for 等级 in range(4):
        副产品产出概率字符串.append(加工输入[等级].get())
        for 字符 in 副产品产出概率字符串[等级]:
            if 字符 not in '0123456789.+-*/()（）[]【】':
                加工输入[等级].delete(0, 界面.END)
                加工输入[等级].insert(0, '请输入合适的数学计算式！')
                return
        副产品产出概率.append(eval(副产品产出概率字符串[等级].replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']')) / 100)
    if 加工T3精英材料使用九色鹿获取因果.get():
        副产品产出概率[2] = 0.1
        加工输入[2].delete(0, 界面.END)
        加工输入[2].insert(0, '10')
    if 加工T2精英材料使用九色鹿获取因果.get():
        副产品产出概率[3] = 0.1
        加工输入[3].delete(0, 界面.END)
        加工输入[3].insert(0, '10')
    加工技巧概要副产品产出概率字符串 = 加工技巧概要输入.get()
    if 加工技巧概要使用九色鹿获取因果.get():
        加工技巧概要输入.delete(0, 界面.END)
        加工技巧概要输入.insert(0, '10')
        技巧概要副产品产出概率 = 0.1
    else:
        for 字符 in 加工技巧概要副产品产出概率字符串:
            if 字符 not in '0123456789.+-*/()（）[]【】':
                加工技巧概要输入.delete(0, 界面.END)
                加工技巧概要输入.insert(0, '请输入合适的数学计算式！')
                return
        技巧概要副产品产出概率 = eval(加工技巧概要副产品产出概率字符串.replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']')) / 100
    加工基建材料副产品产出概率字符串 = 加工基建材料输入.get()
    if 加工基建材料使用九色鹿获取因果.get():
        加工基建材料输入.delete(0, 界面.END)
        加工基建材料输入.insert(0, '10')
        基建材料副产品产出概率 = 0.1
    else:
        for 字符 in 加工基建材料副产品产出概率字符串:
            if 字符 not in '0123456789.+-*/()（）[]【】':
                加工基建材料输入.delete(0, 界面.END)
                加工基建材料输入.insert(0, '请输入合适的数学计算式！')
                return
        基建材料副产品产出概率 = eval(加工基建材料副产品产出概率字符串.replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']')) / 100

    读取游戏文件(json.load(open('游戏物品数据.json')))
    采购价格数据 = json.load(open('采购价格.json', encoding="utf-8"))
    for 序号, 材料名 in enumerate(精英材料名列表[0]+精英材料名列表[1]+其他物品信息列表[1]):
        if 材料名 in 采购价格数据["信用"].keys():
            for 字符 in 采购价格数据["信用"][材料名]:
                if 字符 not in '0123456789./':
                    提示.configure(text="请还原采购价格文件！")
                    return

    for 阶段 in range(3):
        for 序号, 材料名 in enumerate(精英材料名列表[2]+其他物品信息列表[1]):
            if 材料名 in 采购价格数据[f"资质凭证阶段{阶段+1}"].keys():
                for 字符 in 采购价格数据[f"资质凭证阶段{阶段+1}"][材料名]:
                    if 字符 not in '0123456789./':
                        提示.configure(text="请还原采购价格文件！")
                        return

    for 序号, 材料名 in enumerate(精英材料名列表[3] + 其他物品信息列表[1]):
        if 材料名 in 采购价格数据["高级凭证"].keys():
            for 字符 in 采购价格数据["高级凭证"][材料名]:
                if 字符 not in '0123456789./':
                    提示.configure(text="请还原采购价格文件！")
                    return

    for 序号, 材料名 in enumerate(精英材料名列表[0]+精英材料名列表[1]+精英材料名列表[2]+精英材料名列表[3]):
        if 材料名 in 采购价格数据["寻访参数模型"].keys():
            for 字符 in 采购价格数据["寻访参数模型"][材料名]:
                if 字符 not in '0123456789./':
                    提示.configure(text="请还原采购价格文件！")
                    return

    for 序号, 材料名 in enumerate(精英材料名列表[3]+其他物品信息列表[1]):
        if 材料名 in 采购价格数据["情报凭证"].keys():
            for 字符 in 采购价格数据["情报凭证"][材料名]:
                if 字符 not in '0123456789./':
                    提示.configure(text="请还原采购价格文件！")
                    return

    基备选集合 = 关卡范围.get()
    换算活动代币 = 活动代币.get()
    瑕光加工T5精英材料 = 瑕光[0].get
    瑕光加工T4精英材料 = 瑕光[1].get
    瑕光加工T3精英材料 = 瑕光[2].get
    瑕光加工T2精英材料 = 瑕光[3].get
    九色鹿加工T3精英材料 = 加工T3精英材料使用九色鹿获取因果.get()
    九色鹿加工T2精英材料 = 加工T2精英材料使用九色鹿获取因果.get()
    九色鹿加工技巧概要 = 加工技巧概要使用九色鹿获取因果.get()
    九色鹿加工基建材料 = 加工基建材料使用九色鹿获取因果.get()

    输入 = [
        龙门币价值, 经验价值, 赤金价值, 合成玉价值, 价值, 副产品产出概率, 技巧概要副产品产出概率, 基建材料副产品产出概率,
        基备选集合, 换算活动代币, 瑕光加工T5精英材料, 瑕光加工T4精英材料, 瑕光加工T3精英材料, 瑕光加工T2精英材料,
        九色鹿加工T3精英材料, 九色鹿加工T2精英材料, 九色鹿加工技巧概要, 九色鹿加工基建材料
    ]

    try:
        定价关卡列表, 精英材料价值排序表, 精英材料价值向量, 信用性价比表, 资质凭证性价比表, 高级凭证性价比表, 寻访参数模型性价比表, 情报凭证性价比表 = 材料定价计算(输入, 精英材料编号列表, 精英材料名列表, 精英材料图片列表, 其他物品信息列表)
    except:
        提示.configure(text='计算失败，请检查输入内容的合理性！', foreground='red')
        return

    # 界面输出
    for 等级 in range(5):
        for 子控件 in 精英材料定价域[等级].winfo_children():
            子控件.destroy()
    for 子控件 in 信用性价比域.winfo_children(): 子控件.destroy()
    for 子控件 in 资质凭证性价比域.winfo_children(): 子控件.destroy()
    for 子控件 in 高级凭证性价比域.winfo_children(): 子控件.destroy()
    for 子控件 in 寻访参数模型性价比域.winfo_children(): 子控件.destroy()
    for 子控件 in 情报凭证性价比域.winfo_children(): 子控件.destroy()
    for 子控件 in 定价关卡域.winfo_children(): 子控件.destroy()
    界面.Label(定价关卡域, image=理智图标).grid(row=0, column=0, padx=10, pady=3)
    界面.Label(定价关卡域, text="材料名称").grid(row=0, column=1, padx=10, pady=3)
    界面.Label(定价关卡域, text="理智定价").grid(row=0, column=2, padx=10, pady=3)
    界面.Label(定价关卡域, text="定价关卡").grid(row=0, column=3, padx=10, pady=3)

    游戏关卡数据 = json.load(open('游戏关卡数据.json'))
    for 序号, 材料名 in enumerate(精英材料名列表[2]):
        if 定价关卡列表[序号].endswith('_perm'): 关卡代码 = 游戏关卡数据['stages'][定价关卡列表[序号][:-5]]['code'] + ' 常驻'
        elif 定价关卡列表[序号].endswith('_rep'): 关卡代码 = 游戏关卡数据['stages'][定价关卡列表[序号][:-4]]['code'] + ' 复刻'
        else: 关卡代码 = 游戏关卡数据['stages'][定价关卡列表[序号]]['code']
        界面.Label(定价关卡域, image=精英材料图片列表[2][序号]).grid(row=序号+1, column=0, padx=10, pady=2)
        界面.Label(定价关卡域, text=材料名, foreground=名称颜色[2]).grid(row=序号+1, column=1, padx=10, pady=2)
        界面.Label(定价关卡域, text=format(精英材料价值向量[2][序号], '.2f')).grid(row=序号+1, column=2, padx=10, pady=2)
        界面.Label(定价关卡域, text=关卡代码).grid(row=序号+1, column=3, padx=10, pady=2)

    with open('材料理智定价.csv', 'w', newline="") as 材料理智定价文件:
        导出材料理智定价 = csv.writer(材料理智定价文件)
        导出材料理智定价.writerow(['材料名', '理智定价'])

        for 等级 in range(5):
            界面.Label(精英材料定价域[等级], image=理智图标).grid(row=0, column=0, padx=10, pady=3)
            界面.Label(精英材料定价域[等级], text="材料名称").grid(row=0, column=1, padx=10, pady=3)
            界面.Label(精英材料定价域[等级], text="理智定价").grid(row=0, column=2, padx=10, pady=3)
            # for 序号, 材料名 in enumerate(精英材料名列表[等级]):
            #     界面.Label(精英材料定价域[等级], image=精英材料图片列表[等级][序号]).grid(row=序号+1, column=0, padx=10, pady=2)
            #     界面.Label(精英材料定价域[等级], text=材料名, foreground=名称颜色[等级]).grid(row=序号+1, column=1, padx=10, pady=2)
            #     界面.Label(精英材料定价域[等级], text=format(精英材料价值向量[等级][序号], '.2f')).grid(row=序号+1, column=2, padx=10, pady=2)
            #     导出材料理智定价.writerow([材料名, 精英材料价值向量[等级][序号]])
            for 序号 in range(len(精英材料名列表[等级])):
                界面.Label(精英材料定价域[等级], image=精英材料图片列表[等级][精英材料价值排序表[等级].index(序号+1)]).grid(row=序号+1, column=0, padx=10, pady=2)
                界面.Label(精英材料定价域[等级], text=精英材料名列表[等级][精英材料价值排序表[等级].index(序号+1)], foreground=名称颜色[等级]).grid(row=序号+1, column=1, padx=10, pady=2)
                界面.Label(精英材料定价域[等级], text=format(精英材料价值向量[等级][精英材料价值排序表[等级].index(序号+1)], '.2f')).grid(row=序号+1, column=2, padx=10, pady=2)
                导出材料理智定价.writerow([精英材料名列表[等级][精英材料价值排序表[等级].index(序号+1)], 精英材料价值向量[等级][精英材料价值排序表[等级].index(序号+1)]])

    界面.Label(信用性价比域, image=信用图标).grid(row=0, column=0, padx=10, pady=3)
    界面.Label(信用性价比域, text="材料名称").grid(row=0, column=1, padx=10, pady=3)
    界面.Label(信用性价比域, text="性价比").grid(row=0, column=2, padx=10, pady=3)
    shop_dict = {}
    for 序号 in range(len(信用性价比表[4])):
        shop_dict[信用性价比表[1][信用性价比表[4].index(序号+1)]] = format(100 * [num / max(信用性价比表[3]) for num in 信用性价比表[3]][信用性价比表[4].index(序号+1)], '.2f')
        界面.Label(信用性价比域, image=信用性价比表[0][信用性价比表[4].index(序号+1)]).grid(row=序号+1, column=0, padx=10, pady=2)
        界面.Label(信用性价比域, text=信用性价比表[1][信用性价比表[4].index(序号+1)], foreground=名称颜色[信用性价比表[2][信用性价比表[4].index(序号+1)]]).grid(row=序号+1, column=1, padx=10, pady=2)
        界面.Label(信用性价比域, text=format(100 * [num / max(信用性价比表[3]) for num in 信用性价比表[3]][信用性价比表[4].index(序号+1)], '.2f')).grid(row=序号+1, column=2, padx=10, pady=2)

    with open('shop.json', 'w', newline="") as f:
        f.write(json.dumps(shop_dict, ensure_ascii=False, indent=4))


    行 = 0
    for 阶段 in range(3):
        界面.Label(资质凭证性价比域, image=资质凭证图标).grid(row=行, column=0, padx=10, pady=3)
        界面.Label(资质凭证性价比域, text="材料名称").grid(row=行, column=1, padx=10, pady=3)
        界面.Label(资质凭证性价比域, text="性价比").grid(row=行, column=2, padx=10, pady=3)
        行 += 1
        for 序号 in range(len(资质凭证性价比表[阶段][4])):
            界面.Label(资质凭证性价比域, image=资质凭证性价比表[阶段][0][资质凭证性价比表[阶段][4].index(序号+1)]).grid(row=行, column=0, padx=10, pady=2)
            界面.Label(资质凭证性价比域, text=资质凭证性价比表[阶段][1][资质凭证性价比表[阶段][4].index(序号+1)], foreground=名称颜色[资质凭证性价比表[阶段][2][资质凭证性价比表[阶段][4].index(序号+1)]]).grid(row=行, column=1, padx=10, pady=2)
            界面.Label(资质凭证性价比域, text=format(100 * [num / max(资质凭证性价比表[0][3] + 资质凭证性价比表[1][3] + 资质凭证性价比表[2][3]) for num in 资质凭证性价比表[阶段][3]][资质凭证性价比表[阶段][4].index(序号+1)], '.2f')).grid(row=行, column=2, padx=10, pady=2)
            行 += 1
        if 阶段 < 2:
            界面.Separator(资质凭证性价比域, bootstyle="success").grid(row=行, column=0, columnspan=3, pady=15, sticky=界面.W + E)
            行 += 1

    界面.Label(高级凭证性价比域, image=高级凭证图标).grid(row=0, column=0, padx=10, pady=3)
    界面.Label(高级凭证性价比域, text="材料名称").grid(row=0, column=1, padx=10, pady=3)
    界面.Label(高级凭证性价比域, text="性价比").grid(row=0, column=2, padx=10, pady=3)
    for 序号 in range(len(高级凭证性价比表[4])):
        界面.Label(高级凭证性价比域, image=高级凭证性价比表[0][高级凭证性价比表[4].index(序号+1)]).grid(row=序号+1, column=0, padx=10, pady=2)
        界面.Label(高级凭证性价比域, text=高级凭证性价比表[1][高级凭证性价比表[4].index(序号+1)], foreground=名称颜色[高级凭证性价比表[2][高级凭证性价比表[4].index(序号+1)]]).grid(row=序号+1, column=1, padx=10, pady=2)
        界面.Label(高级凭证性价比域, text=format(100 * [num / max(高级凭证性价比表[3]) for num in 高级凭证性价比表[3]][高级凭证性价比表[4].index(序号+1)], '.2f')).grid(row=序号+1, column=2, padx=10, pady=2)

    界面.Label(寻访参数模型性价比域, image=寻访参数模型图标).grid(row=0, column=0, padx=10, pady=3)
    界面.Label(寻访参数模型性价比域, text="材料名称").grid(row=0, column=1, padx=10, pady=3)
    界面.Label(寻访参数模型性价比域, text="性价比").grid(row=0, column=2, padx=10, pady=3)
    for 序号 in range(len(寻访参数模型性价比表[4])):
        界面.Label(寻访参数模型性价比域, image=寻访参数模型性价比表[0][寻访参数模型性价比表[4].index(序号+1)]).grid(row=序号+1, column=0, padx=10, pady=2)
        界面.Label(寻访参数模型性价比域, text=寻访参数模型性价比表[1][寻访参数模型性价比表[4].index(序号+1)], foreground=名称颜色[寻访参数模型性价比表[2][寻访参数模型性价比表[4].index(序号+1)]]).grid(row=序号+1, column=1, padx=10, pady=2)
        界面.Label(寻访参数模型性价比域, text=format(100 * [num / max(寻访参数模型性价比表[3]) for num in 寻访参数模型性价比表[3]][寻访参数模型性价比表[4].index(序号+1)], '.2f')).grid(row=序号+1, column=2, padx=10, pady=2)

    界面.Label(情报凭证性价比域, image=情报凭证图标).grid(row=0, column=0, padx=10, pady=3)
    界面.Label(情报凭证性价比域, text="材料名称").grid(row=0, column=1, padx=10, pady=3)
    界面.Label(情报凭证性价比域, text="性价比").grid(row=0, column=2, padx=10, pady=3)
    for 序号 in range(len(情报凭证性价比表[4])):
        界面.Label(情报凭证性价比域, image=情报凭证性价比表[0][情报凭证性价比表[4].index(序号+1)]).grid(row=序号+1, column=0, padx=10, pady=2)
        界面.Label(情报凭证性价比域, text=情报凭证性价比表[1][情报凭证性价比表[4].index(序号+1)], foreground=名称颜色[情报凭证性价比表[2][情报凭证性价比表[4].index(序号+1)]]).grid(row=序号+1, column=1, padx=10, pady=2)
        界面.Label(情报凭证性价比域, text=format(100 * [num / max(情报凭证性价比表[3]) for num in 情报凭证性价比表[3]][情报凭证性价比表[4].index(序号+1)], '.2f')).grid(row=序号+1, column=2, padx=10, pady=2)

    提示.configure(text='计算完成！', foreground='#78c2ad')


名称颜色 = ["black", "YellowGreen", "DodgerBlue", "LightSlateBlue", "GoldenRod"]
框架颜色 = ["dark", "success", "info", "secondary", "warning"]
窗口 = 界面.Window(title="罗德岛物价局", themename="minty", iconphoto="图片/标题栏图标.png", size=(1750, 1000), minsize=(0, 0))
窗口.style.configure('primary.TNotebook', tabposition='wn', tabmargins=0, background='#78c2ad')
窗口.style.configure('primary.TNotebook.Tab', font=('微软雅黑', 11))
标签页集 = 界面.Notebook(窗口, style='primary.TNotebook')
标签页集.pack(fill=BOTH, expand=YES)
标签页 = []
滚动区域 = []
for 序号 in range(3):
    标签页.append(界面.Frame(标签页集))
    标签页[序号].rowconfigure(0, weight=1)
    标签页[序号].columnconfigure(0, weight=1)
    滚动区域.append(ScrolledFrame(标签页[序号], autohide=True))
    滚动区域[序号].pack(fill=BOTH, expand=YES)
设置与计算图标 = ImageTk.PhotoImage(Image.open('图片/设置与计算.png').resize((32, 32)))
标签页集.add(标签页[0], text='设置与计算', image=设置与计算图标, compound=TOP)
材料定价表图标 = ImageTk.PhotoImage(Image.open('图片/材料定价表.png').resize((40, 32)))
标签页集.add(标签页[1], text='材料定价表', image=材料定价表图标, compound=TOP)
采购性价比图标 = ImageTk.PhotoImage(Image.open('图片/采购性价比.png'))
标签页集.add(标签页[2], text='采购性价比', image=采购性价比图标, compound=TOP)
# 半透明背景
# c = Image.open('图片/信用.png').resize((300, 300)).convert('RGBA')
# c.putalpha(ImageEnhance.Brightness(c.split()[3]).enhance(0.2))
# 信用背景 = ImageTk.PhotoImage(c)
理智图标 = ImageTk.PhotoImage(Image.open('图片/材料定价表.png'))
信用图标 = ImageTk.PhotoImage(Image.open('图片/信用.png'))
资质凭证图标 = ImageTk.PhotoImage(Image.open('图片/资质凭证.png').resize((40, 40)))
高级凭证图标 = ImageTk.PhotoImage(Image.open('图片/高级凭证.png').resize((40, 40)))
情报凭证图标 = ImageTk.PhotoImage(Image.open('图片/情报凭证.png').resize((31, 40)))
寻访参数模型图标 = ImageTk.PhotoImage(Image.open('图片/寻访参数模型.png').resize((37, 40)))

# 设置与计算标签页
# 价值观域
价值观域 = 界面.LabelFrame(滚动区域[0], text="价值观基础", relief=界面.RIDGE, borderwidth=10)
价值观域.grid(row=0, column=0, sticky=界面.W+E+N+S, padx=10, pady=10)
价值输入列表 = ['龙门币', '经验', '赤金', '合成玉', '寻访凭证', '中坚寻访凭证', '芯片助剂', '模组数据块', '招聘许可', '加急许可', '家具零件']
价值输入 = []
物品图片 = []
for 序号, 物品 in enumerate(价值输入列表):
    行 = 序号
    if 序号 > 2: 行 += 9
    物品原图片 = Image.open(f'图片/{物品}.png')
    宽 = 40 * 物品原图片.size[0] // 物品原图片.size[1]
    物品图片.append(ImageTk.PhotoImage(Image.open(f'图片/{物品}.png').resize((宽, 40))))
    界面.Label(价值观域, image=物品图片[序号]).grid(row=行, pady=5, column=0, sticky=界面.E)
    界面.Label(价值观域, text=f"{物品}价值").grid(row=行, pady=5, column=1, padx=10, sticky=界面.W)
    价值输入.append(界面.Entry(价值观域, justify=RIGHT))
    价值输入[序号].grid(row=行, pady=5, column=2)
    界面.Label(价值观域, text="理智").grid(row=行, padx=5, pady=5, column=3, sticky=界面.W)
价值输入[0].insert(0, '36/10000')
价值输入[1].insert(0, '龙门币价值/1.2468')
价值输入[2].insert(0, '经验价值*2*1000/5')
价值输入[3].insert(0, '135/180')
价值输入[4].insert(0, '合成玉价值*600')
价值输入[5].insert(0, '合成玉价值*600')
价值输入[6].insert(0, '90*30/21')
价值输入[7].insert(0, '120*30/21')
价值输入[8].insert(0, '28.3')
价值输入[9].insert(0, '0')
价值输入[10].insert(0, '0')
界面.Separator(价值观域, bootstyle="light").grid(row=3, column=0, columnspan=5, pady=5, sticky=界面.W+E)
关卡范围 = 界面.StringVar(value='全部历史关卡')
界面.Label(价值观域, text='关卡范围').grid(row=4, pady=5, column=1, padx=10, sticky=界面.E)
界面.Radiobutton(价值观域, text='全部历史关卡', variable=关卡范围, value='全部历史关卡').grid(row=4, pady=5, column=2, sticky=界面.W)
界面.Radiobutton(价值观域, text='当前开放关卡', variable=关卡范围, value='当前开放关卡').grid(row=5, pady=5, column=2, sticky=界面.W)
界面.Radiobutton(价值观域, text='常驻关卡', variable=关卡范围, value='常驻关卡').grid(row=6, pady=5, column=2, sticky=界面.W)
界面.Label(价值观域, text='活动代币换算无限龙门币').grid(row=7, column=2, columnspan=2, ipadx=60, pady=10, sticky=界面.E)
活动代币 = 界面.BooleanVar(value=TRUE)
界面.Checkbutton(价值观域, bootstyle="round-toggle", variable=活动代币, onvalue=TRUE, offvalue=FALSE).grid(row=7, column=1, pady=10, sticky=界面.E)
界面.Separator(价值观域, bootstyle="light").grid(row=8, column=0, columnspan=3, pady=5, sticky=界面.W+E)

# 副产品策略域
副产品策略域 = 界面.LabelFrame(滚动区域[0], text="加工副产品策略", relief=界面.RIDGE, borderwidth=10)
副产品策略域.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky=界面.W+N+S)
加工输入 = []
瑕光 = []
瑕光图标 = ImageTk.PhotoImage(Image.open('图片/瑕光.png').resize((40, 40)))
for 序号 in range(4):
    界面.Label(副产品策略域, text=f"加工T{5-序号}精英材料", foreground=名称颜色[4-序号]).grid(row=3*序号, column=0, columnspan=3, padx=10, pady=5, sticky=界面.E)
    界面.Label(副产品策略域, text="副产品产出概率").grid(row=3*序号, column=3, pady=5, sticky=界面.W)
    瑕光.append(界面.BooleanVar(value=FALSE))
    界面.Checkbutton(副产品策略域, text='瑕光', bootstyle="round-toggle", variable=瑕光[序号], onvalue=TRUE, offvalue=FALSE).grid(row=3*序号+1, column=0, columnspan=2, padx=10, pady=5, sticky=界面.E)
    加工输入.append(界面.Entry(副产品策略域, justify=RIGHT))
    加工输入[序号].grid(row=3*序号+1, column=3, pady=5)
    界面.Label(副产品策略域, image=瑕光图标).grid(row=3*序号+1, column=2, pady=5, sticky=界面.W)
    界面.Label(副产品策略域, text="%", width=3).grid(row=3*序号+1, column=4, padx=5, pady=5, sticky=界面.W)
    if 序号 < 3: 界面.Separator(副产品策略域, bootstyle="light").grid(row=3*序号+2, column=0, columnspan=5, pady=5, sticky=界面.W+E)
加工输入[0].insert(0, '20')
加工输入[1].insert(0, '20')
加工输入[2].insert(0, '10')
加工输入[3].insert(0, '10')
界面.Separator(副产品策略域, bootstyle="primary").grid(row=11, column=0, columnspan=5, pady=10, sticky=界面.W+E)
界面.Label(副产品策略域, text="加工技巧概要").grid(row=12, column=0, columnspan=3, padx=10, pady=5, sticky=界面.E)
界面.Label(副产品策略域, text="副产品产出概率").grid(row=12, column=3, pady=5, sticky=界面.W)
技巧概要卷2图标 = ImageTk.PhotoImage(Image.open('图片/技巧概要·卷2.png').resize((40, 40)))
界面.Label(副产品策略域, image=技巧概要卷2图标).grid(row=13, column=1, pady=5)
技巧概要卷3图标 = ImageTk.PhotoImage(Image.open('图片/技巧概要·卷3.png').resize((40, 40)))
界面.Label(副产品策略域, image=技巧概要卷3图标).grid(row=13, column=2, pady=5)
加工技巧概要输入 = 界面.Entry(副产品策略域, justify=RIGHT)
加工技巧概要输入.grid(row=13, column=3, pady=5)
加工技巧概要输入.insert(0, '10')
界面.Label(副产品策略域, text="%", width=3).grid(row=13, column=4, padx=5, pady=5, sticky=界面.W)
界面.Separator(副产品策略域, bootstyle="light").grid(row=14, column=0, columnspan=5, pady=5, sticky=界面.W+E)
界面.Label(副产品策略域, text="加工基建材料").grid(row=15, column=0, columnspan=3, padx=10, pady=5, sticky=界面.E)
界面.Label(副产品策略域, text="副产品产出概率").grid(row=15, column=3, pady=5, sticky=界面.W)
碳素图标 = ImageTk.PhotoImage(Image.open('图片/碳素.png').resize((40, 40)))
界面.Label(副产品策略域, image=碳素图标).grid(row=16, column=0, pady=5)
碳素组图标 = ImageTk.PhotoImage(Image.open('图片/碳素组.png').resize((40, 40)))
界面.Label(副产品策略域, image=碳素组图标).grid(row=16, column=1, pady=5)
家具零件图标 = ImageTk.PhotoImage(Image.open('图片/家具零件.png').resize((40, 40)))
界面.Label(副产品策略域, image=家具零件图标).grid(row=16, column=2, pady=5)
加工基建材料输入 = 界面.Entry(副产品策略域, justify=RIGHT)
加工基建材料输入.grid(row=16, column=3, pady=5)
加工基建材料输入.insert(0, '10')
界面.Label(副产品策略域, text="%", width=3).grid(row=16, column=4, padx=5, pady=5, sticky=界面.W)
界面.Label(副产品策略域, text="*加工家具零件时减半").grid(row=17, column=3, sticky=界面.W)
界面.Separator(副产品策略域, bootstyle="light").grid(row=19, column=0, columnspan=5, pady=10, sticky=界面.W + E)
界面.Label(副产品策略域, text="九色鹿获取【因果】").grid(row=20, pady=3, column=0, columnspan=3, padx=5, sticky=界面.E)
九色鹿图标 = ImageTk.PhotoImage(Image.open('图片/九色鹿.png').resize((60, 60)))
界面.Label(副产品策略域, image=九色鹿图标).grid(row=21, rowspan=4, column=1, pady=5)
因果图标 = ImageTk.PhotoImage(Image.open('图片/因果.png').resize((40, 40)))
界面.Label(副产品策略域, image=因果图标).grid(row=22, rowspan=4, column=2, pady=5)
加工T3精英材料使用九色鹿获取因果 = 界面.BooleanVar(value=TRUE)
界面.Checkbutton(副产品策略域, text='加工T3精英材料', variable=加工T3精英材料使用九色鹿获取因果, onvalue=TRUE, offvalue=FALSE).grid(row=20, pady=5, column=3, padx=5, sticky=界面.W)
加工T2精英材料使用九色鹿获取因果 = 界面.BooleanVar(value=TRUE)
界面.Checkbutton(副产品策略域, text='加工T2精英材料', variable=加工T2精英材料使用九色鹿获取因果, onvalue=TRUE, offvalue=FALSE).grid(row=21, pady=5, column=3, padx=5, sticky=界面.W)
加工技巧概要使用九色鹿获取因果 = 界面.BooleanVar(value=TRUE)
界面.Checkbutton(副产品策略域, text='加工技巧概要', variable=加工技巧概要使用九色鹿获取因果, onvalue=TRUE, offvalue=FALSE).grid(row=22, pady=5, column=3, padx=5, sticky=界面.W)
加工基建材料使用九色鹿获取因果 = 界面.BooleanVar(value=TRUE)
界面.Checkbutton(副产品策略域, text='加工基建材料', variable=加工基建材料使用九色鹿获取因果, onvalue=TRUE, offvalue=FALSE).grid(row=24, pady=5, column=3, padx=5, sticky=界面.W)

# 定价关卡域
定价关卡域 = 界面.LabelFrame(滚动区域[0], text="T3精英材料关卡理智定价表", relief=界面.RIDGE, bootstyle="info", borderwidth=10)
定价关卡域.grid(row=0, rowspan=4, column=3, columnspan=2, sticky=界面.W+E+N+S, padx=10, pady=10)

界面.Button(滚动区域[0], text="开 始 计 算", bootstyle=(SECONDARY), command=计算工序).grid(row=1, rowspan=3, column=0, padx=10, ipadx=200, ipady=20, sticky=界面.W + E + N + S)
界面.Button(滚动区域[0], text="从Github更新文件与数据", bootstyle=(PRIMARY, "outline-toolbutton"), command=更新文件).grid(row=1, column=1)
界面.Label(滚动区域[0], text='期间请耐心等待其更新完成', foreground='#78c2ad').grid(row=1, column=2, sticky=界面.W)
提示 = 界面.Label(滚动区域[0], text="计算器准备就绪")
提示.grid(row=3, column=1, columnspan=2, sticky=界面.N)

# 材料定价表标签页
滚动区域[1].rowconfigure(0, weight=1)
滚动区域[1].rowconfigure(1, weight=1)
# 精英材料定价域
精英材料定价域 = []
for 等级 in range(5): 精英材料定价域.append(界面.LabelFrame(滚动区域[1], text="T{}精英材料".format(等级+1), relief=界面.RIDGE, bootstyle=框架颜色[等级], borderwidth=10))
精英材料定价域[4].grid(row=0, column=0, sticky=界面.W+E+N+S, pady=10, padx=10)
精英材料定价域[3].grid(row=0, rowspan=2, column=1, sticky=界面.W+E+N+S, pady=10, padx=10)
精英材料定价域[2].grid(row=0, rowspan=2, column=2, sticky=界面.W+E+N+S, pady=10, padx=10)
精英材料定价域[1].grid(row=0, column=3, sticky=界面.W+E+N+S, pady=10, padx=10)
精英材料定价域[0].grid(row=1, column=3, sticky=界面.W+E+N+S, pady=10, padx=10)

# 采购性价比标签页
# 信用性价比域
信用性价比域 = 界面.LabelFrame(滚动区域[2], text="   信用", relief=界面.RIDGE, bootstyle="danger", borderwidth=10)
信用性价比域.grid(row=0, column=0, sticky=界面.W+E+N+S, pady=10, padx=10)
# 资质凭证性价比域
资质凭证性价比域 = 界面.LabelFrame(滚动区域[2], text="资质凭证", relief=界面.RIDGE, bootstyle="success", borderwidth=10)
资质凭证性价比域.grid(row=0, column=1, sticky=界面.W+E+N+S, pady=10, padx=10)
# 高级凭证性价比域
高级凭证性价比域 = 界面.LabelFrame(滚动区域[2], text="高级凭证", relief=界面.RIDGE, bootstyle="warning", borderwidth=10)
高级凭证性价比域.grid(row=0, column=2, sticky=界面.W+E+N+S, pady=10, padx=10)
# 寻访参数模型价比域
寻访参数模型性价比域 = 界面.LabelFrame(滚动区域[2], text="寻访参数模型", relief=界面.RIDGE, bootstyle="danger", borderwidth=10)
寻访参数模型性价比域.grid(row=0, column=3, sticky=界面.W+E+N+S, pady=10, padx=10)
# 情报凭证性价比域
情报凭证性价比域 = 界面.LabelFrame(滚动区域[2], text="情报凭证", relief=界面.RIDGE, bootstyle="info", borderwidth=10)
情报凭证性价比域.grid(row=0, column=4, sticky=界面.W+E+N+S, pady=10, padx=10)

计算工序()
窗口.mainloop()
