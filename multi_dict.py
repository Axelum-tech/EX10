product={
    'name': 'xPhone',
    'year': 2020,
    'brand':'Peach',
    'used': True,
    'price': {
        'value':1000,
        'currency':'EUR',
    }
}

print(product['name'])
print (product['price']['value'],end=" ")
print (product['price']['currency'])