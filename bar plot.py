import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 9]
colors = ['red', 'blue', 'green', 'purple']  
plt.bar(categories, values, color=colors)
plt.title("Bar Plot of Categories")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
