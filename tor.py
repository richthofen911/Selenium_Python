import tornado.ioloop
import tornado.web
import urllib2
import urllib
import re
import json


url_signup = "https://admin.firebase.com/account"
url_login = 'https://admin.firebase.com/account/login?email=yichaoli.richthofen%40gmail.com&password=qwer1234&rememberMe=true'
url_newapp = 'https://admin.firebase.com/firebase/apdqc'

def hit_url_params(url, params):
    request = urllib2.Request(url, params)
    res_page = urllib2.urlopen(request).read()
    return res_page

def hit_url_simple(url):
    res_page = urllib2.urlopen(url).read()	
    return res_page



class MainHandler(tornado.web.RequestHandler):
    def get(self):
       # self.write(self.get_argument('email'))
#        data = 
        params_signup = urllib.urlencode({'email': self.get_argument('email'), 'password': 'qwer1234', 'referrer': 'https://www.google.ca/'})
        res_signup = hit_url_params(url_signup, params_signup)
        print res_signup
#        self.write(res_signup)
#        self.write("Hello, world " + self.get_argument('email') + self.get_argument('name'))

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
