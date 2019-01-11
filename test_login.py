#缺库函数的用， pip install requests/lxml 安装即可,base64自带的
import requests
import base64
from lxml import etree
#信息门户的账号密码
username = ''
password = ''

r = requests.Session()
url = 'http://id.ouc.edu.cn:8071/sso/login?service=http%3A%2F%2Fmy.ouc.edu.cn%2Fuser%2FsimpleSSOLogin'
h=r.get(url)

cookies = {'JSESSIONID':h.headers['Set-Cookie'][11:43],'SSOcookUser':username,'SSOcookPass':password,'SSOremember':'1','nginx':'978b14d6155abcfe50b14ae230300a04'}
payload={'username':username,'password':(str(base64.b64encode(bytes(password,'ascii')))[2:-1]),'lt':'e1s1','_eventId':'submit'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
h=r.post(url,params=payload,allow_redirects=False,cookies=cookies,headers=headers)

h=r.get(h.headers['Location'])
h=r.get('http://my.ouc.edu.cn/web/guest')
headers={'Upgrade-Insecure-Requests': '1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

h=r.get('http://graduate.ouc.edu.cn/ssoLogin.do',headers=headers,allow_redirects=True)
h=r.get('http://graduate.ouc.edu.cn/studentscore/queryScore.do?groupId=&moduleId=25011')
#print(h.text)
express_course_name = '/html/body/div/div[2]/table/tbody//tr/td[2]/text()'
express_course_score = '/html/body/div/div[2]/table/tbody//tr/td[7]/text()'
temp1 = etree.HTML(h.content).xpath(express_course_name)
temp2 = etree.HTML(h.content).xpath(express_course_score)
dic={}
for i,j in zip(temp1,temp2):
	i=i.replace("\xa0",'')
	j=j.replace("\n",'')
	j=j.replace(" ",'')
	dic[i]=j

for key,value in dic.items():
	print(key,value)


