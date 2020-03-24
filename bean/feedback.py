# -*- coding: UTF-8 -*-
"""Activity的报名反馈实体类"""
class FeedBack:
    def __init__(self, name, title, status, location, err = None):
        self.name = name
        self.title = title
        self.status = status
        self.location = location
        self.err = err