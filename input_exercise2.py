#Exercise 2 shopping cart progarm

item=input('what item would you like to buy')
price=float(input('What is the price ?: '))
quantity=int(input('How many would like ?:'))
total=price*quantity
print(f' you have bought{quantity} {item}/s')
print(f' your total is:{total}')