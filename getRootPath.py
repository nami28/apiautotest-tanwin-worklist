# coding=utf-8 

import os

root_dir = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    # print(root_dir)  #C:\tanwinjob\interface test\testyaml
    yaml_path = os.path.join(root_dir, "yamlCase", "1登录", "1登录.yaml")
    print(yaml_path)