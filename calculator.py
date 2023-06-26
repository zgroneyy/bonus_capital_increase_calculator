# -*- coding: utf-8 -*-
"""
Calculate number of stocks needed in capital increase through bonus issues 
in order to have "integer" number of stocks at the and of capital increase. 
"""

def is_int(val):
    if type(val) == int:
         return True
    else:
         if val.is_integer():
             return True
         else:
             return False
         
lot = float(input("# of Stocks: "))
bedelsiz_yuzde = 322.53521
yeni_lot_sayisi = int(lot) * (bedelsiz_yuzde)/100
print(yeni_lot_sayisi)

options_list = []
checker = 0
check=True
while check:
    if(is_int((lot + checker)*(bedelsiz_yuzde/100))):
        options_list.append(checker)
        if len(options_list) == 5:
            check=False
    checker+=1
print(options_list)


