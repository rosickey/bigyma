colors = ["#4572A7","#AA4643","#89A54E","#80699B","#3D96AE","#DB843D","#92A8CD","#A47D7C","#B5CA92"]
def op_year(value):
    n = 0
    color = 'color'
    y = 'y'
    data = []
    for i in value:
        data.append({y:value[n],color:colors[n%9]})
        n+=1
    return data
def op_week_day(dic1,dic2):
    data = []
    label = ["Sun","Mon","Tue","Wed","Thur","Fri","Sat"]
    for i in range(6):
        #dic1['value'][i] += dic2['value'][i]
        data.append([label[i],(dic1['value'][i]+dic2['value'][i])])
    data.append({'name':label[6],'y':(dic1['value'][6]+dic2['value'][6]),'sliced': 'true','selected': 'true'})
    return data

def op_zhuanf(zhuanf,fzhuanf,f_total):
    data1 = []
    data2 = []
    data = []
    for i in range(31):
        data1.append([zhuanf['label'][i],zhuanf['value'][i]])
        data2.append([fzhuanf['label'][i],fzhuanf['value'][i]])
        data.append([f_total['label'][i],f_total['value'][i]])
    #print 'zhuanfsssssssssssssssss',zhuanf
    #print 'zhuanfsssssssssssssssss',fzhuanf
    return data1,data2,data
    
def op_hour(dic):
    series = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    for i in range(6):
        data1.append(dic['value'][i*4])
        data2.append(dic['value'][i*4+1])
        data3.append(dic['value'][i*4+2])
        data4.append(dic['value'][i*4+3])
    for i in range(6):
        data5.append((data1[i]+data2[i]+data3[i]+data4[i])/4)
    data6.append({'name':'00:00~07:59','y':(data5[0]+data5[1])*4,'color':'#2E2C29'})
    data6.append({'name':'08:00~15:59','y':(data5[2]+data5[3])*4,'color':'#AA4643'})
    data6.append({'name':'16:00~23:59','y':(data5[4]+data5[5])*4,'color':"#4572A7"})
    series.append({'type':'column','name':'00:00~07:59','data':data1})
    series.append({'type':'column','name':'08:00~13:59','data':data2})
    series.append({'type':'column','name':'08:00~13:59','data':data3})
    series.append({'type':'column','name':'08:00~23:59','data':data4})
    series.append({'type':'spline','name':'Average','data':data5})
    series.append({'type':'pie','name':'Total','data':data6})
    series.append({'center':[100,80]})
    series.append({'size':100})
    series.append({'showInLegend':'false'})
    series.append({'dataLabels':{'enabled':'false'}})
    return [data1,data2,data3,data4,data5,data6]
    
    
    