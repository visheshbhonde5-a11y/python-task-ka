#hello world ... by  YOUR_NAME
print("Hello, World!")

#2. create 2 variables cost_price , selling_price and calculate the profit or loss
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)

else:
    print("No Profit No Loss")


   # WAP to check wheather the num is odd or even
# Program to check odd or even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

    #4. WAP to check weather the age is valid and elegible for voting or not



age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

    #WAP to find the word1 and word2 is Anagram or Not


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Words are Anagram")
else:
    print("Words are Not Anagram")
