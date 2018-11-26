import requests
import time
import json
# init_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=407267817&lang=zh_CN&pass_ticket=ISlKGlP5riujgmwGK0l88gjPyAFsSRgWDX3P%252FziNteAH%252Fg1eEOWObDoo%252F%252BF7oyuy'
# post_data = {
#             "BaseRequest": {
#                 'DeviceID':"e309376293628595",
#                 'Skey':"@crypt_b40c533b_be4e099e3a54308495e79174fd7c0d3b",
#                 'Uin':"1826731782",
#                 'Sid':"8bqV/KUgLooIXT3D",
#             }
#         }
# r3=requests.post(
#             url=init_url,
#             json=post_data,
#             verify=False,)
# print(r3.text)


# ctime = int(time.time() * 1000)
# base_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket=ISlKGlP5riujgmwGK0l88gjPyAFsSRgWDX3P%252FziNteAH%252Fg1eEOWObDoo%252F%252BF7oyuy&r={0}&seq=0&skey=@crypt_b40c533b_be4e099e3a54308495e79174fd7c0d3b".format(
#     ctime)
#
# # cookies = {}
# # cookies.update(req.session['LOGIN_COOKIES'])
# # cookies.update(req.session['TICKET_COOKIES'])
#
# Cookie ={'webwx_data_ticket': 'gSfE13UKqVs092OiIjO7ifLV', 'mm_lang': 'zh_CN', 'webwx_auth_ticket': 'CIsBEMfuv/0BGoABj/k8KG1OFYaomDDWf4/PNFHCAs25JWCuYUfJNzIZqOYzqj9Ohp+wu77/oQLXwFgHhBDGNxAUu1ekrdtO577wwsJOlKa36rfcXlffZrtf/iRLdLJ4I+wBbvJXndvoQBc3UhdPznrsy1DRY2IhUQ7oUmi8ifTHfGhWfToazbx6Rws=', 'webwxuvid': '6daf4ea73911c27ba25bf5086f22369c4b2ca282f782c4e5cbba4847465236d9014aff591d52b4c4ceaa45a91a72bccd', 'wxloadtime': '1541486031', 'wxsid': '8bqV/KUgLooIXT3', 'wxuin': '1826731782'}
#
#
#
#
#
#
#
# r1 = requests.get(base_url, cookies=Cookie,verify=False,)
# r1.encoding = 'utf-8'
# print(r1.text)




pass_ticket='%2FZkET%2BSzh5g3e6c3Cg0tzgf8PDri2dvIxEh%2FszVZMU%2BO3VEfIAb0oSeIdzWEZusP'
sid='Td8IALZZaHe+9iRh'
uin='2479493837'
skey='@crypt_f948ad5c_4639c1c422b42d22d053e2b737e44840'
# username_list=req.session['use1r_dict']
# print(username_list[i])
# for i in user_dict['MemberList']:
#     print(i['UserName'])

#print(username_list['MemberList'][i]['UserName'])
#count=int(len(username_list))  #联系公众号总数


ctime = int(time.time() * 1000)
post_data = {
    "BaseRequest":{
        "DeviceID": "e384757757885382",
        'Sid': sid,
        'Uin': uin,
        'Skey': skey,
    },
    "Msg":{
        "ClientMsgId":ctime,
            "LocalID":ctime,
        "FromUserName": '@a0564fe9f11cfa16511efc8ca75a4cdda70b6e8615800ad4d60e89f0d28f26ad',
         # @ a0564fe9f11cfa16511efc8ca75a4cdda70b6e8615800ad4d60e89f0d28f26ad
        "ToUserName":'@6f982be166f9886db60414c0637f6f73',
        "Content": "测试",
        "Type": 1
    },
    "Scene": 0
}

url = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket=%252FZkET%252BSzh5g3e6c3Cg0tzgf8PDri2dvIxEh%252FszVZMU%252BO3VEfIAb0oSeIdzWEZusP"
# res = requests.post(url=url,json=post_data) # application/json,json.dumps(post_data)
# res = requests.post(url=url,data=json.dumps(post_data),headers={'Content-Type': "application/json"}) # application/json,json.dumps(post_data)
Cookie = {'webwx_data_ticket': 'gSfgkWXLY4c4X/8SgpePuaJT',
          'mm_lang': 'zh_CN',
          'webwx_auth_ticket': 'CIsBENakxesEGoABy0U9qyAZNLr4xCkHv+P+/at94yYOkTf//RuK5X/NLUFuVYqeZQShp2RFDYS45xhMb/8UWfnkyVxjnT4LI7G65LwKHCTTseRnpMpsHvb6DVpUhuF96EDNie5O/DoRF/9drRszj45Hc20TUuOBS9BhrF6uYhTc0XC0Azruc4YODpY=',
          'webwxuvid': '9b90f614758067e8d821bc128d8858afafa9d18e90a8fbe1f8140e476c7b5d468db7fde7609c3e1c4d229c4576808615',
          'wxloadtime': '1541557160_expired',
          'wxsid': 'Td8IALZZaHe+9iRh',
          'wxuin': '2479493837',
          'last_wxuin': '2479493837',
          'MM_WX_NOTIFY_STATE': '1',
          'MM_WX_SOUND_STATE': '1',
          'wxpluginkey': '1541545802',
          'login_frequency': '1'
          }
res = requests.post(url=url,data=json.dumps(post_data,ensure_ascii=False).encode('utf-8'),headers={'Content-Type': "application/json"},cookies=Cookie,verify=False) # application/json,json.dumps(post_data)
print(res.text)

