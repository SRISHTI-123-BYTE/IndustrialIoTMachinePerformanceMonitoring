# Industrial IoT Machine Performance Monitoring

machines = [
    {
        "Machine ID": "M101",
        "Plant": "Plant A",
        "Operating Hours": 220,
        "Downtime": 20,
        "Energy": 5000,
        "Units": 4000,
        "Maintenance": 120000
    },
    {
        "Machine ID": "M102",
        "Plant": "Plant A",
        "Operating Hours": 250,
        "Downtime": 10,
        "Energy": 6000,
        "Units": 5200,
        "Maintenance": 90000
    },
    {
        "Machine ID": "M103",
        "Plant": "Plant B",
        "Operating Hours": 200,
        "Downtime": 30,
        "Energy": 4500,
        "Units": 3200,
        "Maintenance": 150000
    },
    {
        "Machine ID": "M104",
        "Plant": "Plant B",
        "Operating Hours": 240,
        "Downtime": 20,
        "Energy": 5800,
        "Units": 4800,
        "Maintenance": 100000
    },
    {
        "Machine ID": "M105",
        "Plant": "Plant C",
        "Operating Hours": 230,
        "Downtime": 15,
        "Energy": 5200,
        "Units": 4300,
        "Maintenance": 130000
    }
]

print("\nINDUSTRIAL IoT MACHINE PERFORMANCE MONITORING\n")

# Question 1
print("1. Machine Efficiency")
for m in machines:
    working = m["Operating Hours"] - m["Downtime"]
    m["Efficiency"] = m["Units"] / working
    print(m["Machine ID"], "=", round(m["Efficiency"], 2))

# Question 2
print("\n2. Production Cost Per Unit")
for m in machines:
    m["Cost"] = m["Energy"] / m["Units"]
    print(m["Machine ID"], "=", round(m["Cost"], 2))

# Question 3
print("\n3. Inefficient Machines")
for m in machines:
    if m["Efficiency"] < 20:
        print(m["Machine ID"], "-", round(m["Efficiency"], 2))

# Question 4
print("\n4. Highest Maintenance Cost")
highest = max(machines, key=lambda x: x["Maintenance"])
print(highest["Machine ID"], "-", highest["Maintenance"])

# Question 5
print("\n5. Plant-wise Efficiency")
plants = {}

for m in machines:
    if m["Plant"] not in plants:
        plants[m["Plant"]] = []

    plants[m["Plant"]].append(m["Efficiency"])

for p in plants:
    avg = sum(plants[p]) / len(plants[p])
    print(p, "=", round(avg, 2))

# Question 6
print("\n6. Preventive Maintenance Required")
for m in machines:
    if m["Maintenance"] > 120000:
        print(m["Machine ID"])

# Question 7
print("\n7. Machines Sorted by Efficiency")
sorted_list = sorted(machines, key=lambda x: x["Efficiency"], reverse=True)

for m in sorted_list:
    print(m["Machine ID"], round(m["Efficiency"], 2))

# Question 8
print("\n8. Maintenance Report")

report = ""

for m in sorted_list:
    line = (f'{m["Machine ID"]} | {m["Plant"]} | '
            f'Efficiency={round(m["Efficiency"],2)} | '
            f'Maintenance={m["Maintenance"]}\n')
    report += line
    print(line, end="")

# Question 9
print("\n9. Saving Report")

file = open("maintenance_report.txt", "w")
file.write(report)
file.close()

print("Report Saved Successfully")

# Question 10
print("\n10. Reading Report")

try:
    file = open("maintenance_report.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Report file not found")