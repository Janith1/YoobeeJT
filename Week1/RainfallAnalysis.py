def rainfall_analysis():
    import numpy as np

    rainfall = np.array ([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])

    #print rainfall values
    for i, rain in enumerate(rainfall):
        print(f"Day {i+1} rainfall: {rain}")

    #Total rainfall for the week
    print(f"\nTotal rainfall for the week: {np.sum(rainfall):.2f}")

    #Average rainfall for the week
    print(f"Average rainfall for the week: {np.average(rainfall):.2f}")

    #Count of no rainy days
    count = np.where(rainfall == 0.0)
    print(f"\nCount of no rainy days: {np.size(count)}")

    #High rainy days for the week
    print(f"\nHigh rainy days for the week:")
    high_rain = np.where(rainfall > 5.0)[0]
    for index in high_rain:
        print(f"Day {index+1} rainfall: {rainfall[index]}")

if __name__ == "__main__":
    rainfall_analysis()