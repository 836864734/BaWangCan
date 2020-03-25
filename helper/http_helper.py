import json
import re
from typing import List

import requests
from bean.activity import Activity
from bean.feedback import FeedBack
from bean.user import User
from model.configurator import Configurator
from util import logger, random_sleep_util

logger = logger.getLogger("HttpHelper")


# 查询指定城市的全部符合类别的霸王餐
def list(cityId="1") -> List[Activity]:
    activitys = []
    data = {"cityId": cityId, "type": 0, "mode": "", "page": 1}
    for type in Configurator.types:
        for page in range(1, 15):
            data["page"] = str(page)
            data["type"] = str(type)
            response = requests.post(
                Configurator.list_url,
                headers=Configurator.list_header,
                data=str(json.dumps(data))
            )
            for item in response.json()["data"]["detail"]:
                activitys.append(Activity(item["activityTitle"], item["offlineActivityId"]))
    return activitys


# 批量报名
def regist(list: List[Activity], user: User) -> List[FeedBack]:
    feedbacks = []
    successCount = 0
    registedCount = 0
    errCount = 0
    for activity in list:
        param = Configurator.regist_param
        text = requests.get(Configurator.desc_url + str(activity.id), headers=Configurator.regist_header,
                            cookies={"dper": user.dper}).text
        shopid = re.search(r'shopid:[0-9]*', text).group().split('shopid:')[1]
        param["offlineActivityId"] = str(activity.id)
        param["branchId"] = shopid
        param["phoneNo"] = str(user.phone)
        param["email"] = str(user.qq + "@qq.com")
        response = requests.post(Configurator.regist_url, headers=Configurator.regist_header,
                                 cookies={"dper": user.dper}, data=param)
        msg = json.loads(response.text)
        # 封装反馈结果
        if ("不要重复报名") in msg["msg"]["html"]:
            feedbacks.append(FeedBack(user.name, activity.title, "重复报名", Configurator.desc_url + str(activity.id)))
            registedCount += 1
        elif ("报名成功") in msg["msg"]["html"]:
            feedbacks.append(FeedBack(user.name, activity.title, "报名成功", Configurator.desc_url + str(activity.id)))
            successCount += 1
        else:
            logger.warn(msg)
            feedbacks.append(FeedBack(user.name, activity.title, "报名异常", Configurator.desc_url + str(activity.id),
                                      msg["msg"]["html"]))
            errCount += 1
        # 随机休眠2-10秒
        random_sleep_util.sleep(0, 1)

    logger.info("用户%s成功报名%s条活动", user.name, successCount)
    logger.info("用户%s重复报名%s条活动", user.name, registedCount)
    logger.info("用户%s报名失败%s条活动", user.name, errCount)

    return feedbacks
