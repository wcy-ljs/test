import pytest
import os
# 执行pytest命令  生成测试报告

# 执行测试用例
pytest.main(['--alluredir=./report'])

# 生成测试报告
os.system('allure generate ./report -o ./allure-report --clean')