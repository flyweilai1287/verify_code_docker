# -*- coding:utf-8 -*-
"""
Created on 2019/1/21 21:55
@author: Leo
@file:test.py
@desc:
"""
import requests


def detect_yh_client_result(image_path):
    """封装了tesseract的识别，部署在阿里云上，服务端源码地址为： https://github.com/shidenggui/yh_verify_code_docker"""
    api = "http://127.0.0.1:5000/yh_client"
    # api = "http://yh.ez.shidenggui.com:5000/yh_client"
    with open(image_path, "rb") as f:
        rep = requests.post(api, files={"image": f})
    if rep.status_code != 201:
        error = rep.json()["message"]
        raise requests.exceptions.TradeError("request {} error: {}".format(api, error))
    return rep.json()["result"]

if __name__ == '__main__':
    result=detect_yh_client_result('C:\\Users\\leo\\AppData\\Local\\Temp\\tmpq1rv5wgd.jpg')
    print(':::'+result)