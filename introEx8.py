print("\tStock Transaction Program ")
print("Total number of Stocks joe purchase was 1000 ")
print("Share purchase amount per stock 32.87$")

Invest = 32.87 * 1000
print("Joe invest " + str(Invest) + "$ last month")
Commission_for_Broker = (2/100)* Invest
print("Commission for stock broker is 2% from total amount which is " + str(Commission_for_Broker) + "$")
Total_Invest_amount = Invest + Commission_for_Broker
print("Total amount invested before " + str(Total_Invest_amount) + "$\n")

print("Joe sold 1000 stocks for 33.92$ ")
Balance = 1000*33.92
print("Joe get " + str(Balance) + "$ after sold ")
Broker_Amount = (2/100) * Balance
print("Joe paid " + str(Broker_Amount) + "$ after sold stocks")
Total_Amount_after_sold = Balance - Broker_Amount
print("Joe amount after sold " + str(Total_Amount_after_sold) + "$")

Final_amount = (Total_Amount_after_sold - Total_Invest_amount)
print("\nRemain amount " + str(Final_amount) +"$")

Final_amount = (Total_Amount_after_sold - Total_Invest_amount)<0
print("\nJoe is in Loss "+ str(Final_amount))
Final_amount = (Total_Amount_after_sold - Total_Invest_amount)>0
print("Joe made a Profit "+ str(Final_amount))









