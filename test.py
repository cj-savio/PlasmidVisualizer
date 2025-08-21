import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
labels = ['AraC ORF', 'attR1', 'Chloramphenicol', 'ccdB', 'PmA', 'Bgl I']
sizes = [25, 5, 25, 10, 5, 30] # Adjusted sizes for visual balance
colors = ['#0074D9', '#FF851B', '#0074D9', '#B10DC9', '#FF851B', '#AAAAAA']

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
# Note: We remove the 'labels' argument from the pie() call
wedges, texts, autotexts = ax.pie(sizes, 
                                  colors=colors, 
                                  autopct='%1.1f%%', 
                                  startangle=90, 
                                  pctdistance=0.85)

# Draw a white circle at the center to create the donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# --- CUSTOM ANNOTATION PART ---
# Add text in the center of the donut
ax.text(0, 0, 'pCHART-DEMO\n6160 units', ha='center', va='center', fontsize=12)

# Loop through each wedge to draw custom annotations
for i, wedge in enumerate(wedges):
    # Calculate the angle of the middle of the wedge
    angle = (wedge.theta1 + wedge.theta2) / 2.
    ang_rad = np.radians(angle)

    # 1. Point on the circumference (for the tick mark)
    x1 = wedge.r * np.cos(ang_rad)
    y1 = wedge.r * np.sin(ang_rad)

    # 2. The "elbow" point of the connecting line
    x2 = (wedge.r + 0.1) * np.cos(ang_rad)
    y2 = (wedge.r + 0.1) * np.sin(ang_rad)
    
    # 3. The starting point of the horizontal line for the text
    # The x-position is pushed to the left or right
    x3 = 1.3 * np.sign(np.cos(ang_rad))
    y3 = y2

    # Set horizontal alignment for the text based on which side of the chart it is
    horizontalalignment = 'right' if angle > 180 else 'left'

    # Draw the connecting lines
    ax.plot([x1, x2], [y1, y2], color='black', lw=0.7) # Radial line (tick)
    ax.plot([x2, x3], [y2, y3], color='black', lw=0.7) # Horizontal line

    # Draw the text
    ax.text(x3, y3, labels[i], ha=horizontalalignment, va='center', fontsize=10)

# --- END ANNOTATION PART ---

ax.axis('equal')
# We don't need tight_layout() here as it can interfere with custom annotations
# plt.tight_layout() 
plt.show()