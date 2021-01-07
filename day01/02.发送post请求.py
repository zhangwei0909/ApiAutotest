'''
post请求
'''
import requests

url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": 18012345678, "pwd": "123456"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "登录成功"

# 发送post请求，json类型的参数，使用json传参
url = "http://www.httpbin.org/post"
cs = {"username": "1231231", "pwd": "123123123", "email": "324324@qq.com"}
r = requests.post(url, json=cs)
print(r.text)
assert r.json()['json']['username'] == "1231231"
# assert r.json()['headers']['User-Agent']=="python-requests/2.25.0"

# 发送post请求，带请求头
head = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

r = requests.post(url, json=cs, headers=head)
print(r.text)
