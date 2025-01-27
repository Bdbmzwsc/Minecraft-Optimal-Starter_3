# coding=utf-8
import json
import os
from sys import platform
from .Log import print_


def JsonRead(JsonFile):
    """
        读取Json
        JsonFile = Json的目录
    """
    with open(JsonFile, 'r', encoding='utf_8') as f:
        r = json.load(f, strict=False)
    return r


def JsonFile():
    """获取Json路径"""
    a = File()
    b = os.path.join(a, 'MOS.json')
    return b


def JsonWrite(Json_, JsonFile):
    """
        写入Json
        :param Json_: Json内容
        :param JsonFile: Json路径
    """
    with open(JsonFile, 'w+', encoding='utf_8') as f:
        json.dump(Json_, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    print_('Info',str('写入Json(启动器配置Json)  内容:\n') + str(Json_))

    return 'OK'


def Json_Cheak(JsonFile):
    """检查Json是否所有值都有"""
    J_C = Json_InitializeFirst()
    J = JsonRead(JsonFile)
    C = 0  # 存储C中是否少参数
    for J_C_1 in J_C:
        if J_C_1 not in J:
            J[J_C_1] = J_C[J_C_1]
            C = 1
    if C == 1:
        # 如果少参数
        JsonWrite(J, JsonFile)
        return True  # 需要进行补全,补全文件
    else:
        return False  # 不需要进行补全


def Json_InitializeFirst():
    """返回Json默认(字典)"""
    J = {
        'Subject': 'Light',
        'BackGround': False,
        'Sidebar_Sidebar_Time': 15,  # 左边栏动画延迟
        'UserPage_setChoice': 'Choices',
        'Users': {},
        'GameFile': {
            '当前目录': {
                'Name': '当前目录',
                'File': os.path.join(os.path.dirname(File()), '.minecraft')
            }
        }
    }
    return J


def InitializeFirst():
    """在第一次运行时，初始化"""
    f = ['Download', 'Music', 'Java', 'Html', 'Mod', 'Logs']
    q = File()
    for f_1 in f:
        file = os.path.join(q, f_1)
        os.makedirs(file, exist_ok=True)

    JsonFile_ = JsonFile()

    J = Json_InitializeFirst()

    with open(JsonFile_, 'w', encoding='utf-8') as f:
        json.dump(J, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


def File():
    """获取缓存目录"""
    s = Systeam()
    if s == 'Mac':
        # 获取当前系统用户目录
        UserFile = os.path.expanduser('~')
        file = os.path.join(UserFile, 'Documents', '.MOS')
    else:
        file = '.MOS'
    return file


def Systeam():
    """
        return: Mac Win Linux

        注意：在本项目中 Cygwin系统 算作Win AIX系统 算作Linux

        'win32':Windows
        'cygwin':Windows/Cygwin
        'darwin':macOS
        'aix':AIX
        'linux':Linux
    """
    a = str(platform)
    if a == 'win32' or a == 'cygwin':
        s = 'Win'
        print(a)
    elif a == 'darwin':
        s = 'Mac'
    elif a == 'linux' or a == 'aix':
        s = 'Linux'
    return s
