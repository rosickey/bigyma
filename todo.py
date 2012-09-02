#coding:utf-8
import web
import os
import sys
import model
import urllib2
from time import sleep
from datetime import datetime
#from weibopy.auth import OAuthHandler
#from weibopy.api import API
from weibo import APIClient,APIError
from web.contrib.template import render_mako

import time
import data_theme
import time_operate 
import rule
CONSUME_KEY= 
CONSUME_SECRET =
month_label = ['Jan','Feb','Mar','Apr','May',\
                'Jun' ,'Jul' ,'Aug' ,'Sep' ,'Oct',\
                'Nov' ,'Dec']
week_label = ['Sun' ,'Mon' ,'Tue' ,'Wed' ,'Thu' ,'Fri' ,'Sta' ,]
best_date= 0

web.config.debug = True
#日志对象

def initlog():
    import logging
    logger=logging.getLogger("sina_twitter")
    hd=logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s') 
    hd.setFormatter(fmt)
    logger.addHandler(hd)
    logger.setLevel(logging.DEBUG)
    return logger 


def store_test(name='',data=''):
    s = sae.storage.Client(accesskey=sae.const.ACCESS_KEY, secretkey=sae.const.SECRET_KEY, prefix=sae.const.APP_NAME)
    ob = sae.storage.Object(data)
    s.put('store',name+'.png',ob)
    #data = ob.data
    #data = 1
    #data = '121212121'
    return imgdata.len


logger=initlog()

 
#url映射配置
urls = (
        '/','FirstP',
        '/index','Index',
        '/callback','CallBack',
        '/logout','LogOut',
        '/updata','Updata',
)

app = web.application(urls, globals())
render = render_mako(
        directories=[os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )




store = web.session.DBStore(model.db, 'weibo_sessions')
session = web.session.Session(app, store, initializer={'isLogin':0,'userName':'',})
web.config._session = session

weibo_api = ''
#使用jinja2模板渲染文件

#首页
 #首先从session中获取access_token，没有就转向新浪微博页面认证
 #认证成功后将access_token保存在session中
class Index:

    def GET(self):

	global access_token
        access_token = session.get('access_token',None)
        global expires_in
        expires_in = session.get('expires_in',None)
        #access_token = 0
        if not access_token:
            client = APIClient(app_key=CONSUME_KEY, app_secret=CONSUME_SECRET, redirect_uri=web.ctx.get('homedomain')+'/callback')
            #auth = OAuthHandler(CONSUME_KEY, CONSUME_SECRET,web.ctx.get('homedomain')+'/callback')
            #获得新浪微博的认证url地址
            auth_url = client.get_authorize_url()
            #auth_url = auth.get_authorization_url()
            logger.debug("认证地址为：%s"%auth_url)
            #在session中保存request_token，用于在新浪微博认证通过后换取access_token
            
            #session.request_token=auth.request_token
            print '1111111111111111111111111111111111111'
            print auth_url
            global errr
            errr = 4321
            web.seeother(auth_url)
            
            
        else:

            #code = session.get('code')
            #return str(code)
            #client = APIClient(app_key=CONSUME_KEY, app_secret=CONSUME_SECRET, redirect_uri=web.ctx.get('homedomain')+'/callback')
            #auth_url = client.get_authorize_url()
            #auth = OAuthHandler(CONSUME_KEY, CONSUME_SECRET)
            #auth.access_token=access_token
            #r = client.request_access_token(code)
            #access_token = r.access_token
            #expires_in = r.expires_in
            #client.set_access_token(access_token, expires_in)
            
            #api=API(auth)

            #global weibo_api
            #weibo_api = api
            #user=api.verify_credentials()
            #client.get.account__get_uid()
            
            global client
            client = APIClient(app_key=CONSUME_KEY, app_secret=CONSUME_SECRET, redirect_uri=web.ctx.get('homedomain')+'/callback')
            #r = client.request_access_token(code)
            #access_token = r.access_token # 新浪返回的token，类似abc123xyz456
            #return str(access_token )
            #expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
            # TODO: 在此可保存access token
            client.set_access_token(access_token, expires_in)
            self.client = client
            
            #user = client.get.account_get_uid()
            #return user
            #user = ''
            #id = client.get.account__get_uid()
            #friends=api.friends()

            total = 200
            #sleep(1)

            #blogs = api.user_timeline(page=1,count = total,trim_user=1)
            blog = client.get.statuses__user_timeline(page=1,count = 1,trim_user=0).statuses
            user = blog[0]['user']['screen_name']
            index = blog[0]['user']['statuses_count']
            index = 300
            #return user,index
            blogs = client.get.statuses__user_timeline(page=1,count = total,trim_user=1).statuses

            #index =  user.statuses_count
            #return blogs
            #index = 2800
          
            #web.header("Content-Type", "text/html;charset=utf-8")
            #return ':-( 出错了wqwqwsdsdsdqqqqqqqq'
            #获取全部
            #print index
            
            mm = 21

            try:
                #blogs += api.user_timeline(page=2,count = total,trim_user=1)
                blogs += client.get.statuses__user_timeline(page=2,count = total,trim_user=1).statuses
            except:
                print 'nook 2'
                mm = 11
                
            
            for i in xrange(3,index/100 + 1):
                try:
                    sleep(0.001)
                    #blogs += api.user_timeline(page=i)
                    blogs += client.get.statuses__user_timeline(page=i,count = total,trim_user=1).statuses
                except:
                    print 'nook 3', i
                    #break
            
            time_data = []
            time_data_fzhuanf = []
            time_data_zhuanf = []
            test = "转发微"
            test2 = "//@"
            a = 0 
            for blog in blogs:
                #print blog.created_at.month
                #print blog.created_at.isocalendar()
                blog.created_at = time.strptime(str(blog.created_at),"%a %b %d  %H:%M:%S +0800 %Y")
                if (blog.text[:3].encode('utf8') == test) or (blog.text[:3].encode('utf8') == test2):
                    #print '11111111',blog.text[:3].encode('utf8')
                    a+=1
                  
                    time_data_zhuanf.append(blog.created_at)
                else:
                    #print blog.text[:3].encode('utf8')
                    time_data_fzhuanf.append(blog.created_at)
                
                time_data.append(blog.created_at)
            #print 'aaaaaaaaaaaaaaaa',a
            #return time_data,time_data_zhuanf,time_data_fzhuanf
            data_2012_M , data_2011_M, data_2012_W, data_2011_W,\
            data_zhuanf,data_fzhuanf ,data_f_total,data_H\
            =  time_operate.time_operate(time_data,time_data_zhuanf,time_data_fzhuanf)
            #return render_template('index.html',friends=friends,user=user)
            #print blogs
            #pic1 = chart.plot_bar(name = 'The Number of weibo in 2012',value=data_2012_M['value'],label=month_label)
            #pic2 = chart.plot_bar(name = 'The Number of weibo in 2012',value=data_2011_M['value'],label=month_label)
            #aa = test_line()
            #print pic1
            print time_data.__len__()
            web.header("Content-type","text/html")
            data_2012 =data_theme.op_year(data_2012_M['value'])
            data_2011 =data_theme.op_year(data_2011_M['value'])
            data_week_day = data_theme.op_week_day(data_2012_W,data_2011_W)
            data_zhuanf,data_fzhuanf,data_total = data_theme.op_zhuanf(data_zhuanf,data_fzhuanf,data_f_total)
            data_hour= data_theme.op_hour(data_H)
            #print '11111asasas',data_zhuanf,data_fzhuanf
            best_day,best_time = rule.rule(data_f_total,data_H)
            global best_date
            best_date = best_day
            global best_t
            best_t = best_time
            #return  best_date,best_time
            #return data_2012_M , data_2011_M, data_2012_W, data_2011_W,data_zhuanf,data_fzhuanf ,data_f_total,data_H
            return render.index2(quantity = "%.0f" % (time_data.__len__()*100.0/(index)),picname = '2012',label=month_label,value1=data_2012,\
                                    value2=data_2011,value3=data_week_day,\
                                    zhuanf=data_zhuanf,fzhuanf=data_fzhuanf,\
                                    combin=data_hour,f_total=data_total,\
                                    best_day=best_day,best_time=best_time,blogs=blogs, user=user)
#页面回调，新浪微博验证成功后会返回本页面
    def POST(self):
        data = web.input()
        
        web.header("Content-Type", "text/html;charset=utf-8")
        #access_token = session.get('access_token',None)
        #expires_in = session.get('expires_in',None)
        #return render.hello()
        #client = APIClient(app_key=CONSUME_KEY, app_secret=CONSUME_SECRET, redirect_uri=web.ctx.get('homedomain')+'/callback')
            #r = client.request_access_token(code)
            #access_token = r.access_token # 新浪返回的token，类似abc123xyz456
            #return str(access_token )
            #expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
            # TODO: 在此可保存access token
        #global client
        client.set_access_token(access_token, expires_in)
        import base64
	from PIL import Image
	import StringIO
        im = Image.open(StringIO.StringIO(base64.b64decode(data['img'][22:])))
        new_im = im.resize((800,267),Image.BILINEAR)
	imgdata = StringIO.StringIO()
	new_im.save(imgdata, 'PNG')
        imgdata.name = 's.png'
        url = '"http://bigyma.sinaapp.com"'

        try:
            client.upload.statuses__upload(status=u'我每月'+str(best_date)+u'号'+best_t+u'点量最少...！赶快通过围脖来看看自己的作息习惯吧'+str(url),pic=imgdata)
        
            return u'上传成功'
        except:
            return u'网速有影响，再上传一次'
        '''
        except APIError as apierr:
            #return(str(apierr))
            raise
    	except urllib2.HTTPError as err:
     
            #return(str(err)+str(err.read()))   # 记录HTTP状态码
            raise
        '''	
        #return client.post.statuses__update(status=u'lcek')
        
        #log = client.upload.statuses__upload(status=u'w测试一下',pic=imgdata)
	
        

class FirstP:
    def GET(self):
        web.header("Content-Type", "text/html;charset=utf-8")
        return render.hello()
    
class CallBack:
     def GET(self):
        try:
            ins=web.input()
   
            # 获取URL参数code:
            code = ins.get('code')

            client = APIClient(app_key=CONSUME_KEY, app_secret=CONSUME_SECRET,redirect_uri=web.ctx.get('homedomain')+'/callback')
            
            r = client.request_access_token(code)
            access_token = r.access_token # 新浪返回的token，类似abc123xyz456
            #return str(access_token )
            expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
            # TODO: 在此可保存access token
            client.set_access_token(access_token, expires_in)
            
            #oauth_verifier=ins.get('oauth_verifier',None)
            #request_token=session.get('request_token',None)
            #auth=OAuthHandler(CONSUME_KEY, CONSUME_SECRET)
            #auth.request_token=request_token
            #通过oauth_verifier来获取access_token
            #access_token=auth.get_access_token(oauth_verifier)
            session.access_token=access_token
            
            session.code = code
            session.expires_in = expires_in
            #return str(access_token)
            print '111111111111111111111'
            #user = client.get.users_show()
            #id = client.get.account__get_uid()
            #return str(expires_in)
            web.seeother("/index")
        except Exception:
            web.header("Content-Type", "text/html;charset=utf-8")
            return ':-( 出错了在这里222'+ str(code)
            
            
class Updata:
    def GET(self):
        fayan = '每月的'+str(best_date)+'号总有那么几天....～快来通过微博分析分析你的生活吧。http://bigyma.sinaapp.com/'
        weibo_api.upload('c:/2.png',fayan)
        web.header("Content-Type", "text/html;charset=utf-8")
        #web.header("Content-type","text/html")
        return render.hello()
 #退出微博，返回到首页    
class LogOut:
    def GET(self):
        session.kill()
        web.header("Content-Type", "text/html;charset=utf-8")
        return ':-( 推出楼'
def notfound():
    web.header("Content-Type", "text/html;charset=utf-8")
    return web.notfound("nooooooooooootfound,尝试刷新一下，F5")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

app.notfound = notfound

def internalerror():
    return web.internalerror("wait for a monment,sorry...or you can use F5")

app.internalerror =  web.debugerror

#app.internalerror =  internalerror
if __name__=='__main__':
    #logger.debug("web.py服务开始启动……")
    app.run()