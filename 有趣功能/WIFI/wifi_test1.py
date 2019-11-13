from tkinter import *
from pywifi import const
import time
import pywifi


def wificonnect(wifiname, pwd):
    '''
    导入模块
    获取无线网卡
    断开wifi
    读取密码本
    设置睡眠时间
    '''
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]

    interface.disconnect()

    if interface.status() == const.IFACE_DISCONNECTED:

        profile = pywifi.Profile()
        # wifi密码
        profile.ssid = wifiname
        # 网卡加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 网卡密码
        profile.key = pwd
        # 网卡加密方式
        profile.auth = const.AUTH_ALG_OPEN

        # 删除所有已有wifiprofile文件
        interface.remove_all_network_profiles()

        # 调用设置profile
        temp_profile = interface.add_network_profile(profile)

        # 连接wifi
        interface.connect(temp_profile)
        time.sleep(4)  # 睡眠4秒连接wifi

        if interface.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("wifi当前已经连接！")

    pass


def readPwd():
    # 获取wifi
    wifiname = entry.get()
    path = r'D:\Project&Files\Python_basic\有趣功能\wifipass.txt'
    with open(path, 'r') as pwd:
        while True:
            try:
                # 读取密码字典一行
                myStr = pwd.readline()

                # 测试密码
                bool = wificonnect()
                if bool:
                    print(wifiname + "】的正确密码:" + myStr)
                else:
                    text.insert(END, "密码错误: " + myStr)  # 在字符列表最后插入错误密码
                    text.see(END)  # 定位到最后一行
                    text.update()  # 刷新字符列表
            except:
                continue


# 创建窗口
root = Tk()

# 窗口标题
root.title("myFrame")

# 窗口大小(像素)
root.geometry('500x260')

# 初始化开始位置
root.geometry('+200+200')

# 上面两个可以合并写：root.geometry('200x400+200+200')

# 标签空间
label = Label(root, text='输入WIFI名称:')

# 定位label位置
label.grid()  # 网格式布局   pack：包布局    place：像素位置布局

# 输入控件
entry = Entry(root, font=('微软雅黑', 20))
entry.grid(row=0, column=1)

# 列表框空间
text = Listbox(root, width=80, height=10)
text.grid(row=1, columnspan=2)  # 跨列

button = Button(root, text='开始', width=20, height=1)
button.grid(row=2, columnspan=2)

# 显示窗口  （消息循环）
root.mainloop()
