import os

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "Logs")
# 报告目录
REPORT_DIR = os.path.join(BASE_DIR, "Reports")

# appcaps配置目录
CAPS_DIR = os.path.join(BASE_DIR, "Capabilities/caps.yaml")

# 失败重跑次数
rerun = "0"

# 运行测试用例的目录或文件
cases_path = "TestCase/"

