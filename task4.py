with open("task3.txt", "r") as file:
    file_lines = file.readlines()

    for line in file_lines:
        print(line.strip())