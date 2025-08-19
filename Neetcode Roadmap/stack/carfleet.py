def carFleet(target,position,speed):
    # Calculate the time taken for each car to reach the target
    time = [(target - p) / s for p, s in zip(position, speed)]
    # Sort the times in descending order
    time.sort(reverse=True)
    fleets = 0
    # Iterate through the times and count the number of fleets
    for i in range(len(time)):
        if i == 0 or time[i] > time[i - 1]:
            fleets += 1
    return fleets

print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))