import tushare


	

class Stock():

	'''有关股票的类'''

	def __init__(self,code,buy_point,sale_point):

		self.code = code

		self.buy_point = buy_point
		self.sale_point = sale_point



	def get_stock_data(self):

		stock = tushare.get_realtime_quotes(self.code)

		stock_name = stock.loc[0][0]
		global price_now
		price_now = float(stock.loc[0][3])
		hight_price = stock.loc[0][4]
		low_price = stock.loc[0][5]
		volumn = stock.loc[0][8]
		amount_price = stock.loc[0][9]
		open_price = stock.loc[0][1]
		close_price = stock.loc[0][2]
		time_data = stock.loc[0][30]

		print("股票名："+stock_name+"\t\t"+"股票价格："+str(price_now))

		return price_now
	


	def stock_remind(self):


		if price_now <= self.buy_point:
			print(price_now,"<=",self.buy_point)
			print("达到买点，请尽快购买")

		elif price_now >= self.sale_point:
			print("达到卖点，请尽快卖出")


		else:
			print("请继续观望")	
			


