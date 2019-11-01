# -*- coding: utf-8 -*-
# 一年以后来优化此代码


def is_leap_year(year):
    """闰年判定：指定一个年份，判断它是否是闰年"""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def get_year_num(year):
    """计算这一年之前有多少天， 不包含这一年"""
    days = 0
    for i in range(1, year):
        days += 366 if is_leap_year(i) else 365
    return days


def get_month_num(month, year):
    """计算这个月之前有多少天， 不包含这个月"""
    each_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # 每个月的天数
    days = 0
    for m in range(1, month):
        days += 29 if m == 2 and is_leap_year(year) else each_month[m]
    return days


def sum_days(year, month, day):
    """计算日期之前有多少天"""
    return get_year_num(year)+get_month_num(month, year)+day


date1 = [1996, 8, 29]
date2 = [2019, 11, 1]
print(sum_days(*date2) - sum_days(*date1))
