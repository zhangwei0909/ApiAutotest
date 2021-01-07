'''
脚本层的一些公共方法
'''
import pytest

from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests

env_path=r"data_env.ini"

# 读取env.ini中的url，设置session级别的，整个执行过程读一次
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path,"url")

@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path,"db"))

# 创建一个BaseRequests的实例，设置session级别，整个执行过程只有一个实例，自动管理Cookie
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()