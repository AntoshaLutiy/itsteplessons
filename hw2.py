def sum_numbers(a,b):
    return a+b

def max_number(numbers):
    return max(numbers)

def count_letters(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def square_list(numbers):
    return [i ** 2 for i in numbers]

def palindrome(text):
    text = text.lower()
    return text[::-1] == text

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a,b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b

def perfect_number(n):
    sum_d = sum(i for i in range(1,n)if n%i == 0)
    return sum_d == n

PI =3.14159
def circle_area(radius):
    area = PI*radius**2
    return area

DAYS_IN_A_WEEK = 7
def weeks_days(weeks):
    return weeks * DAYS_IN_A_WEEK

Tax_Rate = 0.2
def tax_sum(money):
    return money * Tax_Rate

MAX_ATTEMPTS = 3
def check_password(correct_password):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        password = input("Enter your password: ")
        if password == correct_password:
            print("Password match")
            return
        attempts += 1
    print("Password not match")


SPEED_OF_LIGHT = 299792458
def light_travel(distance):
    return distance / SPEED_OF_LIGHT

