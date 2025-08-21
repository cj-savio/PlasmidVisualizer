import matplotlib.pyplot as plt

# Data for the chart
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)

# Draw a white circle at the center to create the "donut" hole
centre_circle = plt.Circle((0, 0), 0.90, fc='white')
fig = plt.gcf()

# Add the circle to the axes
ax.add_artist(centre_circle)

# Ensure the chart is a circle (equal aspect ratio)
ax.axis('equal')  

plt.tight_layout()
plt.title('Distribution of Forest Creatures')
plt.show()