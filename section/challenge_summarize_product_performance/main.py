def summarize_products(sales_records):
    summary = {}
    for row in sales_records:
        product = row['product']
        if product not in summary:
            summary[product] = {'units_sold': 0, 'revenue': 0}
        summary[product]['units_sold'] += row['units_sold']
        summary[product]['revenue'] += row['revenue']
    return summary

sales_data = [
    {'product': 'Widget', 'units_sold': 10, 'revenue': 250},
    {'product': 'Gadget', 'units_sold': 5, 'revenue': 150},
    {'product': 'Widget', 'units_sold': 7, 'revenue': 175},
    {'product': 'Gizmo', 'units_sold': 3, 'revenue': 90},
    {'product': 'Gadget', 'units_sold': 2, 'revenue': 60}
]
summary = summarize_products(sales_data)
for product, stats in summary.items():
    print(f"{product}: {stats['units_sold']} units, ${stats['revenue']} revenue")
