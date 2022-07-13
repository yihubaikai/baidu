# encoding:utf-8

import requests
import base64
import json

'''
身份证识别
APPID      :26448537
API Key   ：QVAxGOLHvi3ItkUnoHuUwddY
Secret Key：pq4wnf4zDfTQfWwehjHO8iARkpuIAIfo
'''
APIKey    = "QVAxGOLHvi3ItkUnoHuUwddY"
SecretKey = "pq4wnf4zDfTQfWwehjHO8iARkpuIAIfo"

def Get_Token():
    #host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+APIKey+'&client_secret='+SecretKey
    response = requests.get(host)
    if response:
        js = response.json()
        access_token = js["access_token"]
        print(access_token)
        return access_token
    return ""

def BD_OCR_indiney(access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    f = open('sfz001.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"id_card_side":"front","image":img}
    access_token = access_token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        #print (response.json())
        js = response.json()
        #print( json.dumps(js))
        _name = js["words_result"]["姓名"]["words"]
        _addr = js["words_result"]["住址"]["words"]
        _Numb = js["words_result"]["公民身份号码"]["words"]
        _Minz = js["words_result"]["民族"]["words"]
        _Birt = js["words_result"]["出生"]["words"]
        _Sexy = js["words_result"]["性别"]["words"]
        ret   = _name+"_"+_Sexy+"_"+_Minz+"_"+_Numb+"_"+_Birt+"_"+_addr
        print( ret )
        return ret
    return ""


def main():
    ak = Get_Token()
    BD_OCR_indiney(ak)


if __name__ == '__main__':
    main()