price = input ("Enter price: ")
gst = 1.06
pst = 1.08

if price <= 4.00:
	final_price = price * gst
else:
	final_price = price * pst

print ("The total is: " + repr(final_price))
