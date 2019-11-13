import pywifi
from pywifi import const  # 引入常量


def gic():
    # 创建一个wifi对象
    wifi = pywifi.PyWiFi()
    print(wifi)

    # 获取无线网卡
    interface = wifi.interfaces()[0]
    name = interface.name()
    status = interface.status()

    if interface.status() == const.IFACE_DISCONNECTED:
        print('未连接')
    elif interface.status() == const.IFACE_CONNECTED:
        print('已连接')
    elif interface.status() == const.IFACE_CONNECTING:
        print('正在连接')
    elif interface.status() == const.IFACE_INACTIVE:
        print('已禁用')
    elif interface.status() == const.IFACE_SCANNING:
        print('已禁用')
    else:
        print('网卡状态异常')


def san():
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]

    interface.scan()

    scan_res = interface.scan_results()

    for _ in scan_res:
        print("{0:^20} \t {1:^20} \t ".format(_.ssid, _.bssid))


if __name__ == '__main__':
    san()
