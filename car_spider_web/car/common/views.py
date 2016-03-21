# -*- coding: utf-8 -*-

from car.common import Common

from car.common.models import Car
from flask import render_template, redirect, url_for, flash
import requests, string, random

@Common.route('/')
def index():
    """
    首页
    """
    return render_template('index.html')
