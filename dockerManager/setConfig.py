#!/usr/bin/python
#coding:utf-8

from jinja2 import Template
import sys
reload(sys)
sys.setdefaultencoding('utf8')

configs = [{'domain': 'sc.edu88.com',
           'upstream': {'name': 'etoh','server': ['10.102.43.114:8081','10.102.43.115:8080']},
           'location':'/'}]

with open('/root/workspace/dockerDev/dockerManager/nginx.conf.tpl') as tpl_file:
    template = Template(tpl_file.read())
    with open('/root/workspace/dockerDev/dockerManager/nginx.conf','w') as cfg_file:
        cfg_file.write(template.render(configs=configs))
