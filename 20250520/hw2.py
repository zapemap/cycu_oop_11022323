import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the midterm scores data
df = pd.read_csv('20250520/midterm_scores.csv')

# Set the subjects to plot
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']

# Define bins for scores (0-10, 10-20, ..., 90-100)
bins = np.arange(0, 101, 10)
bin_centers = (bins[:-1] + bins[1:]) / 2  # Calculate the center of each bin

# Initialize the figure
plt.figure(figsize=(14, 8))

# Bar width and offset for each subject
bar_width = 1.0 / (len(subjects) + 1)  # Divide space equally for all subjects
offsets = np.arange(len(subjects)) * bar_width  # Offset for each subject

# Plot the bar chart for each subject
for i, subject in enumerate(subjects):
    counts, _ = np.histogram(df[subject], bins=bins)  # Count the number of students in each bin
    plt.bar(bin_centers + offsets[i], counts, width=bar_width, label=subject, edgecolor='black')

# Add labels and title
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Score Distribution by Subject (10-point Intervals)')
plt.xticks(bin_centers + bar_width * (len(subjects) - 1) / 2, [f'{int(bins[i])}-{int(bins[i+1])}' for i in range(len(bins) - 1)])
plt.legend(title='Subjects')
plt.tight_layout()

# Save the plot as an image
plt.savefig('20250520/midterm_scores_distribution_non_overlapping.png')
plt.show()