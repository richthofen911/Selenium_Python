#!/usr/bin/python

import urllib2
import urllib
import re
import json
import math
import subprocess

def hit_url_data(url, data):
		request = urllib2.Request(url, data)
		res_page = urllib2.urlopen(request).read()
		return res_page

def hit_url_simple(url):
		res_page = urllib2.urlopen(url).read()	
		return res_page

url1 = "http://54.149.146.72/auth.php"
url2 = "http://54.149.146.72/index.php"
url3 = "http://54.149.146.72/inout.php"
url4 = "http://www.google.ca"
url_login = 'https://admin.firebase.com/account/login?email=yichaoli.richthofen%40gmail.com&password=qwer1234&rememberMe=true'
url_newapp = 'https://admin.firebase.com/firebase/apqde'
#login_values = {'macaddress': 'aa:bb:cc:dd:ee:ff', 'presence': 'in'}


login_data2 = urllib.urlencode(login_values2)

#data = json.loads(hit_url_simple(per3hrs_url))
#temp_now = int(math.floor(weather[0]['main']['temp']- 273.15))

data = json.loads(hit_url_simple(url_login))
token = data['adminToken']

newapp_values = {'token': token, 'appName': 'apdqc'}
newapp_data = urllib.urlencode(newapp_values)


#print hit_url_data(url_newapp, login_data2)

'''
output = open('log', 'w')
output.write(source_code)
output.close()S
'''

