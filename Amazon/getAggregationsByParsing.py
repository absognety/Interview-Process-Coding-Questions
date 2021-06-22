# Input:
    
sales_data = [{'channel':'Amazon', 'id':'AMZ456', 'sales':10, 'returns':0},
    {'channel':'Amazon', 'id':'AMZ123', 'sales':5, 'returns':2},
    {'channel':'Shopify', 'id':'1234', 'sales':15, 'returns':0},
    {'channel':'Target', 'id':'TGT456', 'sales':23, 'returns':5}
  ]
 
channel_thrasio_mapping = {
    'AMAZON':{'AMZ123':'THRASIO-987', 'AMZ456':'THRASIO-456'},
  'SHOPIFY':{'1234':'THRASIO-987', '5678':'THRASIO-321'}
  }
 
#Expected Output:
    # [
#   {'id':'THRASIO-987', 'net_sales':18, 'returns':2},
#   {'id':'THRASIO-456', 'net_sales':10, 'returns':0},
# ]

result = []
for k1,v1 in channel_thrasio_mapping.items():
    for k2,v2 in v1.items():
        temp_dict = {}
        temp_dict['id'] = v2
        all_sales = []
        all_returns = []
        for s in sales_data:
            if s['id'] == k2:
                all_sales.append(s['sales'])
                all_returns.append(s['returns'])
        net_sales = sum(all_sales)-sum(all_returns)
        returns = sum(all_returns)
        temp_dict['net_sales'] = net_sales
        temp_dict['returns'] = returns
        result.append(temp_dict)
    
    
#print (result)
unique_thrasio_ids = set([t['id'] for t in result])
#print (unique_thrasio_ids)

output = []
for utd in unique_thrasio_ids:
    final_result = {}
    final_result['id'] = utd
    final_result['net_sales'] = 0
    final_result['returns'] = 0
    for res in result:
        if res['id'] == utd:
            final_result['net_sales'] += res['net_sales']
            final_result['returns'] += res['returns']
    output.append(final_result)

print (output)