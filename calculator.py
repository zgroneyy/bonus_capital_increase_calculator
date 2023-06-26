# -*- coding: utf-8 -*-
"""
Calculate number of stocks needed in capital increase through bonus issues 
in order to have "integer" number of stocks at the and of capital increase. 

>>Enter number of stocks you have
>>Get a list of 5 consist of # of stocks you need to have in order to have integer
"""
# Initial calculation was based on bonus capital increase of BIST.ISMEN, to be held on 2023
# 322.53521% 
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
decimal = str(yeni_lot_sayisi-int(yeni_lot_sayisi)).split('.')[1]
print("You have 0." + str(decimal) + " as decimal")

options_list = []
checker = 0
check=True
while check:
    if(is_int((lot + checker)*(bedelsiz_yuzde/100))):
        options_list.append(checker)
        if len(options_list) == 3:
            check=False
    checker+=1
print(options_list)


