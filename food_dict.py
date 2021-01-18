order={
    'client': 'John Doe',
    'item': 'Salad',
    'quantity': int(input("how many salads do you want?")),
    'price': 15.00,
}

order['total']=order['price']*order['quantity']
order['delivery']=str(input("do you want delivery?"))
    



if order['quantity']>=7:
    order['quantity']=order['quantity']*0.8
    order['total']=order['price']*order['quantity']

    print('PRICE X QUANTITY:', round(order['price'],2),'x', round(order['quantity'],2),"(discount -20%)")
    print(round(order['total'],2),"lei")
else:
    order['total']=order['price']*order['quantity']
    print("ORDER FOR:", order['client'])
    print("FOOD     :", order['item'])
    print('PRICE X QUANTITY:', order['price'],'x', order['quantity'])
    print(round(order['total'],2),"lei")
print(">>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
    
if order['total']>=300 and order['delivery']=='yes':
    print(round(order['total'],2),"lei", "with free delivery")
elif order['total']<=300 and order['delivery']=='yes':
    order['total']=order['total']+50
    print("Total price with delivery is:",round(order['total'],2),"lei")
elif order['total']<=300 and order['delivery']=='yes':
    order['total']=order['total']+50
    print("Total price with delivery is:",round(order['total'],2),"lei (delivery 50lei included")
elif order['delivery']!='yes':
    order['total']=order['total']
    print("Total price :",round(order['total'],2),"lei (no delivery)")

    

#HW1:Modify the code so that order['total'] discount 20% is more than 7 pieces.
#HW2: add code so the user-> question: do you need delivery?
    # based on the answer: total >300 and delivery==>
    #dictionary order['delivery']->'free', otherwise  order['delivery']->>+50 lei->> 'total updated'
    
   
