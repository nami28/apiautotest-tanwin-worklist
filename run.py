
import time
import unittest
from BeautifulReport import BeautifulReport
from getRootPath import root_dir
import os


def run():
    test_dir = os.path.join(root_dir, "cases")
    reportPath = os.path.join(root_dir, "report")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='tes*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # print(now)   #2021-04-21 10_18_22
    reportName = now + '测试报告.html'
    description = "碳银系统接口自动化测试报告"
    BeautifulReport(discover).report(filename=reportName, description=description, log_path=reportPath)
    #print(discover)


if __name__ == "__main__":

    run()