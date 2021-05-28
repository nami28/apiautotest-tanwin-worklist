import re
from common.readConfig import confParam
from common.get_data import GetData
from common.dataBase import dataBase
class DoRegex:
    @staticmethod
    def do_regex(s):

        while re.search('\$\{(.*?)\}',s):   # $ {} 前面加\表示这个不是正则表达式符号
            key= re.search('\$\{(.*?)\}',s).group(0)  # ${normal_tel}
            value = re.search('\$\{(.*?)\}',s).group(1)  # normal_tel   前面正则表达式有括号，只有一个分组
            # s = s.replace(key,confParam(value)) #注意注意注意  这里一定是赋值给s
            s = s.replace(key, str(getattr(GetData,value)))
            #print(key, value)
            #print(s)
        return  s

if __name__ == '__main__':
    #s = '{"account": "${account}","password": "${password}", "platform": "1"}'  # 目标字符串
    s = '{"stationId": "${stationId}","supplier":"12","deviceName":"GW25KT-DT","sn":"4025KDTT20BG1706","id":${id}}'
    s = DoRegex.do_regex(s)
    print(s)
    db = dataBase(confParam("电站管理"))
    workId = db.getId("id", "work_order_info")
    workNo = db.getprojectId("work_no", "work_order_info")
    setattr(GetData, 'workId', workId)
    setattr(GetData, 'workNo', workNo)
    s='{"workId":${workId}, "workNo":${workNo}, "serviceRank": 2, "timeRank": 2}'
    s = DoRegex.do_regex(s)
    print(s)
