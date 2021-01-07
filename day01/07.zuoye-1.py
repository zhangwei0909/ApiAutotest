
import requests
'''
url= "http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":15929921116,"pwd":"123456","regname":""}
r=requests.post(url,data=cs)
# print(r.text)
assert r.json()['msg']=="注册成功"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":15929931103,"pwd":"123456","regname":"haha"}
r=requests.post(url,data=cs)
# print(r.text)
assert r.json()['msg']=="注册成功"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":15929941002,"pwd":"","regname":""}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="密码不能为空"


url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"","pwd":"123456","regname":""}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号不能为空"


url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"","pwd":"","regname":""}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号不能为空"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"15951111131","pwd":"","regname":"丫丫"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="密码不能为空"


url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"","pwd":"aaa58585","regname":"wawa"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号不能为空"


url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"15961112212","pwd":"aaa55"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="密码长度必须为6~18"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"15971112211","pwd":"abc"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="密码长度必须为6~18"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"15991112212","pwd":"aaaaaa1952154126415"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="密码长度必须为6~18"


url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"1","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']== "手机号码格式不正确"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"136485","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号码格式不正确"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"1234567890","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号码格式不正确"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"12345678941012","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号码格式不正确"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"11111111111","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号码格式不正确"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"15006007018","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="手机号码已被注册"


'''
url="http://jy001:8081/futureloan/mvc/api/member/login"
cs={"mobilephone":"15006007018","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="登录成功"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"15006007018","pwd":""}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="用户名或密码错误"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"","pwd":"abc1234"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="用户名或密码错误"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"","pwd":""}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="用户名或密码错误"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"18911111111","pwd":"123456"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="用户名或密码错误"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"189","pwd":"123456"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="用户名或密码错误"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"18922222222","pwd":"12345"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="用户名或密码错误"

url="http://jy001:8081/futureloan/mvc/api/member/register"
cs={"mobilephone":"18922222222","pwd":"111111"}
r=requests.post(url,data=cs)
print(r.text)
assert r.json()['msg']=="用户名或密码错误"
