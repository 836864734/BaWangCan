# -*- coding: UTF-8 -*-
"""用户实体类"""
class User:
    def __init__(self, name, cityId, dper, phone=None, qq=None):
        self.name = name
        self.cityId = cityId
        self.dper = dper
        self.phone = phone
        self.qq = qq