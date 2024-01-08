import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('NSD3.csv')
category_column = 'Timestamp'
value_column = 'How would you describe your overall mental state since the beginning of this school year?'

# Plotting a bar chart
plt.bar(df[category_column], df[value_column])

# Adding labels
plt.xlabel('Number of Students')
plt.ylabel('Overall mental state')
plt.title('Bar Chart from CSV')
plt.yticks([0, 1, 2, 3, 4, 5], ['Zero', 'One', 'Two', 'Three', 'Four', 'Five'])
plt.xticks([3, 6, 9, 12, 15], ['Three', 'Six', 'Nine', 'Twelve', 'Fifteen'])

# Show the plot
plt.show()

