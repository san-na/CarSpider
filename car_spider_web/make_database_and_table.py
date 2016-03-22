# -*- coding: utf-8 -*-

from torndb import Connection

db = Connection('127.0.0.1', 'mysql', 'root')

try:
    db.execute('create database `car_spider`;')
    print 'create database success.'
except:
    print 'database exists.'
    pass

car_info_sql = """
CREATE TABLE `car_spider`.`car` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `logo` varchar(200) NOT NULL,
    `model` varchar(255),
    `befor_price` varchar(100),
    `after_price` int(12),
    `plan` varchar(500),
    `Purchased` int(12),
    `link` varchar(255) default "",
    `created` datetime,
    `updated` datetime,
    `status` varchar(10),
    PRIMARY KEY (`id`),
    INDEX `idx_dt` (created)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
"""

try:
    db.execute(car_info_sql)
    print 'create table success.'
except:
    print 'table exists.'
    pass
