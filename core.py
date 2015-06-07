#!/usr/bin/python

from sqlalchemy import create_engine
import tushare as ts
import os

#result=ts.get_industry_classified()
engine=create_engine('mysql://root:310018@127.0.0.1/stock?charset=utf8',echo=True)
#result.to_sql('industry',engine)
result=ts.get_area_classified()
result.to_sql('area',engine)

#result.to_excel('/Users/xzp/industry.xlsx')
