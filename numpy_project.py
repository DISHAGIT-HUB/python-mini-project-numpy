import numpy as np

# Generate 50 random integers between 10 and 100
data = np.random.randint(10, 100, size=50)
print("random number stats using numpy in python:")

# Calculate statistics
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
maximum = np.max(data)
minimum = np.min(data)

# Display results
print("Random Numbers:\n", data)
print("\nMean:", mean)
print("\nMedian:", median)
print("\nStandard Deviation:", std_dev)
print("\nMaximum:", maximum)
print("\nMinimum:", minimum) 