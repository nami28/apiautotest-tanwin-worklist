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
from common.findReplace import findAndReplace
from common.dataBase import dataBase
from common.get_data import GetData

@ddt
class test_9接单(unittest.TestCase):
    yamlPath = ['4工单售后运维', '8接单.yaml']
    yaml_path = os.path.join(root_dir, "yamlCase")
    for dir in yamlPath:
        yaml_path = os.path.join(yaml_path, dir)
    read_yaml = readYaml(yaml_path)
    case_list = read_yaml.caseList()
    db = dataBase(confParam("电站管理"))
    taskId = db.getworkId("task_id", "work_order_flow")
    taskId = str(int(taskId)+31)
    setattr(GetData, 'taskId', taskId)
    case_list = eval(findAndReplace(str(case_list), {"taskId": taskId}))

    method = case_list[0]["method"]
    url = case_list[1]["url"]

    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # 拼接接口地址
        cls.url = "http://preflowengine.tanwin.cn:8335" + cls.url
        cls.client = sendRequest()

        # 请求信息头
        cls.headers = {"Authorization": read_token()["token"], "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8","userInfo":"%7B%22userId%22:12581,%22username%22:%22ty_2104141054001%22,%22avatar%22:null,%22nickname%22:%22%E9%BB%84%E5%A8%9C%E6%A2%85%22,%22realName%22:%22%E9%BB%84%E5%A8%9C%E6%A2%85%22,%22authStatus%22:9,%22phone%22:%2213185086800%22,%22email%22:null,%22gender%22:null,%22birthday%22:null,%22isSingleLogin%22:false,%22platform%22:%22TW_ADMIN%22,%22appPlatforms%22:%5B%5D,%22nowOrg%22:%7B%22companyName%22:%22%E6%A1%90%E5%BA%90%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A%22,%22companyOrgId%22:1705,%22deptName%22:%22%E5%B8%82%E5%9C%BA%E9%83%A8%22,%22deptOrgId%22:131,%22positionName%22:%22%E4%B8%9A%E5%8A%A1%E7%BB%8F%E7%90%86%22,%22positionId%22:140,%22busiType%22:%5B1,2,4%5D%7D,%22positions%22:%5B140%5D,%22positionAreas%22:%7B%22businessAreas%22:%5B%22120102%22,%22110101%22,%22330109%22,%22130102%22,%22340122%22,%22410122%22,%22330122%22,%22350102%22%5D,%22installAreas%22:%5B%22330122%22%5D,%22operationAreas%22:%5B%22110101%22,%22330122%22%5D%7D,%22readPositions%22:%5B%5D,%22roles%22:%5B%22tanwin_role%22%5D,%22companyRoles%22:%5B%22TY0000001%22,%22TY0000020%22,%22TY0000029%22%5D,%22permits%22:null,%22flows%22:%5B%7B%22flowId%22:%22BANKING_LOAN_HYZLLC%22,%22nodes%22:%5B%22_SORT100110_%22,%22_SORT100130_%22,%22_SORT100160_%22,%22_SORT100210_%22,%22_SORT100220_%22,%22_SORT100240_%22,%22_SORT100250_%22,%22_SORT100260_%22,%22_SORT100275_%22,%22_SORT100350_%22,%22_SORT100410_%22,%22_SORT100420_%22,%22_SORT100430_%22,%22_SORT100510_%22%5D,%22forms%22:%5B%22_141_0_%22,%22_141_1_%22,%22_143_0_%22,%22_143_1_%22,%22_147_0_%22,%22_150_0_%22,%22_153_0_%22,%22_153_101_%22,%22_154_0_%22,%22_154_101_%22,%22_154_1_%22,%22_156_0_%22,%22_159_0_%22,%22_161_0_%22,%22_162_0_%22,%22_162_101_%22,%22_163_0_%22,%22_163_101_%22,%22_163_102_%22,%22_165_0_%22,%22_165_1_%22%5D%7D,%7B%22flowId%22:%22JOIN_YUNWEIGDTY%22,%22nodes%22:%5B%22_SORT100100_%22,%22_SORT100200_%22,%22_SORT100300_%22%5D,%22forms%22:%5B%22_181_0_%22,%22_182_0_%22,%22_183_0_%22%5D%7D,%7B%22flowId%22:%22EXAMINE_XIANGMU%22,%22nodes%22:%5B%22_SORT100160_%22%5D,%22forms%22:%5B%22_206_0_%22,%22_206_101_%22%5D%7D,%7B%22flowId%22:%22JOIN_YUNXINGSHTY%22,%22nodes%22:%5B%22_SORT100100_%22,%22_SORT100200_%22%5D,%22forms%22:%5B%22_184_0_%22,%22_186_0_%22,%22_186_101_%22%5D%7D,%7B%22flowId%22:%22JOIN_YEWUTY%22,%22nodes%22:%5B%22_SORT100110_%22,%22_SORT100120_%22,%22_SORT100130_%22,%22_SORT100140_%22%5D,%22forms%22:%5B%22_86_0_%22,%22_86_1_%22,%22_87_0_%22,%22_87_101_%22,%22_88_0_%22,%22_89_0_%22%5D%7D,%7B%22flowId%22:%22BANKING_LOAN_GHFQLC%22,%22nodes%22:%5B%22_SORT100110_%22,%22_SORT100130_%22,%22_SORT100160_%22,%22_SORT100170_%22,%22_SORT100210_%22,%22_SORT100220_%22,%22_SORT100240_%22,%22_SORT100250_%22,%22_SORT100260_%22,%22_SORT100275_%22,%22_SORT100320_%22,%22_SORT100350_%22,%22_SORT100410_%22,%22_SORT100420_%22,%22_SORT100430_%22,%22_SORT100510_%22,%22_SORT101011_%22,%22_SORT101031_%22,%22_SORT101041_%22%5D,%22forms%22:%5B%22_101_0_%22,%22_101_1_%22,%22_103_0_%22,%22_103_1_%22,%22_106_0_%22,%22_107_0_%22,%22_107_101_%22,%22_107_102_%22,%22_107_103_%22,%22_110_0_%22,%22_112_0_%22,%22_112_1_%22,%22_113_0_%22,%22_113_1_%22,%22_114_0_%22,%22_114_1_%22,%22_118_0_%22,%22_120_0_%22,%22_122_0_%22,%22_123_0_%22,%22_123_101_%22,%22_123_1_%22,%22_124_0_%22,%22_124_101_%22,%22_124_102_%22,%22_126_0_%22,%22_126_1_%22,%22_131_0_%22,%22_131_1_%22,%22_132_0_%22%5D%7D%5D%7D"}

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_9接单(self, cases):

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
