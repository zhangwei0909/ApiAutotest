'''
注册的测试脚本
'''
# 注册失败的测试脚本



# pytest数据驱动的方式
# 从yaml中读取测试数据
import pytest

from zonghe.baw import Member, Db
from zonghe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param


def test_register_fail(url,baserequests,fail_data):
    # 下发注册的请求
    r =Member.register(url,baserequests,fail_data['data'])
    # 断言结果
    print(r.text)
    assert r.json()['code']==fail_data['expect']['code']
    assert r.json()['msg']==fail_data['expect']['msg']
    assert r.json()['status']==fail_data['expect']['status']

# 把注册成功的数据写到register_pass.yaml
# 注册成功的脚本，下发请求，断言响应的结果
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
def pass_data(request):
    return request.param

def repeat_data(request):
    return request.param

def test_refister_class(url,baserequests,pass_data,db):
    mobilephone=pass_data['data']['mobilephone']
    Db.delete_user(db,mobilephone)
    r=Member.register(url,baserequests,pass_data['data'])
    print(r.text)
    assert str(r.json()['code'])==str(pass_data['expect']['code'])
    assert str(r.json()['msg']==str(pass_data['expect']['msg']))
    assert str(r.json()['status']==str(pass_data['expect']['status']))
    r=Member.list(url,baserequests)
    assert str(mobilephone) in r.text
    Db.delete_user(db,mobilephone)

def test_register_repeat(url,baserequests,repeat_data,db):
    mobilephone=repeat_data['data']['mobilephone']
    Db.delete_user(db,mobilephone)
    Member.register(url,baserequests,repeat_data['data'])
    r=Member.register(url,baserequests,repeat_data['data'])
    assert str(r.json()['code'])==str(pass_data['expect']['code'])
    assert str(r.json()['msg']==str(pass_data['expect']['msg']))
    assert str(r.json()['status']==str(pass_data['expect']['status']))
    Db.delete_user(db,mobilephone)