import random

Apple_juice = 15.5
Orange_juice = 20
Grape_juice = 10.25

Total_volume = (Apple_juice + Orange_juice + Grape_juice)
print(Total_volume)

Total_Int = int(Total_volume)
print(Total_Int)

Total_String = str(Total_volume)
print("The Total Volume is:",Total_String)

Additional_litres = random.randrange(5, 10)
print("Additional litres are:", Additional_litres)

Final_value= Total_volume + Additional_litres
print("The Final Value is:",Final_value)