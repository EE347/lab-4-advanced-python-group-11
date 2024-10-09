import csv

with open("task5.csv", "w", newline = "") as file:
    writer = csv.writer(file)

    while True:
        name = input("Enter your name (quit to end): ")
        if name.lower() == "quit":
            break

        writer.writerow([name])

with open("task5.csv", "r") as file:
    reader = csv.reader(file)

    print("\nNames entered: ")
    for row in reader:
        print(row[0])