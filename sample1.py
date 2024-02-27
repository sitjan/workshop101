# import random


# def generate_random_number(start, end):
#     return random.randint(start, end)


# random_number = generate_random_number(1, 100)
# print("Random number:", random_number)

def main():
    total = 0
    for i in range(5):
        num = float(input("Enter number{}:".format(i+1)))
        total = total+num
    average = total/5
    print("The average of the number is: ", average)


if __name__ == "__main__":
    main()
