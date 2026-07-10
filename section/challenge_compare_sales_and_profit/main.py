import matplotlib.pyplot as plt

def compare_sales_profit(sales, profits, products):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].bar(products, sales, color='skyblue', label='Sales')
    axes[0].set_title('Sales by Product')
    axes[0].set_ylabel('Sales')
    axes[0].set_xlabel('Product')
    axes[0].legend()

    axes[1].bar(products, profits, color='black', label='Profits')
    axes[1].set_title('Profit by Product')
    axes[1].set_ylabel('Profit')
    axes[1].set_xlabel('Product')
    axes[1].legend()

    plt.suptitle('Comparison of Sales and Profit Across Products')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Sample calls
sales = [1000, 1500, 800, 2000]
profits = [200, 300, 100, 400]
products = ['A', 'B', 'C', 'D']
compare_sales_profit(sales, profits, products)