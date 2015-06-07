#!/usr/bin/python

from bottle import route, run
from bottle import template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
engine=create_engine('mysql://root:310018@127.0.0.1/stock?charset=utf8')
DB_session= sessionmaker(bind=engine)

@route('/')
@route('/home')
def home():
    return template('template/home.html')

@route('/industry')
def get_industry():
    session=DB_session()
    result=session.execute('select c_name,count(*) as num from industry group by c_name order by num;').fetchall()
    session.close()
    data={'data':[]}
    for i in result:
        data['data'].append({'name':i[0],'value':i[1]})
    json_str=json.dumps(data)
    return json_str

@route('/area')
def get_area():
    session=DB_session()
    result=session.execute('select area,count(*) as num from area group by area order by num ;').fetchall()
    session.close()
    data={'type':[],'num':[]}
    for i in result:
        data['type'].append(i[0])
        data['num'].append(i[1])
    json_str=json.dumps(data)
    return json_str

@route('/map')
def get_area():
    session=DB_session()
    result=session.execute('select area,count(*) as num from area group by area order by num ;').fetchall()
    session.close()
    data={'map_data':[]}
    for i in result:
        data['map_data'].append({'name':i[0],'value':i[1]})
    json_str=json.dumps(data)
    return json_str



run(host='localhost', port=8080, debug=True)
