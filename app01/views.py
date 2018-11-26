from django.shortcuts import render,HttpResponse
import requests
import time
import re
import json
from bs4 import BeautifulSoup

# Create your views here.


def ticket(html):
    tdict={}
    soup=BeautifulSoup(html,'html.parser')
    tag=soup.find(name='error').find_all()
    for t in tag:
        tdict[t.name]=t.text

    return tdict

def get_alluser():
    ctime = int(time.time() * 1000)
    base_url = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket=SnsnLgpnrJxDzmw50QQJpDw8WIFyGiOK8yzxIRHTbOTwInnXv8KsMIn994Led5Vf&r={0}&seq=0&skey=@crypt_f948ad5c_3c8fcb8dc3310cdee8d5bd7cca8197fc".format(
        ctime)

    # cookies = {}
    # cookies.update(req.session['LOGIN_COOKIES'])
    # cookies.update(req.session['TICKET_COOKIES'])
    Cookie = {'webwx_data_ticket': 'gSeOAIGIbuEcRHWkiShvFQus', 'mm_lang': 'zh_CN', 'webwx_auth_ticket': 'CIsBEL6p0coMGoABg5eFqYoYIdySHB3VfAyHv6t94yYOkTf//RuK5X/NLUEWhJrM1ZEu2cKhtoqc692xqtg957FPcGGmLJZWCgJBYrqENa/w2L46qoLSYfHwZGcxSc+p/1BtpbYyWJLcvXQtkAswahbYwYExZ8CHxqmSkl6uYhTc0XC0Azruc4YODpY=', 'webwxuvid': '9b90f614758067e8d821bc128d8858af930778825eeb7a19e1cefdd573a203dba411084680107a41bd722c3ffe462867', 'wxloadtime': '1541469481', 'wxsid': 'HDscrHRtNoL+qKYz', 'wxuin': '2479493837'}




    r1 = requests.get(base_url, cookies=Cookie)
    r1.encoding = 'utf-8'
    print(r1.text)
    return r1.text
def login(req):
    if req.method=='GET':
        uuid_time=int(time.time()*1000)  #获取时间戳
        base_uuid_url='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'
        uuid_url=base_uuid_url.format(uuid_time)  #格式化URL 传入uuid_time
        r1=requests.get(uuid_url)  #请求地址
        #print(r1.text)
        result=re.findall('= "(.*)";',r1.text)
        #print(result)
        uuid=result[0]

        req.session['UUID_TIME']=uuid_time  #存入session
        req.session['UUID']=uuid
        return render(req,'login.html',{'uuid':uuid})

def check_login(req):

    response={'code':408,'data':None}
    c_time = int(time.time() * 1000)
    base_login_url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=1457378564&_={1}"
    login_url=base_login_url.format(req.session['UUID'],c_time)
    r=requests.get(login_url)
    print(r.text)
    if 'window.code=408' in r.text:
        #无人扫码
        response['code']=408
    elif 'window.code=201' in r.text:
        #扫码获取头像
        response['code']=201
        response['data']=re.findall("window.userAvatar = '(.*)='",r.text)[0]
    #print(r.text)
    elif 'window.code=200' in r.text:
        #点击登录
        req.session['LOGIN_COOKIES']=r.cookies.get_dict()
        print(r.cookies.get_dict())
        base_redirect_url=re.findall('redirect_uri="(.*)";',r.text)[0]
        print(base_redirect_url)

        redirect_url=base_redirect_url+'&fun=new&version=v2&lang=zh_CN'
        print(redirect_url)

        #获取凭证
        r2=requests.get(redirect_url,verify=False)
        #r2=requests.get(base_redirect_url)  #特例Url
        ticket_dict=ticket(r2.text)
        #print(ticket_dict)
        req.session['TICKET_DICT']=ticket_dict   #存入session
        req.session['TICKET_COOKIES']=r2.cookies.get_dict()

        print(r2.cookies.get_dict())
        print('__________________________________________________________')
        cookies = {}
        cookies.update(req.session['LOGIN_COOKIES'])
        cookies.update(req.session['TICKET_COOKIES'])
        print(cookies)
        req.session['all_session']=cookies
        #初始化，获取最近联系人信息
        #StringDeviceID = "e" + String.valueOf(newRandom().nextLong()).substring(1, 16)
        post_data = {
            "BaseRequest": {
                "DeviceID": "e176085775436639",
                #   e876442388480809
                'Sid': ticket_dict['wxsid'],
                'Uin': ticket_dict['wxuin'],
                'Skey': ticket_dict['skey'],
            }
        }
        print(post_data)
        print(ticket_dict['pass_ticket'])
        init_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=426162624&lang=zh_CN&pass_ticket={0}'.format(ticket_dict['pass_ticket'])
        #    1442528109                                              493115868    492928249   492670836  492610883
        # session = requests.Session()
        # session.verify=False
        #cookies=r2.cookies.get_dict() #登录cook
        # s = requests.session()
        # c = requests.cookies.RequestsCookieJar()  # 利用RequestsCookieJar获取
        # c.set('cookie-name', 'cookie-value')
        #s.cookies.update(c)
        r3=requests.post(
            url=init_url,
            json=post_data,
            verify=False,

        )
        #print(r3.text)
        r3.encoding='utf-8'
        #r3.encoding = r3.apparent_encoding
        init_dict=json.loads(r3.text)  #将json数据转换为字典
        #print(init_dict)

        # for k,v in init_dict.items():
        #       print(k,v)

        req.session['INIT_DICT']=init_dict
        response['code']=200
        pass

    return HttpResponse(json.dumps(response))

# def avatar(req):   #获取头像的方法
#     prav=req.GET.get('prav')
#     username=req.GET.get('username')
#     skey = req.GET.get('skey')
#     img_url = "https://wx.qq.com{0}&username={1}&skey={2}".format(prav, username, skey)
#     #rimg = requests.get(img_url, headers={'Referer': 'https://wx.qq.com/'})
#     #print(img_url)
#     cookies = {}
#     cookies.update(req.session['LOGIN_COOKIES'])
#     cookies.update(req.session['TICKET_COOKIES'])
#     #print(img_url)
#     res = requests.get(img_url, cookies=cookies, headers={'Content-Type': 'image/jpeg'})
#     return HttpResponse(res.content)

def index(req):
    '''
    显示最近联系人
    :param req:
    :return:
    '''
    return render(req,'index.html')
def contact_list(req):
    '''
    获取所有联系人
    :param req:
    :return:
    '''
    ctime = int(time.time() * 1000)
    base_url = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket=FUAbu1Blbbi0LRvW07cJnzSD4NTcd8CsY%252FVnJSHwiuGoUgJkrMiRH9VMELL9ZTL4&r={0}&seq=0&skey=@crypt_f948ad5c_8b19be3483ecb401a2033279139d7729".format(ctime)

    # cookies = {}
    # cookies.update(req.session['LOGIN_COOKIES'])
    # cookies.update(req.session['TICKET_COOKIES'])

    Cookie = {'webwx_data_ticket': 'gSd0yZ3JMcAAkIjQL1Z9PLg0',
              'mm_lang': 'zh_CN',
              'webwx_auth_ticket': 'CIsBEJKn/a4PGoABlvLGzq3+CrSj7LidK1uxRKt94yYOkTf//RuK5X/NLUFuVYqeZQShp2RFDYS45xhMb/8UWfnkyVxjnT4LI7G65LwKHCTTseRnpMpsHvb6DVpUhuF96EDNie5O/DoRF/9drRszj45Hc20TUuOBS9BhrF6uYhTc0XC0Azruc4YODpY=',
              'webwxuvid': '9b90f614758067e8d821bc128d8858afafa9d18e90a8fbe1f8140e476c7b5d468db7fde7609c3e1c4d229c4576808615',
              'wxloadtime': '1541578156',
              'wxsid': 'YU0bKbuv5sueVuNG',
              'wxuin': '2479493837',
              'last_wxuin': '2479493837',
              'MM_WX_NOTIFY_STATE': '1',
              'MM_WX_SOUND_STATE': '1',
              'wxpluginkey': '1541574000',
              'login_frequency': '3'
              }

    #r1 = requests.get(base_url, cookies=Cookie)
    r1 = requests.get(base_url, cookies=Cookie)
    r1.encoding = 'utf-8'
    print(r1.text)

    user_list = json.loads(r1.text)
    public=[]
    public_nickname = []
    for p in user_list['MemberList']:   #获取ContactFlay为3的联系人信息  24服务号 8 公众号
        if int(p['VerifyFlag'])==8 or int(p['VerifyFlag'])==24:
            public.append(p['UserName'])
            public_nickname.append(p['NickName'])
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print( public)
    user_public=public
    pcount=len(user_public)
    req.session['use1r_dict'] = user_public
    return render(req, 'contact_list.html', {'user_list': user_list,'pcount':pcount,'public':public,'public_nickname':public_nickname})

def send_msg(req):
    """
    发送消息
    :param req:
    :return:
    """
    response={"count":None}
    #current_user = req.session['INIT_DICT']['User']['UserName'] # session初始化，User.UserName
    #to = req.POST.get('to') # @dfb23e0da382f51746575a038323834a
    i=int(req.POST.get('index'))
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print(type(i))

    msg = req.POST.get('msg')# asdfasdfasdf
    # print('_____________________________')
    # print(type(to))
    # print(to)
    # session Ticket
    # session Cookie
    #ticket_dict = req.session['TICKET_DICT']
    pass_ticket='%2FZkET%2BSzh5g3e6c3Cg0tzgf8PDri2dvIxEh%2FszVZMU%2BO3VEfIAb0oSeIdzWEZusP'
    sid='YU0bKbuv5sueVuNG'   #更换sid   uin   skey   passticket  init 接口
    uin='2479493837'
    skey='@crypt_f948ad5c_8b19be3483ecb401a2033279139d7729'
    username_list=req.session['use1r_dict']
    print(username_list[i])
    # for i in user_dict['MemberList']:
    #     print(i['UserName'])

    #print(username_list['MemberList'][i]['UserName'])
    count=int(len(username_list))  #联系公众号总数
    response['count']=count

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
            "FromUserName": '@7cd4936a4cbea7d7e450b4f8e03268c5e144e4a41949a30ecafe15f871effdbf',  #用户名更换
             # @ a0564fe9f11cfa16511efc8ca75a4cdda70b6e8615800ad4d60e89f0d28f26ad
            "ToUserName":username_list[i],
            "Content": msg,
            "Type": 1
        },
        "Scene": 0
    }
    # url更换               wxloadtime   更换_expired   更换pass_ticket
    url = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket=FUAbu1Blbbi0LRvW07cJnzSD4NTcd8CsY%252FVnJSHwiuGoUgJkrMiRH9VMELL9ZTL4"
    # res = requests.post(url=url,json=post_data) # application/json,json.dumps(post_data)
    # res = requests.post(url=url,data=json.dumps(post_data),headers={'Content-Type': "application/json"}) # application/json,json.dumps(post_data)
    Cookie = {'webwx_data_ticket': 'gSd0yZ3JMcAAkIjQL1Z9PLg0',
              'mm_lang': 'zh_CN',
              'webwx_auth_ticket': 'CIsBEJKn/a4PGoABlvLGzq3+CrSj7LidK1uxRKt94yYOkTf//RuK5X/NLUFuVYqeZQShp2RFDYS45xhMb/8UWfnkyVxjnT4LI7G65LwKHCTTseRnpMpsHvb6DVpUhuF96EDNie5O/DoRF/9drRszj45Hc20TUuOBS9BhrF6uYhTc0XC0Azruc4YODpY=',
              'webwxuvid': '9b90f614758067e8d821bc128d8858afafa9d18e90a8fbe1f8140e476c7b5d468db7fde7609c3e1c4d229c4576808615',
              'wxloadtime': '1541578156_expired',
              'wxsid': 'YU0bKbuv5sueVuNG',
              'wxuin': '2479493837',
              'last_wxuin': '2479493837',
              'MM_WX_NOTIFY_STATE': '1',
              'MM_WX_SOUND_STATE': '1',
              'wxpluginkey': '1541574000',
              'login_frequency': '3'
              }
    res = requests.post(url=url,data=json.dumps(post_data,ensure_ascii=False).encode('utf-8'),headers={'Content-Type': "application/json"},cookies=Cookie,verify=False) # application/json,json.dumps(post_data)
    print(res.text)
    return HttpResponse('...')