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
#import requests
from common.findReplace import findAndReplace
from common.dataBase import dataBase

@ddt
class test_查看工单详情(unittest.TestCase):
    yamlPath = ['4工单售后运维', '查看工单详情.yaml']
    yaml_path = os.path.join(root_dir, "yamlCase")
    for dir in yamlPath:
        yaml_path = os.path.join(yaml_path, dir)
    read_yaml = readYaml(yaml_path)
    case_list = read_yaml.caseList()
    db = dataBase(confParam("电站管理"))
    workId = db.getId("id", "work_order_info")
    case_list = eval(findAndReplace(str(case_list), {"workId": workId}))

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
        cls.headers = {"Authorization": read_token()["token"], "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_查看工单详情(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            data = caseInfo["data"]
            check = caseInfo["check"]
            self.__dict__['_testMethodDoc'] = caseName

        # 发送请求
        response = self.client.sendRequest(self.method, self.url, self.headers, data)
        #response = requests.post(self.url, params=data, headers=self.headers)
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
