from pyofc2  import * 
def pic_bar():      
    
    t = title(text='12121')
    l = line()
    l.values = [9,8,7,6,5,4,3,2,1]
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l)
    return chart