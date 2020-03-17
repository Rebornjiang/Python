from stock_class import Stock
import time




# 
stock_list = []


print("欢迎来到股票托管系统!")
def adding_stock_info():
	while True:

		print("请输入您需要监测的支股票信息")
		code = input("请输入您想要检测的股票代码")

		buy_point = float(input("请输入您需要的买点价格"))

		sale_point = float(input("请输入您需要的卖点价格"))

		#股票对象实例化,并将实例化之后的对象加入列表。
		stock = Stock(code,buy_point,sale_point)

		stock_list.append(stock)

		print("如不需要监测其他的其他的股票请输入：n")
		choice = input("请输入您的选择")
		if choice == "n":
			break
		



while True:

	adding_stock_info()

	while True:

		for stock in stock_list:

			#获取股民数据
			stock.get_stock_data()

			#股票提醒功能
			stock.stock_remind()

			print("--------")

		time.sleep(30)


		





