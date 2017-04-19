from pymongo import MongoClient
import tushare as ts

client = MongoClient()

db = client.stockdb

stock_c = db.stock_c

# stocks=ts.get_stock_basics()

# #i=3
# for index, row in stocks.iterrows():
# 	#if i<3:
# 		stock={	u'code':index
# 				,u'name':row[u'name']
# 				,u'industry':row[u'industry']
# 				,u'area':row[u'area']
# 				,u'pe':row[u'pe']
# 				,u'outstanding':row[u'outstanding']
# 				,u'totals':row[u'totals']
# 				,u'totalAssets':row[u'totalAssets']
# 				,u'liquidAssets':row[u'liquidAssets']
# 				,u'fixedAssets':row[u'fixedAssets']
# 				,u'reserved':row[u'reserved']
# 				,u'reservedPerS':row[u'reservedPerShare']
# 				,u'esp':row[u'esp']
# 				,u'bvps':row[u'bvps']
# 				,u'pb':row[u'pb']
# 				,u'timeToMarket':row[u'timeToMarket']
# 				,u'undp':row[u'undp']
# 				,u'perundp':row[u'perundp']
# 				,u'rev':row[u'rev']
# 				,u'profit':row[u'profit']
# 				,u'gpr':row[u'gpr']
# 				,u'npr':row[u'npr']
# 				,u'holders':row[u'holders']}
# 		stock_c.insert_one(stock)
# 		i=i+1
print(stock_c.count())
	

