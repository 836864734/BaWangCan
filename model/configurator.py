class Configurator:
    # 报名哪些类别
    types = [1, 2, 6, 99]

    # 请求霸王餐列表的url
    list_url = "http://m.dianping.com/activity/static/pc/ajaxList"

    # 查看详情的url
    desc_url = "http://s.dianping.com/event/"

    # 报名的url
    regist_url = "http://s.dianping.com/ajax/json/activity/offline/saveApplyInfo"

    # 报名的param
    regist_param = {
        'shippingAddress': '',
        'extraCount': '',
        'birthdayStr': '',
        'marryDayStr': '',
        'babyBirths': '',
        'pregnant': '',
        'marryStatus': '0',
        'comboId': '1',
        'usePassCard': '0',
        'passCardNo': '',
        'isShareSina': 'false',
        'isShareQQ': 'false'
    }

    # 获取霸王餐列表的请求头
    list_header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://s.dianping.com/event/beijing',
        'Origin': 'http://s.dianping.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Content-Type': 'application/json',
    }
    # 报名的请求头
    regist_header = {
        'Origin': 'http://s.dianping.com',
        'Accept-Encoding': 'gzip, deflate',
        'X-Request': 'JSON',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8;',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept': 'application/json, text/javascript',
        'Referer': 'http://s.dianping.com/event/1063463422',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }
