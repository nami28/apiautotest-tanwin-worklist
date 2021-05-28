# coding=utf-8 

from ddt import ddt, data
import unittest
import json
from common.check import Check
from common.readConfig import confParam
from common.readToken import read_token
from common.readYaml import readYaml
from getRootPath import root_dir
from common.writeLog import writeLog
import os
from common.sendRequest import sendRequest
import requests
#from common.findReplace import findAndReplace
from common.do_regex import DoRegex
from common.dataBase import dataBase

@ddt
class test_修改逆变器信息(unittest.TestCase):
    yamlPath = ['3电站列表', '修改逆变器信息.yaml']
    yaml_path = os.path.join(root_dir, "yamlCase")
    for dir in yamlPath:
        yaml_path = os.path.join(yaml_path, dir)
    read_yaml = readYaml(yaml_path)
    case_list = read_yaml.caseList()
    #print(case_list)
    #case_list = eval(findAndReplace(str(case_list), {"stationId": confParam("stationId")}))
    case_list = eval(DoRegex.do_regex(str(case_list)))
    id = dataBase(confParam("电站管理")).getId("id", "station_inverter_info")
    case_list[2]["修改逆变器信息"]["data"]["id"]=id
    #case_list[2]["修改逆变器信息"]["data"]["sn"] = case_list[2]["修改逆变器信息"]["data"]["sn"]+"a"

    #case_list[2]["修改逆变器信息"]["data"]["deviceName"] = case_list[2]["修改逆变器信息"]["data"]["deviceName"] + "b"
    method = case_list[0]["method"]
    url = case_list[1]["url"]

    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # 拼接接口地址
        cls.url = confParam("hostName") + cls.url
        cls.client = sendRequest()

        # 请求信息头
        cls.headers = {"Authorization": read_token()["token"], "Content-Type": "application/json;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_修改逆变器信息(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            data = caseInfo["data"]
            check = caseInfo["check"]
            self.__dict__['_testMethodDoc'] = caseName

        # 发送请求
        #response = self.client.sendRequest(self.method, self.url, self.headers, data)
        response = requests.post(self.url, params=data, headers=self.headers)
        # 接口返回文本信息
        text = response.text

        # 把文本信息转化为字典格式
        text_dict = json.loads(text)

        # 写日志
        writeLog(caseName, self.url, data, check, text_dict)

        # 断言
        Check().check(check, text_dict)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
