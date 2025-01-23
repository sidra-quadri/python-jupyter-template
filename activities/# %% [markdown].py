# %% [markdown]
# # Matplotlib Activities 
# This notebook contains activities to practice various types of plots and visualizations using Matplotlib.

# %% [markdown]
# ## Activity 1: Basic Line Plot
# ### Objective: Create a simple line plot to visualize data.
# #### Instructions:
# 1. Create a list of x-values (`[0, 1, 2, 3, 4, 5]`) and a list of corresponding y-values (`[0, 1, 4, 9, 16, 25]`).
# 2. Use Matplotlib to plot these values as a line graph.
# 3. Label the axes as `x` and `y`.
# 4. Give the plot a title: `Basic Line Plot`.
# 

# %%
import matplotlib.pyplot as plt
# Data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create a line plot
plt.plot(x, y)

# Labeling the axes and the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Basic Line Plot')

# Show the plot
plt.show()

# %% [markdown]
# ## Activity 2: Bar Plot
# ### Objective: Create a bar plot to visualize categorical data.
# #### Instructions:
# 1. Create a list of categories (`['Category A', 'Category B', 'Category C', 'Category D']`) and corresponding values (`[4, 7, 3, 6]`).
# 2. Use Matplotlib to create a bar plot.
# 3. Add labels for the x and y axes.
# 4. Add a title to the plot: `Bar Plot Example`.

# %%
# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [4, 7, 3, 6]

# Create a bar plot
plt.bar(categories, values)

# Labeling the axes and the plot
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')

# Show the plot
plt.show()

# %% [markdown]
# ## Activity 3: Scatter Plot
# ### Objective: Create a scatter plot to visualize the relationship between two variables.
# #### Instructions:
# 1. Create two lists of random values for x and y (e.g., `x = [1, 2, 3, 4, 5]`, `y = [5, 4, 3, 2, 1]`).
# 2. Use Matplotlib to plot a scatter plot.
# 3. Add labels for the axes and a title: `Scatter Plot Example`.

# %%
# Data
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# Create a scatter plot
plt.scatter(x, y)

# Labeling the axes and the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Example')

# Show the plot
plt.show()

# %% [markdown]
# ## Activity 4: Histogram
# ### Objective: Create a histogram to visualize the distribution of a dataset.
# #### Instructions:
# 1. Create a list of random values (e.g., `data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]`).
# 2. Use Matplotlib to create a histogram with 5 bins.
# 3. Label the axes and give the plot a title: `Histogram Example`.

# %%
# Data
data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]

# Create a histogram
plt.hist(data, bins=5)

# Labeling the axes and the plot
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Show the plot
plt.show()

# %% [markdown]
# ## Activity 5: Pie Chart
# ### Objective: Create a pie chart to visualize the proportions of different categories.
# #### Instructions:
# 1. Create a list of categories (`['Apple', 'Banana', 'Cherry', 'Date']`) and their corresponding values (`[10, 15, 7, 5]`).
# 2. Use Matplotlib to create a pie chart.
# 3. Add a title to the chart: `Fruit Pie Chart`.

# %%
# Data
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [10, 15, 7, 5]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Title
plt.title('Fruit Pie Chart')

# Show the plot
plt.show()

# %% [markdown]
# ## Activity 6: Multiple Subplots
# ### Objective: Create multiple subplots to visualize different types of plots in one figure.
# #### Instructions:
# 1. Create a figure with 2 rows and 2 columns of subplots.
# 2. In the first subplot, create a line plot.
# 3. In the second subplot, create a bar plot.
# 4. In the third subplot, create a scatter plot.
# 5. In the fourth subplot, create a pie chart.

# %%
# Data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
categories = ['A', 'B', 'C', 'D']
values = [5, 3, 9, 6]
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [10, 15, 7, 5]

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# First subplot: Line plot
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')

# Second subplot: Bar plot
axs[0, 1].bar(categories, values)
axs[0, 1].set_title('Bar Plot')

# Third subplot: Scatter plot
axs[1, 0].scatter(x, y)
axs[1, 0].set_title('Scatter Plot')

# Fourth subplot: Pie chart
axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%')
axs[1, 1].set_title('Pie Chart')

# Show the plots
plt.show()


