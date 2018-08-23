#-*- coding: utf-8 -*-

def my_rnpd(year):
    if (year%4==0 and year%100!=0)or year%400==0:
        return true
    else:
        return false
    
def yearnum(year):
    numyear=0
    while year>0:
        year=year-1
        if my_rnpd(year):
            numyear=numyear+1
        numyear=numyear+365
    return numyear

def mdnum(month):
    mtuple=(31,28,31,30,31,30,31,31,30,31,30,31)    #每个月的天数
    nummonth=0
    if month>1:
        for x in list(range(month-1))
            nummonth=nummonth+mtuple[x]
    return nummonth
                
def daysnum(year,month,days):    
    if my_rnpd(year):
        if month>2:
            days=days+1
    return days

y1,m1,d1=input('请输入第一个日期：').strip().split()
y2,m2,d2=input('请输入第二个日期：').strip().split()
y1,m1,d1,y2,m2,d2=int(y1),int(m1),int(d1),int(y2),int(m2),int(d2)
num1=yearnum(y1)+mdnum(m1)+daysnum(y1,m1,d1)
num2=yearnum(y2)+mdnum(m2)+daysnum(y2,m2,d2)
print(y1,'年至',y2,'年共有',num1-num2,'天')

