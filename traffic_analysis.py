# Smart City Traffic Analytics System

junctions = [
    {
        "Junction ID": "J101",
        "Vehicle Count": 500,
        "Average Speed": 40,
        "Accident Count": 3,
        "Signal Delay": 60,
        "Pollution Index": 180,
        "Peak Hour Traffic": 700
    },
    {
        "Junction ID": "J102",
        "Vehicle Count": 350,
        "Average Speed": 45,
        "Accident Count": 1,
        "Signal Delay": 35,
        "Pollution Index": 120,
        "Peak Hour Traffic": 500
    },
    {
        "Junction ID": "J103",
        "Vehicle Count": 650,
        "Average Speed": 30,
        "Accident Count": 5,
        "Signal Delay": 90,
        "Pollution Index": 250,
        "Peak Hour Traffic": 900
    },
    {
        "Junction ID": "J104",
        "Vehicle Count": 450,
        "Average Speed": 38,
        "Accident Count": 2,
        "Signal Delay": 50,
        "Pollution Index": 170,
        "Peak Hour Traffic": 650
    },
    {
        "Junction ID": "J105",
        "Vehicle Count": 700,
        "Average Speed": 28,
        "Accident Count": 6,
        "Signal Delay": 100,
        "Pollution Index": 280,
        "Peak Hour Traffic": 1000
    }
]

print("\nSMART CITY TRAFFIC ANALYTICS SYSTEM\n")

# Question 1
print("1. Congestion Score")
for j in junctions:
    j["Congestion"] = (j["Vehicle Count"] * j["Signal Delay"]) / j["Average Speed"]
    print(j["Junction ID"], "=", round(j["Congestion"], 2))

# Question 2
print("\n2. Rank Junctions")
ranked = sorted(junctions, key=lambda x: x["Congestion"], reverse=True)
rank = 1
for j in ranked:
    print(rank, j["Junction ID"], round(j["Congestion"], 2))
    rank += 1

# Question 3
print("\n3. Accident-Prone Areas")
for j in junctions:
    if j["Accident Count"] >= 3:
        print(j["Junction ID"], "-", j["Accident Count"], "Accidents")

# Question 4
print("\n4. Highly Polluted Junctions")
for j in junctions:
    if j["Pollution Index"] > 200:
        print(j["Junction ID"], "-", j["Pollution Index"])

# Question 5
print("\n5. City Average Congestion")
total = 0
for j in junctions:
    total += j["Congestion"]

average = total / len(junctions)
print("Average Congestion =", round(average, 2))

# Question 6
print("\n6. Busiest Junction")
busy = max(junctions, key=lambda x: x["Peak Hour Traffic"])
print(busy["Junction ID"], "-", busy["Peak Hour Traffic"])

# Question 7
print("\n7. Traffic Alerts")

alerts = ""

for j in junctions:
    if j["Congestion"] > average:
        msg = "ALERT : " + j["Junction ID"] + " Heavy Traffic\n"
        alerts += msg
        print(msg, end="")

# Question 8
print("\n8. Saving Alerts")

file = open("traffic_alerts.txt", "w")
file.write(alerts)
file.close()

print("Alerts Saved Successfully")

# Question 9
print("\n9. Junctions Sorted by Vehicle Count")

vehicle_sorted = sorted(junctions,
                        key=lambda x: x["Vehicle Count"],
                        reverse=True)

for j in vehicle_sorted:
    print(j["Junction ID"], j["Vehicle Count"])

# Question 10
print("\n10. Top 5 Congestion Points")

top5 = sorted(junctions,
              key=lambda x: x["Congestion"],
              reverse=True)

for j in top5[:5]:
    print(j["Junction ID"], round(j["Congestion"], 2))

print("\nReading Saved Alerts\n")

try:
    file = open("traffic_alerts.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Alert file not found.")