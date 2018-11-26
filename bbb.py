dict={
"BaseResponse": {
"Ret": 0,
"ErrMsg": ""
}
,
"MemberCount": 410,
"MemberList": [{
"Uin": 0,
"UserName": "@1d34d62d81c03804f6c3eff1bbeeba38",
"NickName": "娱乐星天地",
"HeadImgUrl": "/cgi-bin/mmwebwx-bin/webwxgeticon?seq=620041018&username=@1d34d62d81c03804f6c3eff1bbeeba38&skey=@crypt_b40c533b_d46b37fff3e17eb18e7e9aee9a97464c",
"ContactFlag": 1,
"MemberCount": 0,
"MemberList": [],
"RemarkName": "",
"HideInputBarFlag": 0,
"Sex": 0,
"Signature": "东方卫视王牌娱乐资讯节目。每周一至周五17点-18点，周末17点30分。为您呈现！",
"VerifyFlag": 8,
"OwnerUin": 0,
"PYInitial": "YYXTD",
"PYQuanPin": "yuyuexingtiande",
"RemarkPYInitial": "",
"RemarkPYQuanPin": "",
"StarFriend": 0,
"AppAccountFlag": 0,
"Statues": 0,
"AttrStatus": 0,
"Province": "上海",
"City": "浦东新区",
"Alias": "",
"SnsFlag": 0,
"UniFriend": 0,
"DisplayName": "",
"ChatRoomId": 0,
"KeyWord": "gh_",
"EncryChatRoomId": "",
"IsOwner": 0
}]
}

for i in dict['MemberList']:
    print(i['UserName'])
