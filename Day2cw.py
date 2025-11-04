header = """Akash Book Stores
Building Number: 150
Street Name: Kempegowda Circle
Street Address: Shop No. 5, Majestic Market, Tank Bund Road
State: Karnataka
City: Bengaluru
Post Code: 560009
RECEIPT"""

title_1 = "Python Basics"
title_2 = "Data Science Intro"
price_1 = 450
price_2 = 600

total_price = price_1 + price_2

print(header.upper())

display_1 = print("{0}:{1}".format(title_1.upper(), price_1))
display_2 = print("{0}:{1}".format(title_2.upper(), price_2))

 
print("Total Price:"+str(total_price) +"\n"+"THANK YOU")