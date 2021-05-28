import json
import urllib3
import requests

login_url = "http://preuserauth.tanwin.cn:7078/auth/login"


def login():
    data = {"account": "17316918814", "password": "123456", "platform": "1"}
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    response = requests.post(url=login_url, data=data, headers=headers)
    print(response.text)
    #cookie = response.headers['Set-Cookie']
    #print(cookie)
    cookie = response.headers['Set-Cookie'].split(";")[0].split("=")[1]
    print(cookie)
    return cookie



def get_user_info():
    params = {"taskId": "1844102","clientName":"电运","clientPhone":"15397059360","completeAddress":"浙江省杭州市桐庐县古古怪怪刚刚干活","capacitySize":1360.00,"reason":"这是工单需求","appointment":"2021-12-09 09:30:00,2021-12-09 11:30:00","beforeVideoBid":"","SUBMIT_SERVICE_API_PUSH_100":"9,1000000,,workorderflow/processpush","globalbutton_1616744550238":0}
    headers = {"token":"2a0542dc-510c-45df-819d-3ad7069314b3", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
   # headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    url = "http://preflowengine.tanwin.cn:8335/process/client/completeTask"
    resp = requests.post(url, params=params, headers=headers)
    #print(resp.text)# 接口返回文本信息

    # 把文本信息转化为字典格式
    text_dict = json.loads(resp.text)
    print(text_dict)

def get_workid_info():
    params = {'provinceNo': '330000', 'cityNo': '330100', 'areaNo': '330122', 'stationId': '66', 'projectId': '50596', 'projectNo': 'TF20210426150552002', 'clientId': '17', 'clientName': '电运', 'clientPhone': '17316918814', 'completeAddress': '古古怪怪刚刚干活', 'appointment': '2021-05-23 09:30:00,2021-05-23 11:30:00', 'companyId': '1705', 'companyName': '桐庐测试企业', 'capacitySize': '1360.00', 'reason': '这是申请售后填写的内容', 'address': '浙江省 杭州市 桐庐县', 'workType': 0, 'source': 2, 'beforeImgBid': 'http://photo.tanwin.cn/tempfile/2021-05-17/542a09d6e465db1c626d88502bb4178c.jpg', 'beforeVideoBid': ''}
    headers = {"token":login(), "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
   # headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    url = "http://preuserauth.tanwin.cn:7078/profession/workorder/saveWorkOrderInfo"
    resp = requests.post(url, data=params, headers=headers)
    #print(resp.text)# 接口返回文本信息

    # 把文本信息转化为字典格式
    text_dict = json.loads(resp.text)
    print(text_dict)

if __name__ == "__main__":
    #get_user_info()
    get_workid_info()
    #login()
