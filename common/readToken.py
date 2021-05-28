# coding=utf-8 
"""
@Time    : 2021/04/25  下午 12:06
@Author  : hnm
@FileName: readToken.py
@IDE     : PyCharm
"""
from getRootPath import root_dir
import os

token_file = os.path.join(root_dir, "conf", "tokens")

def write_file(token):
	with open(token_file, "w") as fp:
		fp.write(token)

def read_token():
	with open(token_file) as fp:
		return eval(fp.readlines()[0])

if __name__ == "__main__":
	# print(read_token())  #返回一个字典,fp.readlines()返回一个列表
	print(read_token()["token"])


