# #Write a function that uses while, if and continue 
# # statements to print all the even numbers between 0 and 50.
def even_numberz():
    x = 0
    while x <= 50:
        x += 1
        if x % 2 != 0:
            continue
        print(x)

# #Write a function that takes an integer argument 
# # and prints "Prime" if the number is prime, and
# #  "Not prime" if the number is not prime.
def prime_numbers(x):
    if x<=1:
        print("not prime")
    elif x>1:
        for i in range(2,x):
            if x%i==0:
                print("not prime")
                break
        else:
            print("prime")

    

# #Write a function that takes a list of integers as input 
# # and prints the sum of all the even numbers in the list.
# # nums = [1,2,3,4,5,6,7,8,9]
def even_nums(nums):
    sum3 = 0
    for x in nums:
        if x % 2 == 0:
            sum3 += x
    print(sum3)

#Write a function that takes any two integers as input, and 
# prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.


def nums_ints(num1,num2):
    total = 0
    for y in range(num1,num2+1):
        if y % 3 == 0:
            total += y
    print(total)