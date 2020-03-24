# 从配置文件中读取所有的user
from lxml import etree

from bean.user import User


def loadConfig():
    tree = etree.parse("../conf/users.xml")
    root = tree.getroot()
    users = []
    for userElement in root:
        for item in userElement:
            if item.tag == "name":
                name = item.text
            elif item.tag == "cityId":
                cityId = item.text
            elif item.tag == "dper":
                dper = item.text
            elif item.tag == "phone":
                phone = item.text
            elif item.tag == "qq":
                qq = item.text
        users.append(User(name, cityId, dper, phone, qq))
    return users
