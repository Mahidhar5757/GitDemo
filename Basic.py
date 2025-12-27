# #calculate age
# Name = input("Enter your Name")
# Age = int(input("enter age"))
# Calculated_age = int(input("enter dob in ddmmyy"))
#Are of Triangle



a = float(input("Enter a  number: "))
b = float(input("Enter a  number: "))
c = float(input("Enter a  number: "))

s = (a + b + c)/2

Area_of_Triangle = (s*(s-a)*(s-b)*(s-c))**0.5
print(round(Area_of_Triangle))

