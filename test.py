import requests
import json
import datetime
import time
#url='https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA5NDIzNzY1OQ==&f=json&offset=10&count=10&is_ok=1&scene=126&uin=777&key=777&pass_ticket=C9fyU0E8XhybQ4c5Kw3Ez6Hkmux2be9nnq0huaB1NsYMzdR3CwOxL67v7MlVZW37&wxtoken=&appmsg_token=981_7ajNvxQ7AMGV3ZJrbsahNpfXQT9Vr67zYT71wg~~&x5=0&f=json'
#url='action=getmsg&__biz=MzA4MjEyNTA5Mw==&f=json&offset=10&count=10&is_ok=1&scene=126&uin=777&key=777&pass_ticket=W9kNtykST9OhY7cDvM%2FjuNr9tFH7BFpsukKrH2Qxk74cIfgV8BUP8tmuA2B%2F%2Fgkj&wxtoken=&appmsg_token=981_aleRlJXX%252FotFC6Rj7rONRqN_E-Nd8IFXBRhzOg~~&x5=0&f=json'
headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9sk Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/359 MMWEBSDK/180801 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x2607036C) NetType/WIFI Language/zh_CN Process/toolsmp',
'Cookie':'sd_userid=24071536902087593; sd_cookie_crttime=1536902087593; pgv_pvid=9975451308; rewardsn=; wxtokenkey=777; wxuin=1826731782; devicetype=android-23; version=2607036c; lang=zh_CN; pass_ticket=W9kNtykST9OhY7cDvM/juNr9tFH7BFpsukKrH2Qxk74cIfgV8BUP8tmuA2B//gkj; wap_sid2=CIbuhucGEnBESmZIZUJRcW11eHlUV2lhR1MxOFFsejBMRFh1cE13dG5mZHFuY0ZTbllWenotYlpNZkQzMWM1TXA4U0lzT1dJZTNDeWpYenV4ZGgxdlBXd3l3N0FTY0xqTGwzdmljMVYxdnB4UjZpRkN1TFZBd0FBMLLs794FOA1AlU4='
         }
offset=10
while True:
    url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4MjEyNTA5Mw==&f=json&offset={0}&count=10&' \
          'is_ok=1&scene=126&uin=777&key=777&pass_ticket=W9kNtykST9OhY7cDvM%2FjuNr9tFH7BFpsukKrH2Qxk74cIfgV8BUP8tmuA2B%2F%2Fgkj&wxtoken=&' \
          'appmsg_token=981_aleRlJXX%252FotFC6Rj7rONRqN_E-Nd8IFXBRhzOg~~&x5=0&f=json'.format(offset)

    resp = requests.get(url, headers=headers,verify=False).json()
    msg=resp.get('errmsg')
    stu=resp.get('ret')
    # if stu == 0 or msg == 'ok':
    general_msg_list=resp.get('general_msg_list')  #list
    #msg_list=general_msg_list['list']
    msg_list = json.loads(general_msg_list)['list']
    #comm_msg_info = msg['comm_msg_info']
    #print(msg_list)
    for items in msg_list:

        #post_time = datetime.fromtimestamp(comm_msg_info['datetime'])
        print(items['app_msg_ext_info']['title'])
    #if stu==0 or msg=='ok':
        #print(url)
        offset=resp.get('next_offset')
