'''
使用requests 做接口测试
'''

# 导入包
import requests

# 发送一个请求
r = requests.get("http://www.baidu.com")
print(r.text)  # 文本格式的
print(r.status_code)  # 响应状态码
print(r.raw)  # 无格式的响应

# 接口测试：构造不同的参数，发送请求，对响应的结果做断言
# 获取用户列表
# http://jy001:8081 测试环境
# futureloan/mvc/api/member/list  接口地址
url = "http://jy001:8081/futureloan/mvc/api/member/list"
r = requests.get(url)
print(r.text)
# 检查status_code ,响应码是不是200
assert r.status_code == 200
# 响应体是json格式的，取里面的code，检查是不是10001
assert r.json()['code'] == '10001'

# 发送的请求带参数
# 方式一：拼接到url后面
# 注册用户
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=18012345678&pwd=123456"
r = requests.get(url)
print(r.text)
assert r.status_code == 200
assert r.json()['code'] == '20110'
assert r.json()['msg'] == "手机号码已被注册"
assert r.json()['status'] == 0

url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=18012345&pwd=123456"
r = requests.get(url)
print(r.text)
assert r.status_code == 200
assert r.json()['code'] == '20109'

# 方法二：使用params传参
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 18012345678, "pwd": "12345", "regname": "requests"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 18011111113, "pwd": "", "regname": "requests"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "密码不能为空"

# 练习：淘宝查询手机号码归属地的接口.htm
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
# 参数tel：手机号码
data = {"tel": 15929911152, "regname": "requests"}
r = requests.get(url, params=data)
print(r.text)
assert "15929911152" in r.text

# 发送请求，设置请求头
# 测试的网站，不管发送什么请求，服务器把请求的内容封装成json格式的返回
# /get get方法，/post post方法
head = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

url = "http://www.httpbin.org.get"
r = requests.get(url, headers=head)
print(r.text)
