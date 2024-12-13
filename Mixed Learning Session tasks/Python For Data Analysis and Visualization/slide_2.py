# Task 1

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data points for S&P 500 and FTSE 100 indices
dates = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
sp500 = [4100, 4120, 4115, 4140, 4165]  # Example values for S&P 500
ftse100 = [7500, 7525, 7530, 7550, 7570]  # Example values for FTSE 100

# Convert dates to pandas datetime format for better handling
dates = pd.to_datetime(dates)

# Create a DataFrame for visualization purposes
data = pd.DataFrame({
    'Date': dates,
    'S&P 500': sp500,
    'FTSE 100': ftse100
})

# Display the data to check
print(data)

# ---------------------------------------------------------------------------
# Task 2

# Plot S&P 500
plt.figure(figsize=(8, 4))
plt.plot(data['Date'], data['S&P 500'], marker='o', color='blue', label='S&P 500')
plt.title('S&P 500 Index')
plt.xlabel('Date')
plt.ylabel('Index Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Plot FTSE 100
plt.figure(figsize=(8, 4))
plt.plot(data['Date'], data['FTSE 100'], marker='o', color='green', label='FTSE 100')
plt.title('FTSE 100 Index')
plt.xlabel('Date')
plt.ylabel('Index Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()


# ---------------------------------------------------------------------------
# Task 3
# Plot both S&P 500 and FTSE 100 on the same graph
plt.figure(figsize=(8, 6))
plt.plot(data['Date'], data['S&P 500'], marker='o', color='blue', label='S&P 500')
plt.plot(data['Date'], data['FTSE 100'], marker='x', color='green', label='FTSE 100')
plt.title('S&P 500 and FTSE 100 Indices')
plt.xlabel('Date')
plt.ylabel('Index Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# ---------------------------------------------------------------------------
# Task 4

# Custom data for scatter plot and bar chart (e.g., sales data)
x = np.arange(1, 41)  # 40 data points, e.g., days or months
y = np.random.randint(10, 100, size=40)  # Random sales values between 10 and 100

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='purple', label='Sales')
plt.title('Sales Data (Scatter Plot)')
plt.xlabel('Time (Days or Months)')
plt.ylabel('Sales Value')
plt.grid(True)
plt.legend()
plt.show()

# Bar Chart
plt.figure(figsize=(8, 6))
plt.bar(x, y, color='orange', label='Sales')
plt.title('Sales Data (Bar Chart)')
plt.xlabel('Time (Days or Months)')
plt.ylabel('Sales Value')
plt.grid(True)
plt.legend()
plt.show()
