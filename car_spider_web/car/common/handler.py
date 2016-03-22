#coding:utf-8
"""
爬取贵州师范大学2015年新生录取信息

Data:2015-11-14
"""

import requests
from bs4 import BeautifulSoup
from models import Car

# set utf-8 env
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def get_content(url=''):
    """
    通过get请求获取页面数据

    return : requests obj

    """

    if url:
        pass
    else:
        url = "http://mall.autohome.com.cn/#pvareaid=103414"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"}

    # 当主机不可到达时会抛出异常所以加个异常处理
    try:
        r = requests.get(url, headers=headers)
    except:
        r = None
    return r


def get_car_info(info):
    """
    使用BeautifulSoup从页面中提取热销汽车相关信息

    """
    soup = BeautifulSoup(info)
    if soup.find_all('div', class_="list"):
        first_list_div = soup.find_all('div', class_="list")[0]
        cars = first_list_div.find_all('li')
    else:
        print '[-] 抓取汽车信息失败.'
        first_list_div = []
        cars = []
    return cars


def get_after_price(url):
    """
    由于通过domain/#pvareaid=103414获取汽车当前价格信息时卡了许久，
    所以另外写个def进入产品详情页面获取汽车价格信息。

    """
    content = get_content(url)
    soup = BeautifulSoup(content.text)
    after_price = soup.find('div', class_="detail-info-banner-main").b['price']
    return after_price


def save_data_in_db(data_list):
    """将数据保持到数据库中"""

    _befor_str = "productPriceReadable-"

    for data in data_list:

        # 获取汽车详情url
        url = data.find_all('a', href=True)[0]['href']
        link = 'http://mall.autohome.com.cn' + url

        # 获取汽车价格信息
        __tag = url.split('/')[2].split('-')[0]
        befor_price = data.find(id=_befor_str+__tag)
        if data.find(id=_befor_str+__tag):
            befor_price = data.find(id=_befor_str+__tag).text
        else:
            befor_price = ''
        after_price = get_after_price(link)

        # 获取汽车产品名和规格
        car_title = data.find('div', class_='carbox-title')['title'].split(' ', 1)
        logo = car_title[0]
        model = car_title[1]

        # 获取汽车购买方案
        plan = data.find('div', class_='carbox-tip')['title']

        # 获取汽车购买次数
        purchased = data.find('div', class_='carbox-number').span.text

        # 开始保存数据
        car = Car(logo, model, befor_price, after_price, plan, purchased, link)
        car.save()
    return True
