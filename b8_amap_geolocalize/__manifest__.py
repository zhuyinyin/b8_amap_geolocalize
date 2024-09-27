# -*- coding: utf-8 -*-

{
    'name': '高德地图地理位置',
    'author': "yann zhu",
    'category': 'Hidden/Tools',
    'summary':"调用高德地图实现获取联系人经纬度 需要在系统基本设置高德web服务api key",
    'description': """高德地图地理位置""",
    'depends': ['base_geolocalize'],
    'data': [
        'views/res_config_settings_views.xml',
        'data/data.xml',
    ],
    'installable': True,
}
