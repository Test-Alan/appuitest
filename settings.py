import os
import sys
# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "page"))
# 报告目录
REPORT_DIR = os.path.join(BASE_DIR, "report")

# appcaps配置目录
CAPS_DIR = os.path.join(BASE_DIR, "capabilities/caps.yaml")

# 失败重跑次数
rerun = "0"

# 运行测试用例的目录或文件
cases_path = "./testcase/"

