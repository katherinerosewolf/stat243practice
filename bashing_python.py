with open("station_count_states.txt", "r") as file:
    for line in file:
        result = ",".join(line.split()[::-1])
        print(f"{result}")