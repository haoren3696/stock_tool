#!/usr/bin/python
# encoding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

engine=create_engine('mysql://root:310018@127.0.0.1/stock?charset=utf8',echo=True)
DB_session= sessionmaker(bind=engine)
session=DB_session()
result=session.execute('select c_name,count(*) as num from industry group by c_name;').fetchall()
session.close()
data={'type':[],'num':[]}
for i in result:
    data['type'].append(i[0])
    data['num'].append(i[1])
json_str=json.dumps(data)
print json_str



