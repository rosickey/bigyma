#coding:utf-8
def rule(day,time):
    print 'dayyyyyyyyyyyyyyy',time
    a= []
    for i in range(31):
        a.append(day['value'][i]+day['value'][i-1]+day['value'][i-2]+day['value'][i-3]+day['value'][(i+3)%31]+day['value'][(i+2)%31]+day['value'][(i+1)%31])
    c = time['value'][:].index(min(time['value'][:]))
    if  c>=0 and c< 5:
        b = u'凌晨'
    if  c>=5 and c< 12:
        b = u'上午'
    if c >12 and c<19:
        b = u'下午'
    if c >19:
        b = u'晚上'
    return a.index(min(a)),b+str(c)
    