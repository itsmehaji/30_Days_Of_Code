import math
mc=float(input())
tip_per=int(input())
tax_per=int(input())
tip=((mc)*(tip_per/100))
tax=((mc)*(tax_per/100))
print(round(mc+tip+tax))
