# coding=utf-8
"""
@Time    : 2020/02/13  下午 2:51
@Author  : hnm
@FileName: client.py
@IDE     : PyCharm
"""
import json
import requests
from common.readConfig import confParam


class sendRequest(object):
    # sendRequest的构造函数
    def __init__(self):
        pass

    def sendRequest(self, method, url, headers, params=None):
        if method.lower() == "get":
            # 拼凑访问地址
            # url =  url + params
            # 通过get请求访问对应地址
            res = requests.get(url, headers=headers, params=params)
            # 返回request的Response结果，类型为requests的Response类型
            return res
        elif method.lower() == "post":
            # 拼凑访问地址
            if len(params) > 0:
                # 如果有参数，通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.post(url, headers=headers, data=params)
            else:
                # 如果无参数，访问方式如下
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.post(url, headers=headers)
            return res
        elif method.lower() == "put":
            '''
                    封装put方法，url是访问路由，params是put请求需要传递的参数，如果没有参数这里为空
                    :param url: 访问路由
                    :param params: 传递参数，string类型，默认为None
                    :return: 此次访问的response
                    '''
            if params is not None:
                # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.put(url, headers=headers, data=json.dumps(params))
            else:
                # 如果无参数，访问方式如下
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.put(url)
            return res

        elif method.lower() == "delete":
            '''
                    封装delete方法，url是访问路由，params是delete请求需要传递的参数，如果没有参数这里为空
                    :param url: 访问路由
                    :param params: 传递参数，string类型，默认为None
                    :return: 此次访问的response
                    '''
            if params is not None:
                # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.delete(url, hearders=headers, data=params)
            else:
                # 如果无参数，访问方式如下
                # 返回request的Response结果，类型为requests的Response类型
                res = requests.put(url, hearders=headers)
            return res
        else:
            print("无效的请求方式，get/post/put/delete,请查找原因！！！")


if __name__ == "__main__":
    # url = confParam("hostName") + "/auth/1登录"
    url = confParam("hostName") + "/middle/station/stationList"
    client = sendRequest()
    headers = {"authorization":"bd55053d-34dd-42f2-b4f1-52694eb519fb","Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    # params = {"account": "17316918814", "password": "123456", "platform": "1"}
    params = {"supplier": "", "status": "","busiType":"" ,"companyId":"","key": "","pageNo":"1","pageSize":"10"}
    response = client.sendRequest("post", url, headers, params=params)
    print(response.text)

