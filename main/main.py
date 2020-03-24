from helper.users_config_helper import loadConfig
from helper.http_helper import HttpHelper

# logger...
from util.logger import Logger

logger = Logger.getLogger("main")
# 从配置文件中获取所有的user
users = loadConfig()
# 为每一个user报名
for user in users:
    # 获取全部霸王餐ID
    activities = HttpHelper.list("1")
    logger.debug("用户%s查询到%s条活动", user.name, len(activities))
    # 全部报名
    feedBacks = HttpHelper.regist(activities, user)
    pass