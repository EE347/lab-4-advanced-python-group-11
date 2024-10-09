def print_name():
    with open('task3.txt', 'a') as file:

        name = input("Enter your name: ")
        file.write(name + "\n")
    file.close()


if __name__ == '__main__':

    n = 0

    while n != 3:
        print_name()
        n += 1