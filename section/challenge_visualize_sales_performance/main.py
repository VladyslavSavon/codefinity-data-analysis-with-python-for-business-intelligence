import matplotlib.pyplot as plt

def plot_sales_performance(summary_dict):
    product_names = list(summary_dict.keys())
    revenues = list(summary_dict.values())
    
    bars = plt.bar(product_names, revenues, color='grey')
    plt.title('Sales Performance')
    plt.xlabel('Product name')
    plt.ylabel('Revenue')
    plt.xticks(rotation=30)

    for bar, revenue in zip(bars, revenues):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            str(revenue),
            ha='center',
            va='bottom'
                )
    plt.tight_layout()
    plt.show()
# Sample usage
summary_dict = {"Widget": 15000, "Gadget": 12000, "Doohickey": 9000}
plot_sales_performance(summary_dict)
