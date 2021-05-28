# coding=utf-8 
"""
@Time    : 2020/05/28  下午 1:38
@Author  : hnm
@FileName: readYaml.py
@IDE     : PyCharm
"""
#下载yaml，pip3 install pyyaml

import yaml
import os
from getRootPath import root_dir
from common.findReplace import findAndReplace
from common.readConfig import confParam
from common.do_regex import DoRegex

class readYaml:
    def __init__(self, yamlPath):
        self.yamlPath = yamlPath

    def caseList(self):
        with open(self.yamlPath, 'r', encoding='utf-8') as fp:
            contents = fp.read()
            testCase_dict = yaml.safe_load(contents)
            # print(type(testCase_dict))
            # print(testCase_dict)
            # print(testCase_dict.items())
            case_list=[]
            for caseName, caseInfo in testCase_dict.items():
                new_dict = {}
                new_dict[caseName] = caseInfo
                case_list.append(new_dict)
            return case_list


if __name__ == "__main__":
    yamlPath = os.path.join(root_dir, "yamlCase", "3电站列表", "修改逆变器信息.yaml")
    print(type(yamlPath))
    print(yamlPath)
    read_yaml = readYaml(yamlPath)
    case_list = read_yaml.caseList()
    print(case_list)
    #num = 0
    #print(confParam("login"))
    #case_list = eval(findAndReplace(str(case_list), {"login": confParam("login")}))
    case_list = eval(DoRegex.do_regex(str(case_list)))
    #for i in case_list[2:]:
    #    num +=1
   #     print(i)
   # print("共%d条用例" % num)
    #print(case_list)
    #print(case_list[0])
   # print(case_list[2]["修改逆变器信息"]["data"]["id"])







