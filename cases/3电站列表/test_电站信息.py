# coding=utf-8 

from ddt import ddt, data
import unittest
import json
from common.findReplace import findAndReplace
from common.check import Check
from common.readConfig import confParam
from common.readToken import read_token
from common.readYaml import readYaml
from getRootPath import root_dir
from common.writeLog import writeLog
import os
from common.sendRequest import sendRequest
import requests

@ddt
class test_电站信息(unittest.TestCase):
    yamlPath = ['3电站列表', '电站信息.yaml']
    yaml_path = os.path.join(root_dir, "yamlCase")
    for dir in yamlPath:
        yaml_path = os.path.join(yaml_path, dir)
    read_yaml = readYaml(yaml_path)
    case_list = read_yaml.caseList()
    case_list = eval(findAndReplace(str(case_list), {"stationId": confParam("stationId")}))

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
        cls.headers = {"token": read_token()["token"], "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                       "userInfo":"%7B%22userId%22:17,%22username%22:%22ty_2103121830001%22,%22avatar%22:%22http://photo.tanwin.cn/tempfile/2021-05-14/d92c640ff4affd5989e3cc6612e8507f.jpg%22,%22nickname%22:%22%E8%83%A1%E6%B0%B8%E6%81%92%22,%22realName%22:%22%E8%83%A1%E6%B0%B8%E6%81%92%22,%22authStatus%22:9,%22phone%22:%2217316918814%22,%22email%22:null,%22gender%22:2,%22birthday%22:%221950-01-01%22,%22isSingleLogin%22:false,%22platform%22:%22TW_ADMIN%22,%22appPlatforms%22:%5B%5D,%22nowOrg%22:%7B%22companyName%22:%22%E6%B5%99%E6%B1%9F%E7%A2%B3%E9%93%B6%E4%BA%92%E8%81%94%E7%BD%91%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22,%22companyOrgId%22:2,%22deptName%22:%22%E5%B7%A5%E7%A8%8B%E9%83%A8%22,%22deptOrgId%22:25,%22positionName%22:%22%E5%B7%A5%E7%A8%8B%E5%AE%A1%E6%A0%B8%22,%22positionId%22:6,%22busiType%22:%5B%5D%7D,%22positions%22:%5B6%5D,%22positionAreas%22:%7B%22businessAreas%22:%5B%22370000%22,%22620000%22,%22320000%22,%22110000%22,%22530000%22,%22460000%22,%22330000%22,%22310000%22,%22120000%22,%22610000%22,%22650000%22,%22520000%22,%22340000%22,%22430000%22,%22130000%22,%22210000%22,%22510000%22,%22640000%22,%22220000%22,%22350000%22,%22420000%22,%22440000%22,%22500000%22,%22140000%22,%22360000%22,%22230000%22,%22630000%22,%22410000%22,%22150000%22,%22540000%22,%22450000%22%5D,%22installAreas%22:%5B%22370000%22,%22620000%22,%22320000%22,%22110000%22,%22530000%22,%22460000%22,%22330000%22,%22310000%22,%22120000%22,%22610000%22,%22650000%22,%22520000%22,%22340000%22,%22430000%22,%22130000%22,%22210000%22,%22510000%22,%22640000%22,%22220000%22,%22350000%22,%22420000%22,%22440000%22,%22500000%22,%22140000%22,%22360000%22,%22230000%22,%22630000%22,%22410000%22,%22150000%22,%22540000%22,%22450000%22%5D,%22operationAreas%22:%5B%22370000%22,%22620000%22,%22320000%22,%22110000%22,%22530000%22,%22460000%22,%22330000%22,%22310000%22,%22120000%22,%22610000%22,%22650000%22,%22520000%22,%22340000%22,%22430000%22,%22130000%22,%22210000%22,%22510000%22,%22640000%22,%22220000%22,%22350000%22,%22420000%22,%22440000%22,%22500000%22,%22140000%22,%22360000%22,%22230000%22,%22630000%22,%22410000%22,%22150000%22,%22540000%22,%22450000%22%5D%7D,%22readPositions%22:%5B%5D,%22roles%22:%5B%22tanwin_role%22%5D,%22companyRoles%22:%5B%22TY0000001%22,%22TY0000007%22,%22TY0000029%22,%22TY0000030%22%5D,%22permits%22:null,%22flows%22:%5B%7B%22flowId%22:%22BANKING_LOAN_HYZLLC%22,%22nodes%22:%5B%22_SORT100110_%22,%22_SORT100130_%22,%22_SORT100160_%22,%22_SORT100210_%22,%22_SORT100220_%22,%22_SORT100240_%22,%22_SORT100250_%22,%22_SORT100260_%22,%22_SORT100275_%22,%22_SORT100350_%22,%22_SORT100410_%22,%22_SORT100420_%22,%22_SORT100430_%22,%22_SORT100510_%22,%22_SORT100135_%22,%22_SORT100140_%22,%22_SORT100215_%22,%22_SORT100270_%22,%22_SORT100280_%22,%22_SORT100520_%22,%22_SORT100535_%22,%22_SORT100540_%22,%22_SORT100560_%22,%22_SORT100570_%22,%22_SORT100360_%22%5D,%22forms%22:%5B%22_141_0_%22,%22_141_1_%22,%22_143_0_%22,%22_143_1_%22,%22_144_0_%22,%22_144_101_%22,%22_145_0_%22,%22_147_0_%22,%22_150_0_%22,%22_153_0_%22,%22_153_101_%22,%22_154_0_%22,%22_154_101_%22,%22_154_1_%22,%22_155_0_%22,%22_155_101_%22,%22_156_0_%22,%22_157_0_%22,%22_157_101_%22,%22_159_0_%22,%22_160_0_%22,%22_161_0_%22,%22_162_0_%22,%22_162_101_%22,%22_163_0_%22,%22_163_101_%22,%22_163_102_%22,%22_165_0_%22,%22_165_1_%22,%22_166_0_%22,%22_166_101_%22,%22_170_0_%22,%22_171_0_%22%5D%7D,%7B%22flowId%22:%22JOIN_YUNWEIGDTY%22,%22nodes%22:%5B%22_SORT100100_%22,%22_SORT100200_%22,%22_SORT100300_%22%5D,%22forms%22:%5B%22_181_0_%22,%22_182_0_%22,%22_183_0_%22%5D%7D,%7B%22flowId%22:%22EXAMINE_XIANGMU%22,%22nodes%22:%5B%22_SORT100160_%22%5D,%22forms%22:%5B%22_206_0_%22,%22_206_101_%22%5D%7D,%7B%22flowId%22:%22JOIN_YUNXINGSHTY%22,%22nodes%22:%5B%22_SORT100100_%22,%22_SORT100200_%22%5D,%22forms%22:%5B%22_184_0_%22,%22_186_0_%22,%22_186_101_%22%5D%7D,%7B%22flowId%22:%22BANKING_LOAN_GHFQLC%22,%22nodes%22:%5B%22_SORT100110_%22,%22_SORT100130_%22,%22_SORT100170_%22,%22_SORT100210_%22,%22_SORT100220_%22,%22_SORT100240_%22,%22_SORT100250_%22,%22_SORT100260_%22,%22_SORT100275_%22,%22_SORT100315_%22,%22_SORT100320_%22,%22_SORT100410_%22,%22_SORT100420_%22,%22_SORT100430_%22,%22_SORT100510_%22,%22_SORT101011_%22,%22_SORT101031_%22,%22_SORT101041_%22,%22_SORT100140_%22,%22_SORT100270_%22,%22_SORT100280_%22,%22_SORT100310_%22,%22_SORT100330_%22,%22_SORT100360_%22,%22_SORT100520_%22,%22_SORT100530_%22,%22_SORT100540_%22,%22_SORT101042_%22%5D,%22forms%22:%5B%22_101_0_%22,%22_101_1_%22,%22_103_0_%22,%22_103_1_%22,%22_104_0_%22,%22_104_1_%22,%22_107_0_%22,%22_107_101_%22,%22_107_102_%22,%22_107_103_%22,%22_110_0_%22,%22_112_0_%22,%22_112_1_%22,%22_113_0_%22,%22_113_1_%22,%22_114_0_%22,%22_114_1_%22,%22_115_0_%22,%22_115_101_%22,%22_116_0_%22,%22_116_101_%22,%22_116_102_%22,%22_116_103_%22,%22_117_0_%22,%22_117_101_%22,%22_118_0_%22,%22_119_0_%22,%22_119_101_%22,%22_121_0_%22,%22_122_0_%22,%22_123_0_%22,%22_123_101_%22,%22_123_1_%22,%22_124_0_%22,%22_124_101_%22,%22_124_102_%22,%22_126_0_%22,%22_126_1_%22,%22_127_0_%22,%22_127_101_%22,%22_128_0_%22,%22_129_0_%22,%22_131_0_%22,%22_131_1_%22,%22_132_0_%22%5D%7D%5D%7D",
                       "Host":"preuserauth.tanwin.cn:7078","Origin":"http://preflow.tanwin.cn","Referer": "http://preflow.tanwin.cn/","Accept": "application/json, text/plain,*/*",
                       "Authorization":read_token()["token"]
                       }

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_电站信息(self, cases):

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
