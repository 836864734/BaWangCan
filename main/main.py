from helper import http_helper, users_config_helper
from util import logger

logger = logger.getLogger("main")
# 从配置文件中获取所有的user
users = users_config_helper.loadConfig()
# 为每一个user报名
for user in users:
    # 获取全部霸王餐ID
    activities = http_helper.list()
    logger.debug("用户%s查询到%s条活动", user.name, len(activities))
    # 全部报名
    feedBacks = http_helper.regist(list=activities, user=user)
    continue
