#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#squares = []
#for number in numbers:
#    squares.append(number**2)

#print(squares)

#print([number**2 for number in numbers])
# [expression for item in iterable]

#squares = []
#for number in numbers:
#    if number % 2:   
#        squares.append(number**2)
#print(squares)

#print([number**2 for number in number%2])
#


stopnie_fahrenheit = [32, 68, 104, 140]
# (Temperatura_f-32)*5/9 <- expression
print([(temperatura_f - 32) * 5 / 9 for temperatura_f in stopnie_fahrenheit])
# [expression for item in iterable if condition]

string = "hello@world123!@#"
#print("a".isalpha())
#print("1".isalpha())
print([znak for znak in string if znak.isalpha()])