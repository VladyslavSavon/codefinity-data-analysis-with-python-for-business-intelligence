import matplotlib.pyplot as plt

def plot_monthly_sales(sample_sales):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    x_labels = months[:len(sample_sales)]
    plt.plot(x_labels, sample_sales, marker='o')
    for i, v in enumerate (sample_sales):
        plt.text(i + 0.8, v + max(sample_sales)*0.01, str(v), ha='center')
    plt.title('Monthly sales trends')
    plt.xlabel('Months')
    plt.ylabel('Sales($)')
    plt.show()
sample_sales = [1200, 1500, 1700, 1600, 1800, 2000, 2200, 2100, 2300, 2500, 2400, 2600]
plot_monthly_sales(sample_sales)