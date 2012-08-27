#coding:utf-8
from pyofc2  import * 
def plot_bar(name = '',value = [],label = []):

    print label
    t = title(text=name)
    b = bar()
    x = x_axis()
    x.labels = labels(labels=label)
    b.values = value#
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(b)
    chart.x_axis = x
    return chart

    '''
    t = title(text='12121')
    l = line()
    l.values = [9,8,7,6,5,4,3,2,1]
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l)
    return chart
    '''