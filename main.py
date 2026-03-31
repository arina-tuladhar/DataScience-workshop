# def main():
#     print("Hello from dsworkshop!")


# if __name__ == "__main__":
#     main()

# while True:
#     grade = float(input("Enter your grade: "))

#     if grade > 3.6 and grade <= 4.0:
#         print("Your grade is A")

#     elif grade > 3.4 and grade <= 3.6:
#         print("Your grade is A-")

#     elif grade > 3.2 and grade <= 3.4:
#         print("Your grade is B")

#     else:
#         print("Your grade is C")

def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = [1, 2, 3, 4, 5]
print("sum of array ",sum(arr))
