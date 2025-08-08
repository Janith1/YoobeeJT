import numpy as np

# Temperature (°C)
temperatures_celsius = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# Calculate average temperature
average_temp_c = np.mean(temperatures_celsius)

# Maximum temperature
max_temp_c = np.max(temperatures_celsius)
# Minimum temperature
min_temp_c = np.min(temperatures_celsius)

# Convert to Fahrenheit
temperatures_fahrenheit = temperatures_celsius * 9/5 + 32

# Indices where temperature > 20°C
hot_days_indices = np.where(temperatures_celsius > 20)[0]

# Display results
print(f"The average temperature is {average_temp_c:.2f}°C")
print(f"The maximum temperature is {max_temp_c:.1f}°C")
print(f"The minimum temperature is {min_temp_c:.1f}°C")

print("\nTemperatures in Fahrenheit:")
for i, temp_f in enumerate(temperatures_fahrenheit):
    print(f"Day {i+1}: {temp_f:.2f}°F")

print("\nDays where temperature exceeded 20°C:")
for index in hot_days_indices:
    print(f"Day {index+1} (Temperature: {temperatures_celsius[index]}°C)")
