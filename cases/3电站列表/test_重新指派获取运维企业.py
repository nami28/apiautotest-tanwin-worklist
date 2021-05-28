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

@ddt
class test_重新指派获取运维企业(unittest.TestCase):
    yamlPath = ['3电站列表', '重新指派获取运维企业.yaml']
    yaml_path = os.path.join(root_dir, "yamlCase")
    for dir in yamlPath:
        yaml_path = os.path.join(yaml_path, dir)
    read_yaml = readYaml(yaml_path)
    case_list = read_yaml.caseList()
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
    def test_重新指派获取运维企业(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            data = caseInfo["data"]
            check = caseInfo["check"]
            self.__dict__['_testMethodDoc'] = caseName

        # 发送请求
        response = self.client.sendRequest(self.method, self.url, self.headers, data)
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
