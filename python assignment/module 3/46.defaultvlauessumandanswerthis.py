a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
ab={}
val=0
for c in a:
    if c['item'] not in ab:
        ab[c['item']] = c['amount']
    else:
        ab[c['item']] += c['amount'] 
print(ab) 
