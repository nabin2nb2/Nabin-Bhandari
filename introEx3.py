
# 3.Go to xe.com and find how much a Canadian dollar is worth in Euros (EUR).-
# Make a program that allows the user to enter the amount of Canadian they -
# have and tell them what it is worth in Euros.

print ("\nConvert Canadian dollar into Euro\n ")
print ("Today Exchange Rate CAD 1$ = 0.675453 euro")

Canadian_Amount =  input("\tEnter the CAD Amount $: ")
Today_Exchange_Rate = 0.675453* int(Canadian_Amount)

print ("Your converted amount is " + str(Today_Exchange_Rate) + " EURO")

