#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

# **********************************************************
# * 作者        : 刘洋华
# * 邮箱        : Liuyh799@163.com
# * 创建时间    : 2019-07-23 14:52
# * 修改时间    : 2019-07-23 14:52
# * 文件名      : erwm.py
# * Description : 192.168
# **********************************************************

from  flask import Flask
from  flask import  render_template
from  flask import  request
import qrcode
import  time

app = Flask(__name__)#框架
@app.route('/')#路由
def index():#语法
    return render_template('shouye.html')#渲染模板
@app.route('/shouye',methods=['GET','POST'])
def shouye():
    if request.method == 'GET':
        return u'当前为GET请求'
    http_shouye = request.form.get('text')#网页
    img = qrcode.make(http_shouye)#通过库生成
    path = 'static/qrimg/%s.png' %time.time()#保存路径
    img.save(path)
    return render_template('img.html',qrimg=path)
if __name__ == '__main__':
    app.run(port=80,debug=True)