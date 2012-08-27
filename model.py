import web
import sae.const
db = web.database(dbn='mysql',host='w.rdc.sae.sina.com.cn',port=int(sae.const.MYSQL_PORT),db='app_bigyma',user=sae.const.MYSQL_USER,pw=sae.const.MYSQL_PASS)
#db = web.database(dbn='mysql',db='rosickey',user='root',pw='rosickey')


def get_todos():
    return db.select('todo',order='id')
    
def new_todo(text):
    db.insert('todo',title=text)
    
def del_todo(id):
    db.delete('todo',where="id=$id",vars=locals())
    
def new_user(text,text2):
    try:
        db.insert('nc_userdb',mail=text,password=text2)
    except:
        db.delete('nc_userdb',where="mail=$text",vars=locals())
        db.insert('nc_userdb',mail=text,password=text2)

def get_user(text):
    return list(db.select('nc_userdb',what='mail,password',where="mail=$text",vars=locals()))
#    return db.select('userdb',what='mail,password',where="mail=$text",vars=locals())