import requests

url = "http://www.testingedu.com.cn:8000/index.php"
# params的参数信息
querystring = {"m":"Home","c":"User","a":"do_login","t":"0.10799091400187022"}
# body体的参数信息
payload = "username=13800138006&password=123456&verify_code=1"
# headers的参数信息
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "0ce0234d-4b8e-42d6-93f5-c657171127fa"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)