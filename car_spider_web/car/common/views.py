# -*- coding: utf-8 -*-

from car.common import Common

from flask import render_template, redirect, url_for, flash
import handler


@Common.route('/')
def index():
    """
    首页
    """
    data_list = handler.get_data_from_db()
    return render_template('index.html', data_list=data_list)


@Common.route('/get_data')
def get_data():
    """
    获取数据
    """

    # flash('Please wait a moment.')
    content = handler.get_content()
    car_info = handler.get_car_info(content.text)
    if handler.save_data_in_db(car_info):
        flash('success')
    return redirect(url_for('Common.index'))
