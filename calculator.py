num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

choice = input("Enter the operation: (Operations +, -, *, /, %)")

if choice == "+":
  sum_of_num = num1 + num2
  print("addition: ", sum_of_num)
elif choice == "-":
  diff_of_num = num1 - num2
  print("subtraction: ", diff_of_num)
elif choice == "*":
  prod_of_num = num1 * num2
  print("multiplication: ", prod_of_num)
